# WebAuthnDevices


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The first time this webAuthn device was used to authenticate the user | 
**cred_id** | **str** | The CredID for this webAuthn device | 
**friendly_name** | **str** | The friendly name for the webAuthn device used to authenticate | 
**id** | **str** | The ID of the webAuthn device used for authentication | 
**last_login_at** | **datetime** | The last time this webAuthn device was used to authenticate the user | 
**type** | [**WebAuthnType**](WebAuthnType.md) |  | 
**updated_at** | **datetime** | The last time this webAuthn device was updated | 
**usage_count** | **int** | How many times this webAuthn device has been used to authenticate the user | 
**icons** | [**WebAuthnIcons**](WebAuthnIcons.md) |  | 

## Example

```python
from passageidentity.openapi_client.models.web_authn_devices import WebAuthnDevices

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnDevices from a JSON string
web_authn_devices_instance = WebAuthnDevices.from_json(json)
# print the JSON string representation of the object
print WebAuthnDevices.to_json()

# convert the object into a dict
web_authn_devices_dict = web_authn_devices_instance.to_dict()
# create an instance of WebAuthnDevices from a dict
web_authn_devices_form_dict = web_authn_devices.from_dict(web_authn_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


