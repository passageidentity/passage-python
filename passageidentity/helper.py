import os
import re
from base64 import b64decode
import requests

from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend

from passageidentity.errors import PassageError

TOKEN_TYPE = "Bearer"

"""
Helper function to extract the JWT from an Authorization header. 
"""
def extractToken(authHeader):
    expression = re.escape(TOKEN_TYPE) + r" ([^\s,]+)"
    match = re.search(expression, authHeader)
    try:
        return match.group(1)
    except (AttributeError, IndexError):
        return None

"""
Helper funtion to get the auth token from a request.
Checks the Authorization header first, then the psg_auth_token cookie
"""
def getAuthTokenFromRequest(request):
    try:
        authHeader = request.headers["Authorization"]
        expression = re.escape(TOKEN_TYPE) + r" ([^\s,]+)"
        match = re.search(expression, authHeader)
        try:
            return match.group(1)
        except (AttributeError, IndexError):
            return None
    except Exception as e:
        # No auth header, try cookies
        if 'psg_auth_token' not in request.cookies.keys():
            raise PassageError("No Passage authentication token.")
        return request.cookies['psg_auth_token']

"""
Helper function to fetch the public key for the given app id from Passage
"""
def fetchPublicKey(app_id):
    # unauthenticated request to get the public key
    r = requests.get("https://api.passage.id/v1/apps/" + app_id)

    # check response code
    if r.status_code != 200:
        raise PassageError("Could not fetch public key for app id " + app_id)

    try:
        public_key = r.json()["app"]["rsa_public_key"]
        keyBytes = b64decode(public_key)
        pubKey = load_pem_public_key(keyBytes, default_backend())
        return pubKey
    except Exception as e:
        raise PassageError("Could not fetch public key for app id " + app_id)

