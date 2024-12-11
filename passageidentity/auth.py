"""Provides the Auth class for interacting with the Passage API."""

from __future__ import annotations

from typing import TYPE_CHECKING

import jwt as pyjwt

from passageidentity.errors import PassageError
from passageidentity.helper import fetch_app
from passageidentity.models.magic_link_args import MagicLinkWithEmailArgs, MagicLinkWithPhoneArgs, MagicLinkWithUserArgs
from passageidentity.openapi_client.api.magic_links_api import MagicLinksApi
from passageidentity.openapi_client.exceptions import ApiException
from passageidentity.openapi_client.models.create_magic_link_request import CreateMagicLinkRequest
from passageidentity.openapi_client.models.magic_link_channel import MagicLinkChannel

if TYPE_CHECKING:
    from passageidentity.models.magic_link_args import MagicLinkArgs
    from passageidentity.models.magic_link_options import MagicLinkOptions
    from passageidentity.openapi_client.models.magic_link import MagicLink


class Auth:
    """Auth class for handling operations to authenticate and validate JWTs."""

    def __init__(self, app_id: str, request_headers: dict[str, str]) -> None:
        """Initialize the Auth class with the app ID and request headers."""
        self.app_id = app_id
        self.request_headers = request_headers
        self.jwks = pyjwt.PyJWKClient(
            f"https://auth.passage.id/v1/apps/{self.app_id}/.well-known/jwks.json",
            # must set a user agent to avoid 403 from CF
            headers={"User-Agent": "passageidentity/python"},
        )
        self.app = fetch_app(self.app_id)

        self.magic_links_api = MagicLinksApi()

    def validate_jwt(self, jwt: str) -> str:
        """Verify the JWT and return the user ID for the authenticated user, or throw a PassageError."""
        if not jwt:
            msg = "jwt is required."
            raise ValueError(msg)

        try:
            kid = pyjwt.get_unverified_header(jwt)["kid"]
            public_key = self.jwks.get_signing_key(kid)
            claims = pyjwt.decode(
                jwt,
                public_key,
                audience=[self.app_id] if self.app["hosted"] else self.app["auth_origin"],
                algorithms=["RS256"],
            )

            return claims["sub"]
        except Exception as e:
            msg = f"JWT is not valid: {e}"
            raise PassageError(msg) from e

    def create_magic_link(self, args: MagicLinkArgs, options: MagicLinkOptions | None = None) -> MagicLink:
        """Create a Magic Link for your app."""
        payload = CreateMagicLinkRequest()
        payload.type = args.type
        payload.send = args.send

        if isinstance(args, MagicLinkWithEmailArgs):
            payload.email = args.email
            payload.channel = MagicLinkChannel.EMAIL
        elif isinstance(args, MagicLinkWithPhoneArgs):
            payload.phone = args.phone
            payload.channel = MagicLinkChannel.PHONE
        elif isinstance(args, MagicLinkWithUserArgs):
            payload.user_id = args.user_id
            payload.channel = args.channel
        else:
            msg = "args must be an instance of MagicLinkArgs"
            raise TypeError(msg)

        if options:
            payload.language = options.language
            payload.magic_link_path = options.magic_link_path
            payload.redirect_url = options.redirect_url
            payload.ttl = options.ttl

        try:
            return self.magic_links_api.create_magic_link(
                self.app_id,
                payload,
                _headers=self.request_headers,
            ).magic_link
        except ApiException as e:
            msg = "Could not create a magic link for this app"
            raise PassageError.from_response_error(e, msg) from e
