# passage-python

This Python SDK allows for verification of server-side authentication for applications using [Passage](https://passage.id)

Install this package using [pip](https://pypi.org/project/passage-identity/).

```
pip install passage-identity
```

## Instantiating the Passage Class

Passage has three arguments that can be used for initialization: `app_id`, `api_key`, and `auth_strategy`.

- `app_id` is the Passage App ID that specifies which app should be authorized. It has no default value and must to be set upon initialization.
- `api_key` is an API key for the Passage app, which can be generated in the 'App Settings' section of the [Passage Console](https://console.passage.id). It is an optional parameter and not required for authenticating requests. It is required to get or update user information.
- `auth_strategy` defines where the Passage SDK should look for the authentication token. It is set by default to `Passage.COOKIE_AUTH`, but can be changed to `Passage.HEADER_AUTH`.

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

| Field            | Type                   |
| ---------------- | ---------------------- |
| id               | string                 |
| email            | string                 |
| phone            | string                 |
| status           | string                 |
| email_verified   | boolean                |
| created_at       | Datetime               |
| last_login_at    | Datetime               |
| webauthn         | boolean                |
| webauthn_devices | array                  |
| recent_events    | array of PassageEvents |

## Activate/Deactivate User

You can also activate or deactivate a user using the Passage SDK. These actions require an API Key and deactivating a user will prevent them from logging into your application
with Passage.

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

#activate or deactivate this user
psg.deactivateUser(user_id)
```

## Update User Attributes

You can also update a user's attributes using the Passage SDK. This will require a Passage API Key.

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# update a user's email
psg.updateUser(user_id, {
    "email": "newEmail@domain.com",
    "phone": "+15005550006"
})
```

## Create User

You can also create users using their email address or phone number. Note that their phone number must be in E164 format (example shown below).

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# create a user via their email
psg.createUser({"email": "exampleEmail@domain.com"})

# create a user via their phone number
psg.createUser({"phone": "+15005550007"})
```

## Delete User

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# delete a user via their userID
deleted_user = psg.deleteUser(user_id)
if deleted_user:
    print("User has been deleted")
```

## Create an Embeddable Magic Link

To create a magic link, you should use the `createMagicLink` method. The method takes in `MagicLinkAttributes`, which is in this structure:

| Field            | Type                   |
| ---------------- | ---------------------- |
| user_id          | string                 |
| email            | string                 |
| phone            | string                 |
| channel          | ChannelType            |
| send             | boolean                |
| magic_link_path  | string                 |
| redirect_url     | string                 |

The information it returns is in a PassageMagicLink object with this structure:

| Field            | Type                   |
| ---------------- | ---------------------- |
| id               | string                 |
| secret           | string                 |
| activated        | boolean                |
| user_id          | string                 |
| app_id           | string                 |
| identifier       | string                 |
| type             | Datetime               |
| webauthn         | boolean                |
| webauthn_devices | array                  |
| recent_events    | array of PassageEvents |

```python

from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# create a magic link
magicLink = psg.createMagicLink(magicLinkAttributes={"email": "<example@email.com>", "channel": "email"})
```