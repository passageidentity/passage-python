import os
import re
from base64 import b64decode

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
Helper function to load the Base-64 encoded passage public key from an environment
variable
"""
def loadPublicKey():
    # load base64 encoded public key 
    b64Key = os.environ.get("PASSAGE_PUBLIC_KEY")
    if not b64Key:
        raise PassageError("Missing PASSAGE_PUBLIC_KEY environment variable")

    # decode public key into PEM format
    try:
        keyBytes = b64decode(b64Key)
        pubKey = load_pem_public_key(keyBytes, default_backend())
        return pubKey
    except Exception as e:
        raise PassageError("PASSAGE_PUBLIC_KEY is not a valid public key")

		