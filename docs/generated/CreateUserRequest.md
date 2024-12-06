# CreateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email of the new user. Either this or &#x60;phone&#x60; is required; both may be provided. | [optional] 
**phone** | **str** | Phone number of the new user. Either this or &#x60;email&#x60; is required; both may be provided. | [optional] 
**user_metadata** | **object** |  | [optional] 

## Example

```python
from passageidentity.openapi_client.models.create_user_request import CreateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequest from a JSON string
create_user_request_instance = CreateUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserRequest.to_json())

# convert the object into a dict
create_user_request_dict = create_user_request_instance.to_dict()
# create an instance of CreateUserRequest from a dict
create_user_request_from_dict = CreateUserRequest.from_dict(create_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


