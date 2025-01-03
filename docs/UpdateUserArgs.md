# UpdateUserArgs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**user_metadata** | **object** |  | [optional] 

## Example

```python
from passageidentity.openapi_client.models.update_user_args import UpdateUserArgs

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserArgs from a JSON string
update_user_args_instance = UpdateUserArgs.from_json(json)
# print the JSON string representation of the object
print(UpdateUserArgs.to_json())

# convert the object into a dict
update_user_args_dict = update_user_args_instance.to_dict()
# create an instance of UpdateUserArgs from a dict
update_user_args_from_dict = UpdateUserArgs.from_dict(update_user_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


