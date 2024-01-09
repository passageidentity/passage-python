# passageidentity.openapi_client.TokensApi

All URIs are relative to *https://api.passage.id/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revoke_user_refresh_tokens**](TokensApi.md#revoke_user_refresh_tokens) | **DELETE** /apps/{app_id}/users/{user_id}/tokens | Revokes refresh tokens


# **revoke_user_refresh_tokens**
> revoke_user_refresh_tokens(app_id, user_id)

Revokes refresh tokens

Revokes all refresh tokens for a user

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import passageidentity.openapi_client
from passageidentity.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.passage.id/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = passageidentity.openapi_client.Configuration(
    host = "https://api.passage.id/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = passageidentity.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with passageidentity.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = passageidentity.openapi_client.TokensApi(api_client)
    app_id = 'app_id_example' # str | App ID
    user_id = 'user_id_example' # str | User ID

    try:
        # Revokes refresh tokens
        api_instance.revoke_user_refresh_tokens(app_id, user_id)
    except Exception as e:
        print("Exception when calling TokensApi->revoke_user_refresh_tokens: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 
 **user_id** | **str**| User ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

