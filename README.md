<img src="https://storage.googleapis.com/passage-docs/passage-logo-gradient.svg" alt="Passage logo" style="width:250px;"/>

[![PyPI version](https://badge.fury.io/py/passage-identity.svg)](https://badge.fury.io/py/passage-identity)
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
- **Deprecated** `auth_strategy` defines where the Passage SDK should look for the authentication token. It is set by default to `Passage.COOKIE_AUTH`, but can be changed to `Passage.HEADER_AUTH`.

```python

from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")

psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
```


## Available Functions


Method | Description
------------- | -------------
[**activateUser**](./docs/passageidentity/Users.md#activateUser) | Activate User
[**deactivateUser**](./docs/passageidentity/Users.md#deactivateUser) | Deactivate User
[**deleteUser**](./docs/passageidentity/Users.md#deleteUser) | Delete User
[**deleteUserDevice**](./docs/passageidentity/Users.md#deleteUserDevice) | Delete User Device
[**authenticateRequest**](./docs/passageidentity/Authentication.md#authenticateRequest) | Validates user jwt token
[**createMagicLink**](./docs/passageidentity/Client.md#createmagiclink) | Create Embeddable Magic Link
[**createUser**](./docs/passageidentity/Users.md#createUser) | Create User
[**deleteUserDevice**](./docs/passageidentity/Users.md#deleteUserDevice) | Delete a device for a user
[**getApp**](./docs/passageidentity/Users.md#getApp) |  Get App
[**getUser**](./docs/passageidentity/Users.md#getUser) | Get User
[**listUserDevices**](./docs/passageidentity/Users.md#listUserDevices) | List User Devices
[**revokeUserDevice**](./docs/passageidentity/Users.md#revokeUserDevice) | **Deprecated** Delete User Device
[**revokeUserRefreshTokens**](./docs/passageidentity/Authentication.md#revokeUserRefreshTokens) | Signout User
[**signOut**](./docs/passageidentity/Users.md#signout) | **Deprecated** Signout User
[**updateUser**](./docs/passageidentity/Users.md#updateUser) | Update User
[**validateJwt**](./docs/passageidentity/Authentication.md#validateJwt) | Validates user jwt token