# CreateUserArgs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email of the new user. Either this or &#x60;phone&#x60; is required; both may be provided. | [optional] 
**phone** | **str** | Phone number of the new user. Either this or &#x60;email&#x60; is required; both may be provided. | [optional] 
**user_metadata** | **object** |  | [optional] 

## Example

```python
from passageidentity.openapi_client.models.create_user_args import CreateUserArgs

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserArgs from a JSON string
create_user_args_instance = CreateUserArgs.from_json(json)
# print the JSON string representation of the object
print(CreateUserArgs.to_json())

# convert the object into a dict
create_user_args_dict = create_user_args_instance.to_dict()
# create an instance of CreateUserArgs from a dict
create_user_args_from_dict = CreateUserArgs.from_dict(create_user_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


