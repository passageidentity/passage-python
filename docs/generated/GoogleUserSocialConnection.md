# GoogleUserSocialConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The external ID of the Social Connection. | 
**created_at** | **datetime** |  | 
**last_login_at** | **datetime** |  | 
**provider_identifier** | **str** | The email of connected social user. | 

## Example

```python
from passageidentity.openapi_client.models.google_user_social_connection import GoogleUserSocialConnection

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleUserSocialConnection from a JSON string
google_user_social_connection_instance = GoogleUserSocialConnection.from_json(json)
# print the JSON string representation of the object
print GoogleUserSocialConnection.to_json()

# convert the object into a dict
google_user_social_connection_dict = google_user_social_connection_instance.to_dict()
# create an instance of GoogleUserSocialConnection from a dict
google_user_social_connection_form_dict = google_user_social_connection.from_dict(google_user_social_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


