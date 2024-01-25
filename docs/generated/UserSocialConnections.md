# UserSocialConnections


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apple** | [**AppleUserSocialConnection**](AppleUserSocialConnection.md) |  | [optional] 
**github** | [**GithubUserSocialConnection**](GithubUserSocialConnection.md) |  | [optional] 
**google** | [**GoogleUserSocialConnection**](GoogleUserSocialConnection.md) |  | [optional] 

## Example

```python
from passageidentity.openapi_client.models.user_social_connections import UserSocialConnections

# TODO update the JSON string below
json = "{}"
# create an instance of UserSocialConnections from a JSON string
user_social_connections_instance = UserSocialConnections.from_json(json)
# print the JSON string representation of the object
print UserSocialConnections.to_json()

# convert the object into a dict
user_social_connections_dict = user_social_connections_instance.to_dict()
# create an instance of UserSocialConnections from a dict
user_social_connections_form_dict = user_social_connections.from_dict(user_social_connections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


