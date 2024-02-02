# GithubUserSocialConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The external ID of the Social Connection. | 
**created_at** | **datetime** |  | 
**last_login_at** | **datetime** |  | 
**provider_identifier** | **str** | The email of connected social user. | 

## Example

```python
from passageidentity.openapi_client.models.github_user_social_connection import GithubUserSocialConnection

# TODO update the JSON string below
json = "{}"
# create an instance of GithubUserSocialConnection from a JSON string
github_user_social_connection_instance = GithubUserSocialConnection.from_json(json)
# print the JSON string representation of the object
print GithubUserSocialConnection.to_json()

# convert the object into a dict
github_user_social_connection_dict = github_user_social_connection_instance.to_dict()
# create an instance of GithubUserSocialConnection from a dict
github_user_social_connection_form_dict = github_user_social_connection.from_dict(github_user_social_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


