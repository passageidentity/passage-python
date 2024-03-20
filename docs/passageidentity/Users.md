# User

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**activateUser()**](#activateUser) | **PATCH** /apps/{app_id}/users/{user_id}/activate | Activate User |
| [**createUser()**](#createUser) | **POST** /apps/{app_id}/users | Create User |
| [**deactivateUser()**](#deactivateUser) | **PATCH** /apps/{app_id}/users/{user_id}/deactivate | Deactivate User |
| [**deleteUser()**](#deleteUser) | **DELETE** /apps/{app_id}/users/{user_id} | Delete User |
| [**deleteUserDevice()**](#deleteUserDevice) | **DELETE** /apps/{app_id}/users/{user_id}/devices | Delete User Device |
| [**getUser()**](#getUser) | **GET** /apps/{app_id}/users/{user_id} | Get User |
| [**getUserByIdentifier()**](#getUserByIdentifier) | **GET** /apps/{app_id}/users | Get User By Identifier |
| [**listUserDevices()**](#listUserDevices) | **GET** /apps/{app_id}/users/{user_id}/devices | List User Devices |
| [**revokeUserDevice()**](#revokeUserDevices) | **DELETE** /apps/{app_id}/users/{user_id}/devices | **Deprecated:** Delete User Devices |
| [**updateUser()**](#updateUser) | **PATCH** /apps/{app_id}/users/{user_id} | Update User |
| [**signout()**](#signout) | DELETE /apps/{app_id}/users/{user_id}/tokens | **Deprecated:** Signout a user |

## activateUser()

Activate a user. They will now be able to login.

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# Activate a user
psg.activateUser(user_id)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| User ID | |


### Return type

[**UserInfo**](../../openapi_client/models/user_info.py)

---

## createUser()

Create user for an application. Must provide an email of phone number identifier. Note that their phone number must be in E164 format (example shown below).

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# create a user via their email (note that user_metadata is optional)
psg.createUser({
    "email": "exampleEmail@domain.com",
    "user_metadata": {
        "example1": "example metadata"
    }
})

# create a user via their phone number
psg.createUser({"phone": "+15005550007"})
```

### Parameters

| Name | Type | Description  |
| ------------- | ------------- | ----------- |
| **user_id** | **string**| User ID |
| **create_user_request** | [**CreateUserRequest**](../../openapi_client/models/create_user_request.py)| user settings |


### Return type

[**UserInfo**](../../openapi_client/models/user_info.py)

---

## deactivateUser()

Deactivate a user. Their account will still exist, but they will not be able to login.

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# Deactivate this user
psg.deactivateUser(user_id)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| User ID | |


### Return type

[**UserInfo**](../../openapi_client/models/user_info.py)

---

## deleteUserDevice

Delete user device

### Examples

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# Deactivate this user
psg.deleteUserDevice(user_id, device_id)
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **user_id** | **String** | User ID |  |
| **device_id** | **String** | Device ID |  |

### Return type

nil (empty response body)

---

## deleteUser()

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

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| User ID | |


### Return type

[**UserInfo**](../../openapi_client/models/user_info.py)

---

## getUser()

To retrieve information about a user, you should use the `getUser` method.

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
    user = psg.getUser(user_id)
	print(user.email)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| User ID | |


### Return type

[**UserInfo**](../../openapi_client/models/user_info.py)

---

## getUserByIdentifier()

To retrieve information about a user, you should use the `getUserByIdentifier` method.

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
    user = psg.getUserByIdentifier(user_email)
	print(user.id)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **identifier** | **string**| User email or phone number | |


### Return type

[**UserInfo**](../../openapi_client/models/user_info.py)

---

## listUserDevices()

List User Devices.

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# Activate a user
psg.listUserDevices(user_id)
```

### Parameters

| Name | Type | Description  |
| ------------- | ------------- | ------------- |
| **user_id** | **string**| User ID | |


### Return type

[**UserInfo**](../../openapi_client/models/user_info.py)

---

## revokeUserDevice

**Deprecated:** Use [deleteUserDevices](#deleteUserDevices) instead

### Examples

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# Deactivate this user
psg.revokeUserDevice(user_id, device_id)
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **user_id** | **String** | User ID |  |
| **device_id** | **String** | Device ID |  |

### Return type

nil (empty response body)

---

## updateUser()

Update a user's attributes.

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# update a user (note that user_metadata is optional)
psg.updateUser(user_id, {
    "email": "newEmail@domain.com",
    "phone": "+15005550006",
    "user_metadata": {
        "example1": "example metadata"
    }
})
```

### Parameters

| Name | Type | Description  |
| ------------- | ------------- | ------------- |
| **user_id** | **string**| User ID | |
| **update_user_request** | [**UpdateUserRequest**](../../openapi_client/models/update_user_request.py)| user settings |


### Return type

[**UserInfo**](../../openapi_client/models/user_info.py)

---

## signout()

Revokes all refresh tokens for a user

### Examples

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# Revokes all refresh tokens
psg.updateUser(user_id)
```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **user_id** | **String** | User ID |  |

### Return type

bool