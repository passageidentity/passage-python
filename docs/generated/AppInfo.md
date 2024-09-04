# AppInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_auth_origins** | **List[str]** |  | 
**allowed_callback_urls** | **List[str]** | The valid URLs where users can be redirected after authentication. | 
**allowed_identifier** | **str** |  | 
**allowed_logout_urls** | **List[str]** | The valid URLs where users can be redirected after logging out. | 
**application_login_uri** | **str** | A route within your application that redirects to the Authorization URL endpoint. | 
**auth_fallback_method** | **str** | Deprecated Property. Please refer to &#x60;auth_methods&#x60; to view settings for individual authentication methods. | 
**auth_fallback_method_ttl** | **int** | Deprecated Property. Please refer to &#x60;auth_methods&#x60; to view settings for individual authentication methods. | 
**auth_methods** | [**AuthMethods**](AuthMethods.md) |  | 
**auth_origin** | **str** |  | 
**auto_theme_enabled** | **bool** | Deprecated Property. Please use &#x60;hosted_theme&#x60; to set hosted page theming instead. | 
**created_at** | **datetime** |  | 
**default_language** | **str** |  | 
**id** | **str** |  | 
**layouts** | [**Layouts**](Layouts.md) |  | 
**login_url** | **str** |  | 
**light_logo_url** | **str** |  | [optional] 
**dark_logo_url** | **str** |  | [optional] 
**name** | **str** |  | 
**hosted** | **bool** | whether or not the app&#39;s login page hosted by passage | 
**hosted_subdomain** | **str** | the subdomain of the app&#39;s hosted login page | 
**hosted_theme** | [**ThemeType**](ThemeType.md) |  | 
**id_token_lifetime** | **int** |  | [optional] 
**passage_branding** | **bool** |  | 
**profile_management** | **bool** |  | 
**public_signup** | **bool** |  | 
**redirect_url** | **str** |  | 
**refresh_absolute_lifetime** | **int** |  | 
**refresh_enabled** | **bool** |  | 
**refresh_inactivity_lifetime** | **int** |  | 
**require_email_verification** | **bool** |  | 
**require_identifier_verification** | **bool** |  | 
**required_identifier** | **str** |  | 
**role** | **str** |  | 
**rsa_public_key** | **str** |  | 
**secret** | **str** | can only be retrieved by an app admin | [optional] 
**session_timeout_length** | **int** |  | 
**type** | **str** |  | 
**user_metadata_schema** | [**List[UserMetadataField]**](UserMetadataField.md) |  | 
**technologies** | [**List[Technologies]**](Technologies.md) |  | 
**element_customization** | [**ElementCustomization**](ElementCustomization.md) |  | 
**element_customization_dark** | [**ElementCustomization**](ElementCustomization.md) |  | 

## Example

```python
from passageidentity.openapi_client.models.app_info import AppInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppInfo from a JSON string
app_info_instance = AppInfo.from_json(json)
# print the JSON string representation of the object
print AppInfo.to_json()

# convert the object into a dict
app_info_dict = app_info_instance.to_dict()
# create an instance of AppInfo from a dict
app_info_form_dict = app_info.from_dict(app_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


