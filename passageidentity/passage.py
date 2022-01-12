import jwt, json, requests
from datetime import datetime

import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict, Union
else:
    from typing_extensions import TypeDict, Union

from requests.sessions import Request
from passageidentity.helper import extractToken, getAuthTokenFromRequest, fetchPublicKey
from passageidentity.errors import PassageError

PUBKEY_CACHE = {}

class Passage():
    COOKIE_AUTH = 1
    HEADER_AUTH = 2

    class PassageUserType(TypedDict):
        created_at: str
        updated_at: str
        active: bool
        email_verified: bool
        email: str
        phone: str
        id: str
        last_login_at: str
        login_count: int
        recent_events: Union[None, list]
        webauthn: bool
        webauthn_devices: Union[None, list]

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
        if app_id in PUBKEY_CACHE.keys():
            self.passage_pubkey: str = PUBKEY_CACHE[app_id]
        else:
            self.passage_pubkey: str = fetchPublicKey(app_id)
            PUBKEY_CACHE[app_id] = self.passage_pubkey
    

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
            claims = jwt.decode(token, self.passage_pubkey, algorithms=["RS256"])
            return claims["sub"]
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
            claims = jwt.decode(token, self.passage_pubkey, algorithms=["RS256"])
            return claims["sub"]
        except Exception as e:
            raise PassageError("JWT is not valid: " + str(e)) 

    """
    Use Passage API to get info for a user, look up by user ID
    """ 
    def getUser(self, user_id: str) -> Union[PassageUserType, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = "https://api.passage.id/v1/apps/" + self.app_id + "/users/" + user_id
            r = requests.get(url, headers=header)

            if r.status_code != 200:
                # get error message
                message = r.json()["status"]
                raise PassageError("Failed request to get user data: " + message)
            return PassageUser(user_id, r.json()["user"])
        except Exception as e:
            raise PassageError("Could not fetch user data")


    """
    Activate Passage User
    """
    def activateUser(self, user_id: str) -> Union[PassageUserType, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = "https://api.passage.id/v1/apps/" + self.app_id + "/users/" + user_id + "/activate"  
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
            url = "https://api.passage.id/v1/apps/" + self.app_id + "/users/" + user_id + "/deactivate"  
            r = requests.patch(url, headers=header)

            if r.status_code != 200:
                # get error message
                message = r.json()["status"]
                raise PassageError("Failed request to deactivate user: " + message)
            return PassageUser(user_id, r.json()["user"])
        except Exception as e:
            raise PassageError("Could not deactivate user")


    """
    Update Passage User's Attributes
    """
    class UpdateUserAttributes(TypedDict):
        phone: str
        email: str

    def updateUser(self, user_id: str, attributes: UpdateUserAttributes) -> Union[PassageUserType, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")
        
        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = "https://api.passage.id/v1/apps/" + self.app_id + "/users/" + user_id  
            r = requests.patch(url, headers=header, data=json.dumps(attributes))
            if r.status_code != 200:
                # get error message
                attributeKeys = ", ".join(attribute for attribute in attributes.keys())
                message = r.json()["status"]
                raise PassageError(f"Failed request to update user attributes ({attributeKeys}): {message}")
            return PassageUser(user_id, r.json()["user"])
        except Exception:
            raise PassageError(f"Could not update user attributes")


    """
    Delete Passage User
    """
    def deleteUser(self, user_id: str) -> Union[bool, PassageError]:
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = "https://api.passage.id/v1/apps/" + self.app_id + "/users/" + user_id  
            r = requests.delete(url, headers=header)

            if r.status_code != 200:
                # get error message
                message = r.json()["status"]
                raise PassageError("Failed request to delete user: " + message)
            
            return True
        except Exception as e:
            raise PassageError("Could not delete user")


    class UpdateUserAttributes(TypedDict, total=False):
        email: str
        phone: str

    """
    Create Passage User
    """
    def createUser(self, userAttributes: UpdateUserAttributes) -> Union[PassageUserType, PassageError]:
        if not ("phone" in userAttributes or "email" in userAttributes):
            raise PassageError("either phone or email must be provided to create the user")

        # if no api key, fail
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = "https://api.passage.id/v1/apps/" + self.app_id + "/users"  
            r = requests.post(url, data=json.dumps(userAttributes), headers=header)
            if r.status_code != 201:
                # get error message
                message = r.json()["status"]
                raise PassageError("Failed request to create user: " + message)

            parsedResponse = r.json()["user"]
            return PassageUser(parsedResponse["id"], parsedResponse)
        except Exception as e:
            raise PassageError("Could not create user")


class PassageUser:
    def __init__(self, user_id, fields={}):
        self.id = user_id
        self.email = fields["email"]
        self.phone = fields["phone"]
        self.active = fields["active"]
        self.email_verified = fields["email_verified"]
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