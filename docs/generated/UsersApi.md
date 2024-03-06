# passageidentity.openapi_client.UsersApi

All URIs are relative to *https://api.passage.id/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user**](UsersApi.md#activate_user) | **PATCH** /apps/{app_id}/users/{user_id}/activate | Activate User
[**create_user**](UsersApi.md#create_user) | **POST** /apps/{app_id}/users | Create User
[**deactivate_user**](UsersApi.md#deactivate_user) | **PATCH** /apps/{app_id}/users/{user_id}/deactivate | Deactivate User
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /apps/{app_id}/users/{user_id} | Delete User
[**get_user**](UsersApi.md#get_user) | **GET** /apps/{app_id}/users/{user_id} | Get User
[**list_paginated_users**](UsersApi.md#list_paginated_users) | **GET** /apps/{app_id}/users | List Users
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
import passageidentity.openapi_client
from passageidentity.openapi_client.models.user_response import UserResponse
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
    api_instance = passageidentity.openapi_client.UsersApi(api_client)
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
import passageidentity.openapi_client
from passageidentity.openapi_client.models.create_user_request import CreateUserRequest
from passageidentity.openapi_client.models.user_response import UserResponse
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
    api_instance = passageidentity.openapi_client.UsersApi(api_client)
    app_id = 'app_id_example' # str | App ID
    create_user_request = passageidentity.openapi_client.CreateUserRequest() # CreateUserRequest | email, phone, user_metadata

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
import passageidentity.openapi_client
from passageidentity.openapi_client.models.user_response import UserResponse
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
    api_instance = passageidentity.openapi_client.UsersApi(api_client)
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
    api_instance = passageidentity.openapi_client.UsersApi(api_client)
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
import passageidentity.openapi_client
from passageidentity.openapi_client.models.user_response import UserResponse
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
    api_instance = passageidentity.openapi_client.UsersApi(api_client)
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

# **list_paginated_users**
> ListPaginatedUsersResponse list_paginated_users(app_id, page=page, limit=limit, created_before=created_before, order_by=order_by, identifier=identifier, id=id, login_count=login_count, status=status, email_verified=email_verified, created_at=created_at, updated_at=updated_at, last_login_at=last_login_at)

List Users

List users for an app.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import passageidentity.openapi_client
from passageidentity.openapi_client.models.list_paginated_users_response import ListPaginatedUsersResponse
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
    api_instance = passageidentity.openapi_client.UsersApi(api_client)
    app_id = 'app_id_example' # str | App ID
    page = 56 # int | page to fetch (min=1) (optional)
    limit = 56 # int | number of users to fetch per page (max=500) (optional)
    created_before = 56 # int | Unix timestamp to anchor pagination results (fetches events that were created before the timestamp) (optional)
    order_by = 'order_by_example' # str | Comma separated list of <field>:<ASC/DESC> (example: order_by=id:DESC,created_at:ASC) **cannot order_by `identifier` (optional)
    identifier = 'identifier_example' # str | search users email OR phone (pagination prepended operators identifier=<val>, identifier=<ne:val>, identifier=<gt:val>, identifier=<lt:val>, identifier=<like:val>, identifier=<not_like:val>) (optional)
    id = 'id_example' # str | search users id (pagination prepended operators id=<val>, id=<ne:val>, id=<gt:val>, id=<lt:val>, id=<like:val>, id=<not_like:val>) (optional)
    login_count = 56 # int | search users login_count (pagination prepended operators login_count=<val>, login_count=<ne:val>, login_count=<gt:val>, login_count=<lt:val>) (optional)
    status = 'status_example' # str | search users by status (pagination prepended operators status=<val>, status=<ne:val>, status=<gt:val>, status=<lt:val>, status=<like:val>, status=<not_like:val>) -- valid values: (active, inactive, pending) (optional)
    email_verified = True # bool | search users email_verified (pagination prepended operators email_verified=<val>, email_verified=<ne:val>, email_verified=<gt:val>, email_verified=<lt:val>) (optional)
    created_at = 'created_at_example' # str | search users created_at (pagination prepended operators created_at=<val>, created_at=<ne:val>, created_at=<gt:val>, created_at=<lt:val> -- valid timestamp in the format: 2006-01-02T15:04:05.000000Z required (optional)
    updated_at = 'updated_at_example' # str | search users updated_at (pagination prepended operators updated_at=<val>, updated_at=<ne:val>, updated_at=<gt:val>, updated_at=<lt:val> -- valid timestamp in the format: 2006-01-02T15:04:05.000000Z required (optional)
    last_login_at = 'last_login_at_example' # str | search users last_login_at (pagination prepended operators last_login_at=<val>, lat_login_at=<ne:val>, last_login_at=<gt:val>, last_login_at=<lt:val> -- valid timestamp in the format: 2006-01-02T15:04:05.000000Z required (optional)

    try:
        # List Users
        api_response = api_instance.list_paginated_users(app_id, page=page, limit=limit, created_before=created_before, order_by=order_by, identifier=identifier, id=id, login_count=login_count, status=status, email_verified=email_verified, created_at=created_at, updated_at=updated_at, last_login_at=last_login_at)
        print("The response of UsersApi->list_paginated_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_paginated_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 
 **page** | **int**| page to fetch (min&#x3D;1) | [optional] 
 **limit** | **int**| number of users to fetch per page (max&#x3D;500) | [optional] 
 **created_before** | **int**| Unix timestamp to anchor pagination results (fetches events that were created before the timestamp) | [optional] 
 **order_by** | **str**| Comma separated list of &lt;field&gt;:&lt;ASC/DESC&gt; (example: order_by&#x3D;id:DESC,created_at:ASC) **cannot order_by &#x60;identifier&#x60; | [optional] 
 **identifier** | **str**| search users email OR phone (pagination prepended operators identifier&#x3D;&lt;val&gt;, identifier&#x3D;&lt;ne:val&gt;, identifier&#x3D;&lt;gt:val&gt;, identifier&#x3D;&lt;lt:val&gt;, identifier&#x3D;&lt;like:val&gt;, identifier&#x3D;&lt;not_like:val&gt;) | [optional] 
 **id** | **str**| search users id (pagination prepended operators id&#x3D;&lt;val&gt;, id&#x3D;&lt;ne:val&gt;, id&#x3D;&lt;gt:val&gt;, id&#x3D;&lt;lt:val&gt;, id&#x3D;&lt;like:val&gt;, id&#x3D;&lt;not_like:val&gt;) | [optional] 
 **login_count** | **int**| search users login_count (pagination prepended operators login_count&#x3D;&lt;val&gt;, login_count&#x3D;&lt;ne:val&gt;, login_count&#x3D;&lt;gt:val&gt;, login_count&#x3D;&lt;lt:val&gt;) | [optional] 
 **status** | **str**| search users by status (pagination prepended operators status&#x3D;&lt;val&gt;, status&#x3D;&lt;ne:val&gt;, status&#x3D;&lt;gt:val&gt;, status&#x3D;&lt;lt:val&gt;, status&#x3D;&lt;like:val&gt;, status&#x3D;&lt;not_like:val&gt;) -- valid values: (active, inactive, pending) | [optional] 
 **email_verified** | **bool**| search users email_verified (pagination prepended operators email_verified&#x3D;&lt;val&gt;, email_verified&#x3D;&lt;ne:val&gt;, email_verified&#x3D;&lt;gt:val&gt;, email_verified&#x3D;&lt;lt:val&gt;) | [optional] 
 **created_at** | **str**| search users created_at (pagination prepended operators created_at&#x3D;&lt;val&gt;, created_at&#x3D;&lt;ne:val&gt;, created_at&#x3D;&lt;gt:val&gt;, created_at&#x3D;&lt;lt:val&gt; -- valid timestamp in the format: 2006-01-02T15:04:05.000000Z required | [optional] 
 **updated_at** | **str**| search users updated_at (pagination prepended operators updated_at&#x3D;&lt;val&gt;, updated_at&#x3D;&lt;ne:val&gt;, updated_at&#x3D;&lt;gt:val&gt;, updated_at&#x3D;&lt;lt:val&gt; -- valid timestamp in the format: 2006-01-02T15:04:05.000000Z required | [optional] 
 **last_login_at** | **str**| search users last_login_at (pagination prepended operators last_login_at&#x3D;&lt;val&gt;, lat_login_at&#x3D;&lt;ne:val&gt;, last_login_at&#x3D;&lt;gt:val&gt;, last_login_at&#x3D;&lt;lt:val&gt; -- valid timestamp in the format: 2006-01-02T15:04:05.000000Z required | [optional] 

### Return type

[**ListPaginatedUsersResponse**](ListPaginatedUsersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **update_user**
> UserResponse update_user(app_id, user_id, update_user_request)

Update User

Update a user's information.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import passageidentity.openapi_client
from passageidentity.openapi_client.models.update_user_request import UpdateUserRequest
from passageidentity.openapi_client.models.user_response import UserResponse
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
    api_instance = passageidentity.openapi_client.UsersApi(api_client)
    app_id = 'app_id_example' # str | App ID
    user_id = 'user_id_example' # str | User ID
    update_user_request = passageidentity.openapi_client.UpdateUserRequest() # UpdateUserRequest | user settings

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

