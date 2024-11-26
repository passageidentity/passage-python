"""Provides the Passage class for interacting with the Passage API."""

from __future__ import annotations

from typing import TYPE_CHECKING

import typing_extensions

from passageidentity.auth import Auth
from passageidentity.errors import PassageError
from passageidentity.helper import get_auth_token_from_request
from passageidentity.openapi_client.api.magic_links_api import MagicLinksApi
from passageidentity.user import User

from .openapi_client.api import (
    AppsApi,
)

if TYPE_CHECKING:
    from requests.sessions import Request

    from .openapi_client.models import (
        AppInfo,
        CreateMagicLinkRequest,
        CreateUserRequest,
        MagicLinkType,
        UpdateUserRequest,
        UserInfo,
        WebAuthnDevices,
    )


class Passage:
    """Passage class for interacting with the Passage API."""

    COOKIE_AUTH = 1
    HEADER_AUTH = 2

    def __init__(self, app_id: str, api_key: str = "", auth_strategy: int = COOKIE_AUTH) -> None:
        """Initialize a new Passage instance."""
        if not app_id:
            msg = "A Passage app ID is required. Please include {app_id=YOUR_APP_ID, api_key=YOUR_API_KEY}."
            raise PassageError(msg)

        self.app_id: str = app_id
        self.passage_apikey: str = api_key
        self.auth_strategy: int = auth_strategy
        self.request_headers = {"Authorization": f"Bearer {api_key}"}

        self.auth = Auth(app_id, self.request_headers)
        self.user = User(app_id, self.request_headers)

    @typing_extensions.deprecated("Passage.validateJwt() will be deprecated. Use Passage.auth.validate_jwt() instead.")
    def validateJwt(self, token: str):  # noqa: ANN201, N802
        """Verify the JWT and return the user ID for the authenticated user, or throw a PassageError.

        Takes the place of the deprecated authenticateRequest() function.
        """
        return self.auth.validate_jwt(token)

    @typing_extensions.deprecated(
        "Passage.authenticateRequest() will be deprecated. Use Passage.auth.validate_jwt() instead.",
    )
    def authenticateRequest(self, request: Request) -> str | PassageError:  # noqa: N802
        """Authenticate a Flask or Django request that uses Passage for authentication.

        This function will verify the JWT and return the user ID for the authenticated user, or throw
        a PassageError.
        """
        # check for authorization header
        token = get_auth_token_from_request(request, self.auth_strategy)
        if not token:
            msg = "Could not find JWT."
            raise PassageError(msg)

        # load and parse the JWT
        try:
            return self.auth.validate_jwt(token)
        except Exception as e:
            msg = f"JWT is not valid: {e}"
            raise PassageError(msg) from e

    @typing_extensions.deprecated(
        "Passage.authenticateJWT() will be deprecated. Use Passage.auth.validate_jwt() instead.",
    )
    def authenticateJWT(self, token: str) -> str | PassageError:  # noqa: N802
        """Authenticate a JWT from Passage.

        This function will verify the JWT and return the user ID for the authenticated user, or throw a PassageError.
        This function can be used to authenticate JWTs from Passage if they are not sent in a typical cookie or
        authorization header.
        """
        return self.auth.validate_jwt(token)

    @typing_extensions.deprecated(
        "Passage.createMagicLink() will be deprecated. Use Passage.auth.create_magic_link() instead.",
    )
    def createMagicLink(  # noqa: N802
        self,
        magicLinkAttributes: CreateMagicLinkRequest,  # noqa: N803
    ) -> MagicLinkType | PassageError:
        """Create Passage MagicLink."""
        # if no api key, fail
        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        magic_link_req = {}

        magic_link_req["user_id"] = magicLinkAttributes.get("user_id") or ""  # type: ignore  # noqa: PGH003
        magic_link_req["email"] = magicLinkAttributes.get("email") or ""  # type: ignore  # noqa: PGH003
        magic_link_req["phone"] = magicLinkAttributes.get("phone") or ""  # type: ignore  # noqa: PGH003

        magic_link_req["language"] = magicLinkAttributes.get("language") or ""  # type: ignore  # noqa: PGH003
        magic_link_req["magic_link_path"] = (
            magicLinkAttributes.get("magic_link_path") or ""  # type: ignore  # noqa: PGH003
        )
        magic_link_req["redirect_url"] = magicLinkAttributes.get("redirect_url") or ""  # type: ignore  # noqa: PGH003
        magic_link_req["send"] = magicLinkAttributes.get("send") or False  # type: ignore  # noqa: PGH003
        magic_link_req["ttl"] = magicLinkAttributes.get("ttl") or 0  # type: ignore  # noqa: PGH003
        magic_link_req["type"] = magicLinkAttributes.get("type") or "login"  # type: ignore  # noqa: PGH003

        if magicLinkAttributes.get("email"):  # type: ignore  # noqa: PGH003
            magic_link_req["channel"] = magicLinkAttributes.get("channel") or "email"  # type: ignore  # noqa: PGH003
        elif magicLinkAttributes.get("phone"):  # type: ignore  # noqa: PGH003
            magic_link_req["channel"] = magicLinkAttributes.get("channel") or "phone"  # type: ignore  # noqa: PGH003

        try:
            client = MagicLinksApi()
            return client.create_magic_link(
                self.app_id,
                magic_link_req,  # type: ignore[arg-type]
                _headers=self.request_headers,
            ).magic_link  # type: ignore[attr-defined]
        except Exception as e:
            msg = f"Failed to create magic link: {e}"
            raise PassageError(msg) from e

    @typing_extensions.deprecated("Passage.getApp() will be removed without replacement.")
    def getApp(self) -> AppInfo | PassageError:  # noqa: N802
        """Use Passage API to get info for their app."""
        client = AppsApi()
        return client.get_app(self.app_id).app

    @typing_extensions.deprecated("Passage.getUser() will be deprecated. Use Passage.user.get() instead.")
    def getUser(self, user_id: str) -> UserInfo | PassageError:  # noqa: N802
        """Use Passage API to get info for a user, look up by user ID."""
        return self.user.get(user_id)

    @typing_extensions.deprecated(
        "Passage.getUserByIdentifier() will be deprecated. Use Passage.user.get_by_identifier() instead.",
    )
    def getUserByIdentifier(self, userIdentifier: str) -> UserInfo | PassageError:  # noqa: N802, N803
        """Use Passage API to get info for a user, look up by user identifier."""
        return self.user.get_by_identifier(userIdentifier)

    @typing_extensions.deprecated(
        "Passage.listUserDevices() will be deprecated. Use Passage.user.list_devices() instead.",
    )
    def listUserDevices(  # noqa: N802
        self,
        user_id: str,
    ) -> list[WebAuthnDevices] | PassageError:
        """Use Passage API to list user devices, look up by user ID."""
        return self.user.list_devices(user_id)

    @typing_extensions.deprecated(
        "Passage.deleteUserDevice() will be deprecated. Use Passage.user.revoke_device() instead.",
    )
    def deleteUserDevice(  # noqa: N802
        self,
        user_id: str,
        device_id: str,
    ) -> bool | PassageError:
        """Use Passage API to revoke user devices, look up by user ID."""
        self.user.revoke_device(user_id, device_id)
        return True

    @typing_extensions.deprecated(
        "Passage.revokeUserDevice() will be deprecated. Use Passage.user.revoke_device() instead.",
    )
    def revokeUserDevice(  # noqa: N802
        self,
        user_id: str,
        device_id: str,
    ) -> bool | PassageError:
        """Use Passage API to revoke user devices, look up by user ID."""
        self.user.revoke_device(user_id, device_id)
        return True

    @typing_extensions.deprecated(
        "Passage.revokeUserRefreshTokens() will be deprecated. Use Passage.user.revoke_refresh_tokens() instead.",
    )
    def revokeUserRefreshTokens(self, user_id: str) -> bool | PassageError:  # noqa: N802
        """Use Passage API to revoke all of a user's refresh tokens, look up by user ID."""
        self.user.revoke_refresh_tokens(user_id)
        return True

    @typing_extensions.deprecated(
        "Passage.signOut() will be deprecated. Use Passage.user.revoke_refresh_tokens() instead.",
    )
    def signOut(  # noqa: N802
        self,
        user_id: str,
    ) -> bool | PassageError:
        """Use Passage API to revoke all of a user's refresh tokens, look up by user ID."""
        self.user.revoke_refresh_tokens(user_id)
        return True

    @typing_extensions.deprecated("Passage.activateUser() will be deprecated. Use Passage.user.activate() instead.")
    def activateUser(self, user_id: str) -> UserInfo | PassageError:  # noqa: N802
        """Activate Passage User."""
        return self.user.activate(user_id)

    @typing_extensions.deprecated("Passage.deactivateUser() will be deprecated. Use Passage.user.deactivate() instead.")
    def deactivateUser(self, user_id: str) -> UserInfo | PassageError:  # noqa: N802
        """Deactivate Passage User."""
        return self.user.deactivate(user_id)

    @typing_extensions.deprecated("Passage.updateUser() will be deprecated. Use Passage.user.update() instead.")
    def updateUser(  # noqa: N802
        self,
        user_id: str,
        attributes: UpdateUserRequest,
    ) -> UserInfo | PassageError:
        """Update Passage User."""
        return self.user.update(user_id, attributes)

    @typing_extensions.deprecated("Passage.deleteUser() will be deprecated. Use Passage.user.delete() instead.")
    def deleteUser(self, user_id: str) -> bool | PassageError:  # noqa: N802
        """Delete Passage User."""
        self.user.delete(user_id)
        return True

    @typing_extensions.deprecated("Passage.createUser() will be deprecated. Use Passage.user.create() instead.")
    def createUser(  # noqa: N802
        self,
        userAttributes: CreateUserRequest,  # noqa: N803
    ) -> UserInfo | PassageError:
        """Create Passage User."""
        if not ("phone" in userAttributes or "email" in userAttributes):  # type: ignore[dict-item]
            msg = "either phone or email must be provided to create the user"
            raise PassageError(msg)

        return self.user.create(userAttributes)
