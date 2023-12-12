# MagicLinkAuthMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**ttl** | **int** | Maximum time (IN SECONDS) for the auth to expire. | [default to 300]
**ttl_display_unit** | [**TtlDisplayUnit**](TtlDisplayUnit.md) |  | 

## Example

```python
from openapi_client.models.magic_link_auth_method import MagicLinkAuthMethod

# TODO update the JSON string below
json = "{}"
# create an instance of MagicLinkAuthMethod from a JSON string
magic_link_auth_method_instance = MagicLinkAuthMethod.from_json(json)
# print the JSON string representation of the object
print MagicLinkAuthMethod.to_json()

# convert the object into a dict
magic_link_auth_method_dict = magic_link_auth_method_instance.to_dict()
# create an instance of MagicLinkAuthMethod from a dict
magic_link_auth_method_form_dict = magic_link_auth_method.from_dict(magic_link_auth_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


