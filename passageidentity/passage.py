
import jwt
from passageidentity.helper import extractToken, getAuthTokenFromRequest, loadPublicKey 
from passageidentity.errors import PassageError

class Passage:

    """
    When a Passage object is created, attempt to load the public key from the environment variable.
    This is currently required.
    """
    def __init__(self):
        self.passage_pubkey = loadPublicKey()
    
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

        print(token)
        # load and parse the JWT
        try:
            claims = jwt.decode(token, self.passage_pubkey, algorithms=["RS256"])
            return claims["sub"]
        except Exception as e:
            raise PassageError("JWT is not valid: " + str(e))
