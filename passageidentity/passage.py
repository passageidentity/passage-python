import jwt, json, requests
from datetime import datetime

import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict, Union
else:
    from typing_extensions import TypedDict
    from typing import Union

from requests.sessions import Request
from passageidentity.helper import fetchApp, getAuthTokenFromRequest
from passageidentity.errors import PassageError
from enum import Enum

AUTH_CACHE = {}
BASE_URL = "https://api.passage.id/v1/apps/"

class UserStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"

class ChannelType(Enum):
    EMAIL = "email"
    PHONE = "phone"

class Passage():
    COOKIE_AUTH = 1
    HEADER_AUTH = 2

    class PassageMagicLinkType(TypedDict, total=False):
        id: str
        secret: str
        activated: bool
        user_id: str
        app_id: str
        identifier: str
        type: str
        redirect_url: str
        url: str
        ttl: int

    class PassageAppType(TypedDict):
        name: str
        id: str
        auth_origin: str
        redirect_url: str
        login_url: str
        rsa_public_key: str
        allowed_identifier: str
        require_identifier_verification: bool
        session_timeout_length: int
        refresh_enabled: bool
        refresh_absolute_lifetime: int
        refresh_inactivity_lifetime: int
        user_metadata_schema: list
        layouts: list

    class PassageUserType(TypedDict):
        created_at: str
        updated_at: str
        status: UserStatus
        email_verified: bool
        phone_verified: bool
        email: str
        phone: str
        id: str
        last_login_at: str
        login_count: int
        recent_events: Union[None, list]
        webauthn: bool
        webauthn_devices: Union[None, list]
        user_metadata: dict
    class PassageDeviceType(TypedDict):
        created_at: str
        updated_at: str
        last_login_at: str
        id: str
        cred_id: str
        friendly_name: str
        usage_count: int



    """
    When a Passage object is created, fetch the public key from the cache or make an API request to get it
    """
    def __init__(self, app_id, api_key="", auth_strategy=COOKIE_AUTH):
        self.app_id: str = app_id
        self.passage_apikey: str = api_key
        self.auth_strategy: str = auth_strategy

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
            raise PassageError("Could not fetch JWKs for app id " + self.app_id)

        jwks = r.json()["keys"]

        # translate the JWKS into map for O(1) access
        jwkItems = {}
        for jwk in jwks:
            jwkItems[jwk["kid"]] = jwk

        return jwkItems

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
        # check for authorization header
        token = getAuthTokenFromRequest(request, self.auth_strategy)
        if not token:
            raise PassageError("Could not find JWT.")

        # load and parse the JWT
        try:
            userID = self.authenticateJWT(token)
            return userID
        except Exception as e:
            raise PassageError("JWT is not valid: " + str(e))

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
            raise PassageError("JWT is not valid: " + str(e))


    class MagicLinkAttributes(TypedDict, total=False):
        user_id: str
        email: str
        phone: str
        channel: ChannelType
        send: bool
        magic_link_path: str
        redirect_url: str
        ttl: int

    """
    Create Passage MagicLink
    """
    def createMagicLink(self, magicLinkAttributes: MagicLinkAttributes) -> Union[PassageMagicLinkType, PassageError]:
        # if no api key, fail
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = BASE_URL + self.app_id + "/magic-links"
            r = requests.post(url, data=json.dumps(magicLinkAttributes), headers=header)
            if r.status_code != 201:
                # get error message
                message = r.json()["status"]
                raise PassageError("Failed request to create magic link: " + message)

            parsedResponse = r.json()["magic_link"]
            return PassageMagicLink(parsedResponse["id"], parsedResponse)
        except Exception as e:
            raise PassageError("Could not create magic link")

    """
    Use Passage API to get info for their app.
    """

    def getApp(self) -> Union[PassageAppType, PassageError]:
        app_info = fetchApp(self.app_id)
        return PassageApp(app_info)


    """
    Use Passage API to get info for a user, look up by user ID
    """
    def getUser(self, user_id: str) -> Union[PassageUserType, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = BASE_URL + self.app_id + "/users/" + user_id
            r = requests.get(url, headers=header)

            if r.status_code != 200:
                # get error message
                message = r.json()["status"]
                raise PassageError("Failed request to get user data: " + message)
            return PassageUser(user_id, r.json()["user"])
        except Exception as e:
            raise PassageError("Could not fetch user data")

    """
    Use Passage API to list user devices, look up by user ID
    """
    def listUserDevices(self, user_id: str) -> Union[list, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = BASE_URL + self.app_id + "/users/" + user_id + "/devices"
            r = requests.get(url, headers=header)

            if r.status_code != 200:
                # get error message
                message = r.json()["status"]
                raise PassageError(f"{message}")
            device_list = list()
            devices = r.json()["devices"]
            if devices != None:
                for d in devices:
                    device_list.append(PassageDevice(d))
            return device_list
        except Exception as e:
            raise PassageError("Could not list user's devices: {e}")

    """
    Use Passage API to list user devices, look up by user ID
    """
    def revokeUserDevice(self, user_id: str, device_id: str) -> Union[bool, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = BASE_URL + self.app_id + "/users/" + user_id + "/devices/" + device_id
            r = requests.delete(url, headers=header)

            if r.status_code != 200:
                # get error message
                message = r.json()["status"]
                raise PassageError(f"{message}")
            return True
        except Exception as e:
            raise PassageError("Could not revoke user device: {e}")

    """
    Use Passage API to revoke all of a user's refresh tokens, look up by user ID
    """
    def signOut(self, user_id: str, ) -> Union[bool, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = BASE_URL + self.app_id + "/users/" + user_id + "/tokens/"
            r = requests.delete(url, headers=header)

            if r.status_code != 200:
                # get error message
                message = r.json()["status"]
                raise PassageError(f"{message}")
            return True
        except Exception as e:
            raise PassageError("Could not revoke user's refresh tokens: {e}")

    """
    Activate Passage User
    """
    def activateUser(self, user_id: str) -> Union[PassageUserType, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = BASE_URL + self.app_id + "/users/" + user_id + "/activate"
            r = requests.patch(url, headers=header)

            if r.status_code != 200:
                # get error message
                message = r.json()["status"]
                raise PassageError("Failed request to activate user: " + message)
            return PassageUser(user_id, r.json()["user"] )
        except Exception as e:
            raise PassageError("Could not activate user")


    """
    Deactivate Passage User
    """
    def deactivateUser(self, user_id: str) -> Union[PassageUserType, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = BASE_URL + self.app_id + "/users/" + user_id + "/deactivate"
            r = requests.patch(url, headers=header)

            if r.status_code != 200:
                # get error message
                message = r.json()["error"]
                raise PassageError(f"{message}")
            return PassageUser(user_id, r.json()["user"])
        except Exception as e:
            raise PassageError("Could not deactivate user: {e}")


    """
    Update Passage User's Attributes
    """
    class UserAttributes(TypedDict, total=False):
        email: str
        phone: str
        user_updates: dict

    def updateUser(self, user_id: str, attributes: UserAttributes) -> Union[PassageUserType, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = BASE_URL + self.app_id + "/users/" + user_id
            r = requests.patch(url, headers=header, data=json.dumps(attributes))
            if r.status_code != 200:
                # get error message
                attributeKeys = ", ".join(attribute for attribute in attributes.keys())
                message = r.json()["error"]
                raise PassageError(f"{message}")
            return PassageUser(user_id, r.json()["user"])
        except Exception as e:
            raise PassageError(f"Could not update user attributes: {e}")


    """
    Delete Passage User
    """
    def deleteUser(self, user_id: str) -> Union[bool, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = BASE_URL + self.app_id + "/users/" + user_id
            r = requests.delete(url, headers=header)

            if r.status_code != 200:
                # get error message
                message = r.json()["status"]
                raise PassageError("Failed request to delete user: " + message)

            return True
        except Exception as e:
            raise PassageError("Could not delete user")


    """
    Create Passage User
    """
    def createUser(self, userAttributes: UserAttributes) -> Union[PassageUserType, PassageError]:
        if not ("phone" in userAttributes or "email" in userAttributes):
            raise PassageError("either phone or email must be provided to create the user")

        # if no api key, fail
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = BASE_URL + self.app_id + "/users"
            r = requests.post(url, data=json.dumps(userAttributes), headers=header)
            if r.status_code != 201:
                # get error message
                message = r.json()["status"]
                raise PassageError("Failed request to create user: " + message)

            parsedResponse = r.json()["user"]
            return PassageUser(parsedResponse["id"], parsedResponse)
        except Exception as e:
            raise PassageError("Could not create user")

class PassageApp:
    def __init__(self, fields={}):
        self.name = fields["name"]
        self.id = fields["id"]
        self.auth_origin = fields["auth_origin"]
        self.redirect_url = fields["redirect_url"]
        self.login_url = fields["login_url"]
        self.rsa_public_key = fields["rsa_public_key"]
        self.allowed_identifier = fields["allowed_identifier"]
        self.require_identifier_verification = fields["require_identifier_verification"]
        self.session_timeout_length = fields["session_timeout_length"]
        self.refresh_enabled = fields["refresh_enabled"]
        self.refresh_absolute_lifetime = fields["refresh_absolute_lifetime"]
        self.refresh_inactivity_lifetime = fields["refresh_inactivity_lifetime"]
        self.user_metadata_schema = fields["user_metadata_schema"]
        self.layouts = fields["layouts"]
class PassageDevice:
    def __init__(self, fields={}):
        self.id = fields["id"]
        try:
            self.created_at = datetime.strptime(time_to_milliseconds(fields["created_at"]),"%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            self.created_at = datetime.strptime(fields["created_at"],"%Y-%m-%dT%H:%M:%SZ")
        try:
            self.updated_at = datetime.strptime(time_to_milliseconds(fields["updated_at"]),"%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            self.updated_at = datetime.strptime(fields["updated_at"],"%Y-%m-%dT%H:%M:%SZ")
        try:
            self.last_login_at = datetime.strptime(time_to_milliseconds(fields["last_login_at"]),"%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            self.last_login_at = datetime.strptime(fields["last_login_at"],"%Y-%m-%dT%H:%M:%SZ")
        self.friendly_name = fields["friendly_name"]
        self.usage_count = fields["usage_count"]

class PassageMagicLink:
    def __init__(self, magic_link_id, fields={}):
        self.id = magic_link_id
        self.secret = fields["secret"]
        self.activated = fields["activated"]
        self.user_id = fields["user_id"]
        self.app_id = fields["app_id"]
        self.identifier = fields["identifier"]
        self.type = fields["type"]
        self.redirect_url = fields["redirect_url"]
        self.url = fields["url"]
        self.ttl = fields["ttl"]

class PassageUser:
    def __init__(self, user_id, fields={}):
        self.id = user_id
        self.email = fields["email"]
        self.phone = fields["phone"]
        self.status = fields["status"]
        self.email_verified = fields["email_verified"]
        self.phone_verified = fields["phone_verified"]
        self.user_metadata = fields["user_metadata"]
        try:
            self.created_at = datetime.strptime(time_to_milliseconds(fields["created_at"]),"%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            self.created_at = datetime.strptime(fields["created_at"],"%Y-%m-%dT%H:%M:%SZ")
        try:
            self.last_login_at = datetime.strptime(time_to_milliseconds(fields["last_login_at"]),"%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            self.last_login_at = datetime.strptime(fields["last_login_at"],"%Y-%m-%dT%H:%M:%SZ")

        self.webauthn = fields["webauthn"]
        self.webauthn_devices = fields["webauthn_devices"]
        if fields["recent_events"] != None:
            events = fields["recent_events"]
            self.recent_events = []
            for e in events:
                pe = PassageEvent(e)
                self.recent_events.append(pe)


class PassageEvent:
    def __init__(self, event):
        self.event_type = event["type"]
        self.id = event["id"]

        try:
            self.timestamp = datetime.strptime(time_to_milliseconds(event["created_at"]),"%Y-%m-%dT%H:%M:%S.%fZ")
        except:
             self.timestamp = datetime.strptime(event["created_at"],"%Y-%m-%dT%H:%M:%SZ")


def time_to_milliseconds(timeString: str) -> str:
	# see if decimal exists; if not, return
	time = timeString.split(".")
	if len(time) < 2:
		return timeString

	# grab the digits; if milliseconds (6 digits) return
	decimalNumbers = time[1][:-1]
	if len(decimalNumbers) == 6:
		return timeString

	# ensure 6 decimal places, add back '.' and 'Z' to string
	return time[0] + "." + decimalNumbers[:6] + "Z"
