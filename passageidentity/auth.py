"""Provides the Auth class for interacting with the Passage API."""

from __future__ import annotations

from typing import TYPE_CHECKING

import jwt
import jwt.algorithms

from passageidentity.errors import PassageError
from passageidentity.helper import fetch_app
from passageidentity.openapi_client.api.magic_links_api import MagicLinksApi
from passageidentity.openapi_client.exceptions import ApiException
from passageidentity.openapi_client.models.create_magic_link_request import CreateMagicLinkRequest

if TYPE_CHECKING:
    from passageidentity.openapi_client.models.magic_link import MagicLink

CreateMagicLinkArgs = CreateMagicLinkRequest


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

    def create_magic_link(self, args: CreateMagicLinkArgs) -> MagicLink:
        """Create a Magic Link for your app."""
        magic_link_req = {}
        args_dict = args.to_dict() if isinstance(args, CreateMagicLinkRequest) else args

        magic_link_req["user_id"] = args_dict.get("user_id") or ""
        magic_link_req["email"] = args_dict.get("email") or ""
        magic_link_req["phone"] = args_dict.get("phone") or ""

        magic_link_req["language"] = args_dict.get("language") or ""
        magic_link_req["magic_link_path"] = args_dict.get("magic_link_path") or ""
        magic_link_req["redirect_url"] = args_dict.get("redirect_url") or ""
        magic_link_req["send"] = args_dict.get("send") or False
        magic_link_req["ttl"] = args_dict.get("ttl") or 0
        magic_link_req["type"] = args_dict.get("type") or "login"

        if args_dict.get("email"):
            magic_link_req["channel"] = args_dict.get("channel") or "email"
        elif args_dict.get("phone"):
            magic_link_req["channel"] = args_dict.get("channel") or "phone"

        try:
            return self.magic_links_api.create_magic_link(
                self.app_id,
                magic_link_req,  # type: ignore[arg-type]
                _headers=self.request_headers,
            ).magic_link
        except ApiException as e:
            msg = "Could not create a magic link for this app"
            raise PassageError.from_response_error(e, msg) from e
