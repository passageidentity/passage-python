# Client

All URIs are relative to *https://api.passage.id/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_app**](ClientApi.md#get_app) | **GET** /apps/{app_id} | Get App |
| [**create_magic_link**](ClientApi.md#create_magic_link) | **POST** /apps/{app_id}/magic-links | Create Embeddable Magic Link |


## getApp()

Get app information.

### Examples

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# Retrieve app information
psg.getApp()
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **app_id** | **String** | App ID |  |

### Return type

[**AppResponse**](../../openapi_client/models/app_response.py)

---


## createMagicLink()

Create magic link for a user.

### Examples

```python
from passageidentity import Passage
import os

PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

# Get Passage User ID from database
# ...

# Create a magic link for a user
psg.createMagicLink({
    "email": "exampleEmail@domain.com",
    "channel": "email", 
    "ttl": 12, 
})
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **create_magic_link_request** | [**CreateMagicLinkRequest**](../../docs/generated/CreateMagicLinkRequest.md) | magic link request |  |

### Return type

[**MagicLinkResponse**](../../docs/generated/MagicLinkResponse.md)

