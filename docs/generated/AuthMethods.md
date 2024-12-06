# AuthMethods

Denotes what methods this app is allowed to use for authentication with configurations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passkeys** | [**PasskeysAuthMethod**](PasskeysAuthMethod.md) |  | 
**otp** | [**OtpAuthMethod**](OtpAuthMethod.md) |  | 
**magic_link** | [**MagicLinkAuthMethod**](MagicLinkAuthMethod.md) |  | 

## Example

```python
from passageidentity.openapi_client.models.auth_methods import AuthMethods

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMethods from a JSON string
auth_methods_instance = AuthMethods.from_json(json)
# print the JSON string representation of the object
print(AuthMethods.to_json())

# convert the object into a dict
auth_methods_dict = auth_methods_instance.to_dict()
# create an instance of AuthMethods from a dict
auth_methods_from_dict = AuthMethods.from_dict(auth_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


