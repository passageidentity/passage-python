
import jwt
import requests
from datetime import datetime
from enum import Enum
from passageidentity.helper import extractToken, getAuthTokenFromRequest, fetchPublicKey
from passageidentity.errors import PassageError

PUBKEY_CACHE = {}

class Passage():
    COOKIE_AUTH = 1
    HEADER_AUTH = 2

    """
    When a Passage object is created, fetch the public key from the cache or make an API request to get it
    """
    def __init__(self, app_id, api_key="", auth_strategy=COOKIE_AUTH):
        self.app_id = app_id
        self.passage_apikey = api_key
        self.auth_strategy = auth_strategy

        # if the pubkey exists in the cache, use that to avoid making requests
        if app_id in PUBKEY_CACHE.keys():
            self.passage_pubkey = PUBKEY_CACHE[app_id]
        else:
            self.passage_pubkey = fetchPublicKey(app_id)
            PUBKEY_CACHE[app_id] = self.passage_pubkey
    
    """
    Authenticate a Flask request that uses Passage for authentication.
    This function will verify the JWT and return the user ID for the authenticated user, or throw
    a PassageError
    """ 
    def authenticateRequest(self, request):
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
    Use Passage API to get info for a user, look up by user ID
    """ 
    def getUser(self, user_id):
        # if no api key, fail
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
    Get instance of Passage User
    """
    def getUserOld(self, user_id):
        return Passage.PassageUser(self, user_id)

    """
    Deactivate Passage User
    """

    def activateUser(self, user_id):
        # if no api key, fail
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

    def deactivateUser(self, user_id):
        # if no api key, fail
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

class PassageUser:

    def __init__(self, user_id, fields={}):
        self.id = user_id
        self.email = fields["email"]
        self.active = fields["active"]
        self.email_verified = fields["email_verified"]

        try:
            self.created_at = datetime.strptime(fields["created_at"],"%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            self.created_at = datetime.strptime(fields["created_at"],"%Y-%m-%dT%H:%M:%SZ")

        try:
            self.last_login_at = datetime.strptime(fields["last_login_at"],"%Y-%m-%dT%H:%M:%S.%fZ")
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
            self.timestamp = datetime.strptime(event["created_at"],"%Y-%m-%dT%H:%M:%S.%fZ")
        except:
             self.timestamp = datetime.strptime(event["created_at"],"%Y-%m-%dT%H:%M:%SZ")
           