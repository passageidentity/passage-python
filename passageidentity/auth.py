"""Provides the Auth class for interacting with the Passage API."""

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import jwt
import jwt.algorithms

from passageidentity.errors import PassageError
from passageidentity.helper import fetch_app
from passageidentity.openapi_client.api.magic_links_api import MagicLinksApi
from passageidentity.openapi_client.exceptions import ApiException

if TYPE_CHECKING:
    from passageidentity.openapi_client.models.magic_link import MagicLink
    from passageidentity.openapi_client.models.magic_link_channel import MagicLinkChannel
    from passageidentity.openapi_client.models.magic_link_type import MagicLinkType


class MagicLinkArgsBase:
    """Base class for MagicLinkArgs."""

    type: MagicLinkType
    send: bool


class MagicLinkWithEmailArgs(MagicLinkArgsBase):
    """Arguments for creating a Magic Link with an email."""

    email: str


class MagicLinkWithPhoneArgs(MagicLinkArgsBase):
    """Arguments for creating a Magic Link with a phone number."""

    phone: str


class MagicLinkWithUserArgs(MagicLinkArgsBase):
    """Arguments for creating a Magic Link with a user ID."""

    user_id: str
    channel: MagicLinkChannel


MagicLinkArgs = Union[MagicLinkWithEmailArgs, MagicLinkWithPhoneArgs, MagicLinkWithUserArgs]


class MagicLinkOptions:
    """Options for creating a Magic Link."""

    language: str | None
    magic_link_path: str | None
    redirect_url: str | None
    ttl: int | None


class Auth:
    """Auth class for handling operations to authenticate and validate JWTs."""

    def __init__(self, app_id: str, request_headers: dict[str, str]) -> None:
        """Initialize the Auth class with the app ID and request headers."""
        self.app_id = app_id
        self.request_headers = request_headers
        self.jwks = jwt.PyJWKClient(
            f"https://auth.passage.id/v1/apps/{self.app_id}/.well-known/jwks.json",
            # must set a user agent to avoid 403 from CF
            headers={"User-Agent": "passageidentity/python"},
        )
        self.app = fetch_app(self.app_id)

        self.magic_links_api = MagicLinksApi()

    def validate_jwt(self, token: str) -> str:
        """Verify the JWT and return the user ID for the authenticated user, or throw a PassageError."""
        try:
            kid = jwt.get_unverified_header(token)["kid"]
            public_key = self.jwks.get_signing_key(kid)
            claims = jwt.decode(
                token,
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
        payload = {
            "type": args.type,
            "send": args.send,
        }

        if isinstance(args, MagicLinkWithEmailArgs):
            payload["email"] = args.email
        elif isinstance(args, MagicLinkWithPhoneArgs):
            payload["phone"] = args.phone
        elif isinstance(args, MagicLinkWithUserArgs):
            payload["user_id"] = args.user_id
            payload["channel"] = args.channel
        else:
            msg = "args must be an instance of MagicLinkArgs"
            raise TypeError(msg)

        if options:
            payload["language"] = options.language
            payload["magic_link_path"] = options.magic_link_path
            payload["redirect_url"] = options.redirect_url
            payload["ttl"] = options.ttl

        try:
            return self.magic_links_api.create_magic_link(
                self.app_id,
                payload,  # type: ignore[arg-type]
                _headers=self.request_headers,
            ).magic_link
        except ApiException as e:
            msg = "Could not create a magic link for this app"
            raise PassageError.from_response_error(e, msg) from e
