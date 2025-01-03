# AppleUserSocialConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The external ID of the Social Connection. | 
**created_at** | **datetime** |  | 
**last_login_at** | **datetime** |  | 
**provider_identifier** | **str** | The email of connected social user. | 

## Example

```python
from passageidentity.openapi_client.models.apple_user_social_connection import AppleUserSocialConnection

# TODO update the JSON string below
json = "{}"
# create an instance of AppleUserSocialConnection from a JSON string
apple_user_social_connection_instance = AppleUserSocialConnection.from_json(json)
# print the JSON string representation of the object
print(AppleUserSocialConnection.to_json())

# convert the object into a dict
apple_user_social_connection_dict = apple_user_social_connection_instance.to_dict()
# create an instance of AppleUserSocialConnection from a dict
apple_user_social_connection_from_dict = AppleUserSocialConnection.from_dict(apple_user_social_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


