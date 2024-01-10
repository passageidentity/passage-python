import jwt, json, warnings
from datetime import datetime

import sys

if sys.version_info >= (3, 8):
    from typing import List, Union
else:
    from typing_extensions import TypedDict
    from typing import List
    from typing import Union

from requests.sessions import Request
from passageidentity import requests
from passageidentity.helper import fetchApp, getAuthTokenFromRequest
from passageidentity.errors import PassageError

from .openapi_client.api import AppsApi, MagicLinksApi, TokensApi, UsersApi, UserDevicesApi
from .openapi_client.models import AppInfo, CreateMagicLinkRequest, CreateUserRequest, MagicLinkType, UpdateUserRequest, UserInfo, WebAuthnDevices

AUTH_CACHE = {}
BASE_URL = "https://api.passage.id/v1/apps/"

class Passage():
    COOKIE_AUTH = 1
    HEADER_AUTH = 2

    """
    When a Passage object is created, fetch the public key from the cache or make an API request to get it
    """
    def __init__(self, app_id, api_key="", auth_strategy=COOKIE_AUTH):
        self.app_id: str = app_id
        self.passage_apikey: str = api_key
        self.auth_strategy: str = auth_strategy
        self.request_headers = {"Authorization": "Bearer " + self.passage_apikey}

        if not app_id:
            raise PassageError("Passage App ID must be provided")

        # if the pubkey exists in the cache, use that to avoid making requests
        if app_id in AUTH_CACHE.keys():
            self.jwks: str = AUTH_CACHE[app_id]["jwks"]
            self.auth_origin: str = AUTH_CACHE[app_id]["auth_origin"]
        else:
            self.__refreshAuthCache()


    """
    Fetch JWKs for the app
    """
    def __fetchJWKS(self):
        r = requests.get(f"https://auth.passage.id/v1/apps/{self.app_id}/.well-known/jwks.json")

        if r.status_code != 200:
            raise PassageError("Could not fetch JWKs for app id " + self.app_id, r.status_code, r.reason, r.json())

        jwks = r.json()["keys"]

        # translate the JWKS into map for O(1) access
        jwkItems = {}
        for jwk in jwks:
            jwkItems[jwk["kid"]] = jwk

        return jwkItems

    """
    This function will verify the JWT and return the user ID for the authenticated user, or throw
    a PassageError. Takes the place of the deprecated authenticateRequest() function.
    """
    def validateJwt(self, token):
        return self.authenticateJWT(token)

    def __refreshAuthCache(self):
        self.auth_origin = fetchApp(self.app_id)["auth_origin"]
        self.jwks = self.__fetchJWKS()
        AUTH_CACHE[self.app_id] = {"jwks": self.jwks, "auth_origin": self.auth_origin}

    """
    Authenticate a Flask or Django request that uses Passage for authentication.
    This function will verify the JWT and return the user ID for the authenticated user, or throw
    a PassageError
    """
    def authenticateRequest(self, request: Request) -> Union[str, PassageError]:
        warnings.warn("Passage.authenticateRequest() is deprecated. Use Passage.authenticateJWT() instead.", DeprecationWarning)

        # check for authorization header
        token = getAuthTokenFromRequest(request, self.auth_strategy)
        if not token:
            raise PassageError("Could not find JWT.")

        # load and parse the JWT
        try:
            userID = self.authenticateJWT(token)
            return userID
        except Exception as e:
            raise PassageError(f"JWT is not valid: {e}")

    """
    Authenticate a JWT from Passage. This function will verify the JWT and return the user ID
    for the authenticated user, or throw a PassageError.
    This function can be used to authenticate JWTs from Passage if they are not sent in a typical cookie or
    authorization header.
    """
    def authenticateJWT(self, token:str) -> Union[str, PassageError]:
        # load and parse the JWT
        try:
            kid = jwt.get_unverified_header(token)["kid"]
            jwk = AUTH_CACHE[self.app_id]["jwks"][kid]

            # if the JWK can't be found, they might need to udpate the JWKS for this Passage intance
            # re-fetch the JWKS and try again
            if not jwk:
                self.__refreshAuthCache
                kid = jwt.get_unverified_header(token)["kid"]
                jwk = AUTH_CACHE[self.app_id]["jwks"][kid]

            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
            claims = jwt.decode(token, public_key, audience=self.auth_origin, algorithms=["RS256"])
            return claims["sub"]
        except Exception as e:
            raise PassageError(f"JWT is not valid: {e}")

    """
    Create Passage MagicLink
    """
    def createMagicLink(self, magicLinkAttributes: CreateMagicLinkRequest) -> Union[MagicLinkType, PassageError]:
        # if no api key, fail
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")
        
        magic_link_req = {}
        
        magic_link_req["user_id"] = magicLinkAttributes.get("user_id") or ""
        magic_link_req["email"] = magicLinkAttributes.get("email") or ""
        magic_link_req["phone"] = magicLinkAttributes.get("phone") or ""

        magic_link_req["language"] = magicLinkAttributes.get("language") or ""
        magic_link_req["magic_link_path"] = magicLinkAttributes.get("magic_link_path") or ""
        magic_link_req["redirect_url"] = magicLinkAttributes.get("redirect_url") or ""
        magic_link_req["send"] = magicLinkAttributes.get("send") or False
        magic_link_req["ttl"] = magicLinkAttributes.get("ttl") or 0
        magic_link_req["type"] = magicLinkAttributes.get("type") or "login"

        if magicLinkAttributes.get("email"):
            magic_link_req["channel"] = magicLinkAttributes.get("channel") or "email"
        elif magicLinkAttributes.get("phone"):
            magic_link_req["channel"] = magicLinkAttributes.get("channel") or "phone"

        try:
            client = MagicLinksApi()
            return client.create_magic_link(self.app_id, magic_link_req, _headers=self.request_headers).magic_link
        except Exception as e:
            raise PassageError(f"Failed to create magic link: {e}")

    """
    Use Passage API to get info for their app.
    """

    def getApp(self) -> Union[AppInfo, PassageError]:
        client = AppsApi()
        return client.get_app(self.app_id).app


    """
    Use Passage API to get info for a user, look up by user ID
    """
    def getUser(self, user_id: str) -> Union[UserInfo, PassageError]:

        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        try:
            client = UsersApi()
            return client.get_user(self.app_id, user_id, _headers=self.request_headers).user
        except Exception as e:
            raise PassageError(f"Failed to fetch user data: {e}")

    """
    Use Passage API to list user devices, look up by user ID
    """
    def listUserDevices(self, user_id: str) -> Union[List[WebAuthnDevices], PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        try:
            client = UserDevicesApi()
            return client.list_user_devices(self.app_id, user_id, _headers=self.request_headers).devices
        except Exception as e:
            raise PassageError(f"Failed to list user's devices: {e}")

    
    """
    Use Passage API to revoke user devices, look up by user ID
    """
    def deleteUserDevice(self, user_id: str, device_id: str) -> Union[bool, PassageError]:
        return self.revokeUserDevice(user_id, device_id)
    
    
    """
    Use Passage API to revoke user devices, look up by user ID
    """
    def revokeUserDevice(self, user_id: str, device_id: str) -> Union[bool, PassageError]:
        warnings.warn("Passage.revokeUserDevice() is deprecated. Use Passage.deleteUserDevice() instead.", DeprecationWarning)
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        try:
            client = UserDevicesApi()
            client.delete_user_devices(self.app_id, user_id, device_id, _headers=self.request_headers)
            return True
        except Exception as e:
            raise PassageError(f"Failed to revoke user device: {e}")
        
    """
    Use Passage API to revoke all of a user's refresh tokens, look up by user ID
    """
    def revokeUserRefreshTokens(self, user_id: str) -> Union[bool, PassageError]:
        return self.signOut(user_id)
    
    """
    Use Passage API to revoke all of a user's refresh tokens, look up by user ID
    """
    def signOut(self, user_id: str, ) -> Union[bool, PassageError]:
        warnings.warn("Passage.signOut() is deprecated. Use Passage.revokeUserRefreshTokens() instead.", DeprecationWarning)

        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        try:
            client = TokensApi()
            client.revoke_user_refresh_tokens(self.app_id, user_id, _headers=self.request_headers)
            return True
        except Exception as e:
            raise PassageError(f"Failed to revoke user's refresh tokens: {e}")

    """
    Activate Passage User
    """
    def activateUser(self, user_id: str) -> Union[UserInfo, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        try:
            client = UsersApi()
            return client.activate_user(self.app_id, user_id, _headers=self.request_headers).user
        except Exception as e:
            raise PassageError(f"Failed activate user: {e}")

    """
    Deactivate Passage User
    """
    def deactivateUser(self, user_id: str) -> Union[UserInfo, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        try:
            client = UsersApi()
            return client.deactivate_user(self.app_id, user_id, _headers=self.request_headers).user
        except Exception as e:
            raise PassageError(f"Failed deactivate user: {e}")


    def updateUser(self, user_id: str, attributes: UpdateUserRequest) -> Union[UserInfo, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        try:
            client = UsersApi()
            return client.update_user(self.app_id, user_id, attributes, _headers=self.request_headers).user
        except Exception as e:
            raise PassageError(f"Failed to update user attributes: {e}")

    """
    Delete Passage User
    """
    def deleteUser(self, user_id: str) -> Union[bool, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        try:
            client = UsersApi()
            client.delete_user(self.app_id, user_id, _headers=self.request_headers)
            return True
        except Exception as e:
            raise PassageError(f"Failed to  delete user: {e}")

    """
    Create Passage User
    """
    def createUser(self, userAttributes: CreateUserRequest) -> Union[UserInfo, PassageError]:
        if not ("phone" in userAttributes or "email" in userAttributes):
            raise PassageError("either phone or email must be provided to create the user")

        # if no api key, fail
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        try:
            client = UsersApi()
            return client.create_user(self.app_id, userAttributes, _headers=self.request_headers).user
        except Exception as e:
            raise PassageError(f"Failed to create user: {e}")
