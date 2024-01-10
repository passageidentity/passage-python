# passageidentity.openapi_client.UserDevicesApi

All URIs are relative to *https://api.passage.id/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_devices**](UserDevicesApi.md#delete_user_devices) | **DELETE** /apps/{app_id}/users/{user_id}/devices/{device_id} | Delete a device for a user
[**list_user_devices**](UserDevicesApi.md#list_user_devices) | **GET** /apps/{app_id}/users/{user_id}/devices | List User Devices


# **delete_user_devices**
> delete_user_devices(app_id, user_id, device_id)

Delete a device for a user

Delete a device for a user.

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
    api_instance = passageidentity.openapi_client.UserDevicesApi(api_client)
    app_id = 'app_id_example' # str | App ID
    user_id = 'user_id_example' # str | User ID
    device_id = 'device_id_example' # str | Device ID

    try:
        # Delete a device for a user
        api_instance.delete_user_devices(app_id, user_id, device_id)
    except Exception as e:
        print("Exception when calling UserDevicesApi->delete_user_devices: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 
 **user_id** | **str**| User ID | 
 **device_id** | **str**| Device ID | 

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

# **list_user_devices**
> ListDevicesResponse list_user_devices(app_id, user_id)

List User Devices

List user devices.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import passageidentity.openapi_client
from passageidentity.openapi_client.models.list_devices_response import ListDevicesResponse
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
    api_instance = passageidentity.openapi_client.UserDevicesApi(api_client)
    app_id = 'app_id_example' # str | App ID
    user_id = 'user_id_example' # str | User ID

    try:
        # List User Devices
        api_response = api_instance.list_user_devices(app_id, user_id)
        print("The response of UserDevicesApi->list_user_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDevicesApi->list_user_devices: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 
 **user_id** | **str**| User ID | 

### Return type

[**ListDevicesResponse**](ListDevicesResponse.md)

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

