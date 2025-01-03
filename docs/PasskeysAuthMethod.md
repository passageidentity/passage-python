# PasskeysAuthMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [default to True]

## Example

```python
from passageidentity.openapi_client.models.passkeys_auth_method import PasskeysAuthMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PasskeysAuthMethod from a JSON string
passkeys_auth_method_instance = PasskeysAuthMethod.from_json(json)
# print the JSON string representation of the object
print(PasskeysAuthMethod.to_json())

# convert the object into a dict
passkeys_auth_method_dict = passkeys_auth_method_instance.to_dict()
# create an instance of PasskeysAuthMethod from a dict
passkeys_auth_method_from_dict = PasskeysAuthMethod.from_dict(passkeys_auth_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


