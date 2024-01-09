# UpdateOtpAuthMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**ttl** | **int** | Maximum time (IN SECONDS) for the auth to expire. | [optional] [default to 300]
**ttl_display_unit** | [**TtlDisplayUnit**](TtlDisplayUnit.md) |  | [optional] 

## Example

```python
from passageidentity.openapi_client.models.update_otp_auth_method import UpdateOtpAuthMethod

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOtpAuthMethod from a JSON string
update_otp_auth_method_instance = UpdateOtpAuthMethod.from_json(json)
# print the JSON string representation of the object
print UpdateOtpAuthMethod.to_json()

# convert the object into a dict
update_otp_auth_method_dict = update_otp_auth_method_instance.to_dict()
# create an instance of UpdateOtpAuthMethod from a dict
update_otp_auth_method_form_dict = update_otp_auth_method.from_dict(update_otp_auth_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


