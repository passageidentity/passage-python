# OtpAuthMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**ttl** | **int** | Maximum time (IN SECONDS) for the auth to expire. | [default to 300]
**ttl_display_unit** | [**TtlDisplayUnit**](TtlDisplayUnit.md) |  | 

## Example

```python
from passageidentity.openapi_client.models.otp_auth_method import OtpAuthMethod

# TODO update the JSON string below
json = "{}"
# create an instance of OtpAuthMethod from a JSON string
otp_auth_method_instance = OtpAuthMethod.from_json(json)
# print the JSON string representation of the object
print OtpAuthMethod.to_json()

# convert the object into a dict
otp_auth_method_dict = otp_auth_method_instance.to_dict()
# create an instance of OtpAuthMethod from a dict
otp_auth_method_form_dict = otp_auth_method.from_dict(otp_auth_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


