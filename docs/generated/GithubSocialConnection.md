# GithubSocialConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The external ID of the Social Connection. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.github_social_connection import GithubSocialConnection

# TODO update the JSON string below
json = "{}"
# create an instance of GithubSocialConnection from a JSON string
github_social_connection_instance = GithubSocialConnection.from_json(json)
# print the JSON string representation of the object
print GithubSocialConnection.to_json()

# convert the object into a dict
github_social_connection_dict = github_social_connection_instance.to_dict()
# create an instance of GithubSocialConnection from a dict
github_social_connection_form_dict = github_social_connection.from_dict(github_social_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


