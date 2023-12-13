# openapi_client.UsersApi

All URIs are relative to *https://api.passage.id/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user**](UsersApi.md#activate_user) | **PATCH** /apps/{app_id}/users/{user_id}/activate | Activate User
[**create_user**](UsersApi.md#create_user) | **POST** /apps/{app_id}/users | Create User
[**deactivate_user**](UsersApi.md#deactivate_user) | **PATCH** /apps/{app_id}/users/{user_id}/deactivate | Deactivate User
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /apps/{app_id}/users/{user_id} | Delete User
[**get_user**](UsersApi.md#get_user) | **GET** /apps/{app_id}/users/{user_id} | Get User
[**update_user**](UsersApi.md#update_user) | **PATCH** /apps/{app_id}/users/{user_id} | Update User


# **activate_user**
> UserResponse activate_user(app_id, user_id)

Activate User

Activate a user. They will now be able to login.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.user_response import UserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.passage.id/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.passage.id/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsersApi(api_client)
    app_id = 'app_id_example' # str | App ID
    user_id = 'user_id_example' # str | User ID

    try:
        # Activate User
        api_response = api_instance.activate_user(app_id, user_id)
        print("The response of UsersApi->activate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->activate_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 
 **user_id** | **str**| User ID | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **create_user**
> UserResponse create_user(app_id, create_user_request)

Create User

Create user for an application. Must provide an email of phone number identifier.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.create_user_request import CreateUserRequest
from openapi_client.models.user_response import UserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.passage.id/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.passage.id/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsersApi(api_client)
    app_id = 'app_id_example' # str | App ID
    create_user_request = openapi_client.CreateUserRequest() # CreateUserRequest | email, phone, user_metadata

    try:
        # Create User
        api_response = api_instance.create_user(app_id, create_user_request)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)| email, phone, user_metadata | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_user**
> UserResponse deactivate_user(app_id, user_id)

Deactivate User

Deactivate a user. Their account will still exist, but they will not be able to login.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.user_response import UserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.passage.id/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.passage.id/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsersApi(api_client)
    app_id = 'app_id_example' # str | App ID
    user_id = 'user_id_example' # str | User ID

    try:
        # Deactivate User
        api_response = api_instance.deactivate_user(app_id, user_id)
        print("The response of UsersApi->deactivate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->deactivate_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 
 **user_id** | **str**| User ID | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **delete_user**
> delete_user(app_id, user_id)

Delete User

Delete a user.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.passage.id/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.passage.id/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsersApi(api_client)
    app_id = 'app_id_example' # str | App ID
    user_id = 'user_id_example' # str | User ID

    try:
        # Delete User
        api_instance.delete_user(app_id, user_id)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
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

# **get_user**
> UserResponse get_user(app_id, user_id)

Get User

Get information about a user.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.user_response import UserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.passage.id/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.passage.id/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsersApi(api_client)
    app_id = 'app_id_example' # str | App ID
    user_id = 'user_id_example' # str | User ID

    try:
        # Get User
        api_response = api_instance.get_user(app_id, user_id)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 
 **user_id** | **str**| User ID | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **update_user**
> UserResponse update_user(app_id, user_id, update_user_request)

Update User

Update a user's information.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.update_user_request import UpdateUserRequest
from openapi_client.models.user_response import UserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.passage.id/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.passage.id/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsersApi(api_client)
    app_id = 'app_id_example' # str | App ID
    user_id = 'user_id_example' # str | User ID
    update_user_request = openapi_client.UpdateUserRequest() # UpdateUserRequest | user settings

    try:
        # Update User
        api_response = api_instance.update_user(app_id, user_id, update_user_request)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 
 **user_id** | **str**| User ID | 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)| user settings | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

