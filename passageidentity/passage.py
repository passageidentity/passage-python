"""Provides the Passage class for interacting with the Passage API."""

from __future__ import annotations

import json
import warnings
from http import HTTPStatus
from typing import TYPE_CHECKING

import jwt
import jwt.algorithms

from passageidentity import requests
from passageidentity.errors import PassageError
from passageidentity.helper import fetch_app, get_auth_token_from_request

from .openapi_client.api import (
    AppsApi,
    MagicLinksApi,
    TokensApi,
    UserDevicesApi,
    UsersApi,
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

AUTH_CACHE = {}
BASE_URL = "https://api.passage.id/v1/apps/"


class Passage:
    """Passage class for interacting with the Passage API."""

    COOKIE_AUTH = 1
    HEADER_AUTH = 2


    def __init__(self, app_id: str, api_key: str = "", auth_strategy: int = COOKIE_AUTH) -> None:
        """When a Passage object is created, fetch the public key from the cache or make an API request to get it."""
        self.app_id: str = app_id
        self.passage_apikey: str = api_key
        self.auth_strategy: int = auth_strategy
        self.request_headers = {"Authorization": "Bearer " + self.passage_apikey}

        if not app_id:
            msg = "Passage App ID must be provided"
            raise PassageError(msg)

        # if the pubkey exists in the cache, use that to avoid making requests
        if app_id in AUTH_CACHE:
            self.jwks: dict[str,list] = AUTH_CACHE[app_id]["jwks"]
            self.auth_origin: str = AUTH_CACHE[app_id]["auth_origin"]
        else:
            self.__refresh_auth_cache()


    def __fetch_jwks(self) -> dict[str,list]:
        """Fetch JWKs for the app."""
        r = requests.get(
            f"https://auth.passage.id/v1/apps/{self.app_id}/.well-known/jwks.json",
        )

        if r.status_code != HTTPStatus.OK:
            raise PassageError(
                "Could not fetch JWKs for app id " + self.app_id,
                r.status_code,
                r.reason,
                r.json(),
            )

        jwks = r.json()["keys"]

        # translate the JWKS into map for O(1) access
        jwk_items = {}
        for jwk in jwks:
            jwk_items[jwk["kid"]] = jwk

        return jwk_items


    def __fetch_hosted(self) -> bool:
        """Fetch whether the app is hosted."""
        r = requests.get(
            f"https://api.passage.id/v1/apps/{self.app_id}", api_key=self.passage_apikey,
        )

        if r.status_code != HTTPStatus.OK:
            raise PassageError(
                "Could not fetch app info for app id " + self.app_id,
                r.status_code,
                r.reason,
                r.json(),
            )

        return r.json()["app"]["hosted"]



    def validateJwt(self, token: str):  # noqa: ANN201, N802
        """Verify the JWT and return the user ID for the authenticated user, or throw a PassageError.

        Takes the place of the deprecated authenticateRequest() function.
        """
        return self.authenticateJWT(token)


    def __refresh_auth_cache(self) -> None:
        self.auth_origin = fetch_app(self.app_id)["auth_origin"]
        self.jwks = self.__fetch_jwks()
        hosted = self.__fetch_hosted()

        AUTH_CACHE[self.app_id] = {
            "jwks": self.jwks,
            "auth_origin": self.auth_origin,
            "hosted": hosted,
        }


    def authenticateRequest(self, request: Request) -> str | PassageError:  # noqa: N802
        """Authenticate a Flask or Django request that uses Passage for authentication.

        This function will verify the JWT and return the user ID for the authenticated user, or throw
        a PassageError.
        """
        warnings.warn(
            "Passage.authenticateRequest() is deprecated. Use Passage.authenticateJWT() instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        # check for authorization header
        token = get_auth_token_from_request(request, self.auth_strategy)
        if not token:
            msg = "Could not find JWT."
            raise PassageError(msg)

        # load and parse the JWT
        try:
            return self.authenticateJWT(token)
        except Exception as e:
            msg = f"JWT is not valid: {e}"
            raise PassageError(msg) from e


    def authenticateJWT(self, token: str) -> str | PassageError:  # noqa: N802
        """Authenticate a JWT from Passage.

        This function will verify the JWT and return the user ID for the authenticated user, or throw a PassageError.
        This function can be used to authenticate JWTs from Passage if they are not sent in a typical cookie or
        authorization header.
        """
        # load and parse the JWT

        try:
            hosted = AUTH_CACHE[self.app_id]["hosted"]
            kid = jwt.get_unverified_header(token)["kid"]
            jwk = AUTH_CACHE[self.app_id]["jwks"][kid]

            # if the JWK can't be found, they might need to udpate the JWKS for this Passage intance
            # re-fetch the JWKS and try again
            if not jwk:
                _ = self.__refresh_auth_cache
                hosted = AUTH_CACHE[self.app_id]["hosted"]
                kid = jwt.get_unverified_header(token)["kid"]
                jwk = AUTH_CACHE[self.app_id]["jwks"][kid]

            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
            claims = jwt.decode(
                token,
                public_key, # type: ignore[arg-type]
                audience=[self.app_id] if hosted else self.auth_origin,
                algorithms=["RS256"],
            )
            return claims["sub"]
        except Exception as e:
            msg = f"JWT is not valid: {e}"
            raise PassageError(msg) from e


    def createMagicLink(  # noqa: N802
        self, magicLinkAttributes: CreateMagicLinkRequest,  # noqa: N803
    ) -> MagicLinkType | PassageError:
        """Create Passage MagicLink."""
        # if no api key, fail
        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        magic_link_req = {}

        magic_link_req["user_id"] = magicLinkAttributes.get("user_id") or "" # type: ignore  # noqa: PGH003
        magic_link_req["email"] = magicLinkAttributes.get("email") or "" # type: ignore  # noqa: PGH003
        magic_link_req["phone"] = magicLinkAttributes.get("phone") or "" # type: ignore  # noqa: PGH003

        magic_link_req["language"] = magicLinkAttributes.get("language") or "" # type: ignore  # noqa: PGH003
        magic_link_req["magic_link_path"] = (
            magicLinkAttributes.get("magic_link_path") or "" # type: ignore  # noqa: PGH003
        )
        magic_link_req["redirect_url"] = magicLinkAttributes.get("redirect_url") or "" # type: ignore  # noqa: PGH003
        magic_link_req["send"] = magicLinkAttributes.get("send") or False # type: ignore  # noqa: PGH003
        magic_link_req["ttl"] = magicLinkAttributes.get("ttl") or 0 # type: ignore  # noqa: PGH003
        magic_link_req["type"] = magicLinkAttributes.get("type") or "login" # type: ignore  # noqa: PGH003

        if magicLinkAttributes.get("email"): # type: ignore  # noqa: PGH003
            magic_link_req["channel"] = magicLinkAttributes.get("channel") or "email" # type: ignore  # noqa: PGH003
        elif magicLinkAttributes.get("phone"): # type: ignore  # noqa: PGH003
            magic_link_req["channel"] = magicLinkAttributes.get("channel") or "phone" # type: ignore  # noqa: PGH003

        try:
            client = MagicLinksApi()
            return client.create_magic_link(
                self.app_id, magic_link_req, _headers=self.request_headers, # type: ignore[arg-type]
            ).magic_link # type: ignore[attr-defined]
        except Exception as e:
            msg = f"Failed to create magic link: {e}"
            raise PassageError(msg) from e


    def getApp(self) -> AppInfo | PassageError:  # noqa: N802
        """Use Passage API to get info for their app."""
        client = AppsApi()
        return client.get_app(self.app_id).app


    def getUser(self, user_id: str) -> UserInfo | PassageError:  # noqa: N802
        """Use Passage API to get info for a user, look up by user ID."""
        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        try:
            client = UsersApi()
            return client.get_user(
                self.app_id, user_id, _headers=self.request_headers,
            ).user
        except Exception as e:
            msg = f"Failed to fetch user data: {e}"
            raise PassageError(msg) from e


    def getUserByIdentifier(self, userIdentifier: str) -> UserInfo | PassageError:  # noqa: N802, N803
        """Use Passage API to get info for a user, look up by user identifier."""
        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        try:
            client = UsersApi()
            users = client.list_paginated_users(
                self.app_id,
                limit=1,
                identifier=userIdentifier.lower(),
                _headers=self.request_headers,
            ).users
        except Exception as e:
            msg = f"Failed to fetch user data: {e}"
            raise PassageError(msg) from e

        if len(users) == 0:
            msg = "Failed to find user data"
            raise PassageError(msg)

        return self.getUser(users[0].id)


    def listUserDevices(  # noqa: N802
        self, user_id: str,
    ) -> list[WebAuthnDevices] | PassageError:
        """Use Passage API to list user devices, look up by user ID."""
        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        try:
            client = UserDevicesApi()
            return client.list_user_devices(
                self.app_id, user_id, _headers=self.request_headers,
            ).devices
        except Exception as e:
            msg = f"Failed to list user's devices: {e}"
            raise PassageError(msg) from e


    def deleteUserDevice(  # noqa: N802
        self, user_id: str, device_id: str,
    ) -> bool | PassageError:
        """Use Passage API to revoke user devices, look up by user ID."""
        return self.revokeUserDevice(user_id, device_id)


    def revokeUserDevice(  # noqa: N802
        self, user_id: str, device_id: str,
    ) -> bool | PassageError:
        """Use Passage API to revoke user devices, look up by user ID."""
        warnings.warn(
            "Passage.revokeUserDevice() is deprecated. Use Passage.deleteUserDevice() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        try:
            client = UserDevicesApi()
            client.delete_user_devices(
                self.app_id, user_id, device_id, _headers=self.request_headers,
            )
            return True  # noqa: TRY300
        except Exception as e:
            msg = f"Failed to revoke user device: {e}"
            raise PassageError(msg) from e


    def revokeUserRefreshTokens(self, user_id: str) -> bool | PassageError:  # noqa: N802
        """Use Passage API to revoke all of a user's refresh tokens, look up by user ID."""
        return self.signOut(user_id)


    def signOut(  # noqa: N802
        self,
        user_id: str,
    ) -> bool | PassageError:
        """Use Passage API to revoke all of a user's refresh tokens, look up by user ID."""
        warnings.warn(
            "Passage.signOut() is deprecated. Use Passage.revokeUserRefreshTokens() instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        try:
            client = TokensApi()
            client.revoke_user_refresh_tokens(
                self.app_id, user_id, _headers=self.request_headers,
            )
            return True  # noqa: TRY300
        except Exception as e:
            msg = f"Failed to revoke user's refresh tokens: {e}"
            raise PassageError(msg) from e


    def activateUser(self, user_id: str) -> UserInfo | PassageError:  # noqa: N802
        """Activate Passage User."""
        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        try:
            client = UsersApi()
            return client.activate_user(
                self.app_id, user_id, _headers=self.request_headers,
            ).user
        except Exception as e:
            msg = f"Failed activate user: {e}"
            raise PassageError(msg) from e


    def deactivateUser(self, user_id: str) -> UserInfo | PassageError:  # noqa: N802
        """Deactivate Passage User."""
        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        try:
            client = UsersApi()
            return client.deactivate_user(
                self.app_id, user_id, _headers=self.request_headers,
            ).user
        except Exception as e:
            msg = f"Failed deactivate user: {e}"
            raise PassageError(msg) from e

    def updateUser(  # noqa: N802
        self, user_id: str, attributes: UpdateUserRequest,
    ) -> UserInfo | PassageError:
        """Update Passage User."""
        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        try:
            client = UsersApi()
            return client.update_user(
                self.app_id, user_id, attributes, _headers=self.request_headers,
            ).user
        except Exception as e:
            msg = f"Failed to update user attributes: {e}"
            raise PassageError(msg) from e


    def deleteUser(self, user_id: str) -> bool | PassageError:  # noqa: N802
        """Delete Passage User."""
        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        try:
            client = UsersApi()
            client.delete_user(self.app_id, user_id, _headers=self.request_headers)
            return True  # noqa: TRY300
        except Exception as e:
            msg = f"Failed to  delete user: {e}"
            raise PassageError(msg) from e


    def createUser(  # noqa: N802
        self, userAttributes: CreateUserRequest,  # noqa: N803
    ) -> UserInfo | PassageError:
        """Create Passage User."""
        if not ("phone" in userAttributes or "email" in userAttributes): # type: ignore[dict-item]
            msg = "either phone or email must be provided to create the user"
            raise PassageError(msg)

        # if no api key, fail
        if self.passage_apikey == "":
            msg = "No Passage API key provided."
            raise PassageError(msg)

        try:
            client = UsersApi()
            return client.create_user(
                self.app_id, userAttributes, _headers=self.request_headers,
            ).user
        except Exception as e:
            msg = f"Failed to create user: {e}"
            raise PassageError(msg) from e
