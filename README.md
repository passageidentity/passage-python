# passage-python

This Python SDK allows for verification of server-side authentication for applications using [Passage](https://passage.id)

Install this package using [pip](https://pypi.org/project/passage-identity/).

```
pip install passage-identity
```

## Authenticating a Request

To authenticate an HTTP request in a Flask application, you can use the Passage library in a middleware function. 
You need to provide Passage with your app ID in order to verify the JWTs.

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID_ = os.environ.get("PASSAGE_APP_ID")

def exampleFlaskMiddleware(request):
    psg = Passage(PASSAGE_APP_ID)
    user = psg.authenticateRequest(request)
```

## Retrieve User Info
To retrieve information about a user, you should use the `getPassageUser` method. You will need to use a Passage API key, which can be created in the Passage Console under your Application Settings. This API key grants your web server access to the Passage management APIs to get and update information about users.
This API key must be protected and stored in an appropriate secure storage location. It should never be hard-coded in the repository.

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

def exampleFlaskMiddleware(request):
    g.user = psg.authenticateRequest(request)

@auth.route('/home')
def authenticatedEndpoint():
    user = psg.getPassageUser(g.user)
	print(user.email)
```

The information available in the Passage User object is as

| Field  | Type    |
|--------|---------|
| id | string  |  
| email  | string  | 
| active | boolean |
| email_verified | boolean  |  
| created_at  | Datetime  | 
| last_login_at | Datetime | 
| webauthn  | boolean  | 
| webauthn_devices | array |
|recent_events| array of PassageEvents |
