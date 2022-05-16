import os
import re
from base64 import b64decode
import requests
from django.core.handlers.wsgi import WSGIRequest

from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend

from passageidentity.errors import PassageError

TOKEN_TYPE = "Bearer"
BASE_URL = "https://api.passage.id/v1/apps/"

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
def getAuthTokenFromRequest(request, auth_strategy):
    if auth_strategy == 2:
        authHeader = request.headers["Authorization"]
        expression = re.escape(TOKEN_TYPE) + r" ([^\s,]+)"
        match = re.search(expression, authHeader)
        try:
            return match.group(1)
        except (AttributeError, IndexError):
            return None
    else:
        try:
            cookies = request.COOKIES
            if 'psg_auth_token' not in cookies.keys():
                raise PassageError("No Passage authentication token.")
            return cookies['psg_auth_token']
        except:
            try:
                cookies = request.cookies
                if 'psg_auth_token' not in cookies.keys():
                    raise PassageError("No Passage authentication token.")
                return cookies['psg_auth_token']
            except:
                raise PassageError("No passage authentication token")

"""
Helper function to fetch the public key for the given app id from Passage
"""
def fetchApp(app_id):
    # unauthenticated request to get the public key
    r = requests.get(BASE_URL + app_id)

    # check response code
    if r.status_code != 200:
        raise PassageError("Could not fetch app information for app id " + app_id)

    return r.json()["app"]

