
import jwt
import requests
from passageidentity.helper import extractToken, getAuthTokenFromRequest, fetchPublicKey
from passageidentity.errors import PassageError

PUBKEY_CACHE = {}

class Passage:

    """
    When a Passage object is created, attempt to load the public key from the environment variable.
    This is currently required.
    """
    def __init__(self, app_handle, api_key=""):
        self.app_handle = app_handle
        self.passage_apikey = api_key

        # if the pubkey exists in the cache, use that to avoid making requests
        if app_handle in PUBKEY_CACHE.keys():
            self.passage_pubkey = PUBKEY_CACHE[app_handle]
        else:
            self.passage_pubkey = fetchPublicKey(app_handle)
            PUBKEY_CACHE[app_handle] = self.passage_pubkey
    
    """
    Authenticate a Flask request that uses Passage for authentication.
    This function will verify the JWT and return the user ID for the authenticated user, or throw
    a PassageError
    """ 
    def authenticateRequest(self, request):
        # check for authorization header
        token = getAuthTokenFromRequest(request)
        if not token:
            raise PassageError("Could not find JWT.")

        # load and parse the JWT
        try:
            claims = jwt.decode(token, self.passage_pubkey, algorithms=["RS256"])
            return claims["sub"]
        except Exception as e:
            raise PassageError("JWT is not valid: " + str(e))

    """
    Use Passage API to get info for a user, look up by user handle
    """ 
    def getUserInfo(self, user_handle):
        # if no api key, fail
        if self.passage_apikey == "":
            raise PassageError("No Passage API key provided.")

        header = {"Authorization": "Bearer " + self.passage_apikey}
        try:
            url = "https://api.passage.id/v1/app/" + self.app_handle + "/users/" + user_handle
            r = requests.get(url, headers=header)

            if r.status_code != 200:
                # get error message
                message = r.json()["message"]
                raise PassageError("Failed request to get user data: " + message)
            return r.json()
        except Exception as e:
            raise PassageError("Could not fetch user data")


    """
    Get instance of Passage User
    """
    def getPassageUser(self, user_handle):
        return Passage.PassageUser(self, user_handle)

    """
    Inner class represesnting a Passage User. 
    """
    class PassageUser:

        def __init__(self, psg, user_handle):
            self.psg = psg
            self.handle = user_handle

            data = self.psg.getUserInfo(self.handle)
            # set the individual fields 
            self.email = data["email"]
            self.active = data["active"]
            self.email_verified = data["email_verified"]
            self.start_date = data["start_date"]
            self.last_login_date = data["last_login_date"]
            self.password = data["password"]
            self.webauthn = data["webauthn"]
            self.webauthn_devices = data["webauthn_devices"]
            self.recent_events = data["recent_events"]




