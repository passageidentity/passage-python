# Authentication

All URIs are relative to *https://api.passage.id/v1*

| Method | Description |
| ------ | ----------- |
| [**authenticate_requauthenticateRequestest**](#authenticateRequest) |  **Deprecated:** Revokes refresh tokens |
| [**revoke_user_refresh_tokens**](#revokeUserRefreshTokens) | Revokes user tokens |
| [**validateJwt**](#validateJwt) |  Validates jwt token


---

## authenticateRequest

**Deprecated:** Validates that request has the correct jwt token


### Examples

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID_ = os.environ.get("PASSAGE_APP_ID")

def exampleFlaskMiddleware(request):
    psg = Passage(PASSAGE_APP_ID)
    user = psg.authenticateRequest(request)
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **request** | **RequestObject** | request |  |

### Return type

[**UserInfo**](../../openapi_client/models/user_info.py)

---

## revokeUserRefreshTokens()

Revokes user tokens

### Examples

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID_ = os.environ.get("PASSAGE_APP_ID")

def exampleFlaskMiddleware(request):
    psg = Passage(PASSAGE_APP_ID)
    user = psg.revokeUserRefreshTokens(user_id)
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **user_id** | **string** | user id |  |

### Return type

boolean

---

## validateJwt()

Validates jwt token for a user

### Examples

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID_ = os.environ.get("PASSAGE_APP_ID")

def exampleFlaskMiddleware(request):
    psg = Passage(PASSAGE_APP_ID)
    user = psg.validateJwt(token)
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **token** | **String** | jwt token |  |

### Return type

[**UserInfo**](../../openapi_client/models/user_info.py)
