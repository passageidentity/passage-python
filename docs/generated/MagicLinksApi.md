# passageidentity.openapi_client.MagicLinksApi

All URIs are relative to *https://api.passage.id/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_magic_link**](MagicLinksApi.md#create_magic_link) | **POST** /apps/{app_id}/magic-links | Create Embeddable Magic Link


# **create_magic_link**
> MagicLinkResponse create_magic_link(app_id, create_magic_link_request)

Create Embeddable Magic Link

Create magic link for a user.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import passageidentity.openapi_client
from passageidentity.openapi_client.models.create_magic_link_request import CreateMagicLinkRequest
from passageidentity.openapi_client.models.magic_link_response import MagicLinkResponse
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
    api_instance = passageidentity.openapi_client.MagicLinksApi(api_client)
    app_id = 'app_id_example' # str | App ID
    create_magic_link_request = passageidentity.openapi_client.CreateMagicLinkRequest() # CreateMagicLinkRequest | Request to create a magic link

    try:
        # Create Embeddable Magic Link
        api_response = api_instance.create_magic_link(app_id, create_magic_link_request)
        print("The response of MagicLinksApi->create_magic_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MagicLinksApi->create_magic_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App ID | 
 **create_magic_link_request** | [**CreateMagicLinkRequest**](CreateMagicLinkRequest.md)| Request to create a magic link | 

### Return type

[**MagicLinkResponse**](MagicLinkResponse.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

