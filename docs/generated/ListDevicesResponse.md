# ListDevicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[WebAuthnDevices]**](WebAuthnDevices.md) |  | 

## Example

```python
from passageidentity.openapi_client.models.list_devices_response import ListDevicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDevicesResponse from a JSON string
list_devices_response_instance = ListDevicesResponse.from_json(json)
# print the JSON string representation of the object
print(ListDevicesResponse.to_json())

# convert the object into a dict
list_devices_response_dict = list_devices_response_instance.to_dict()
# create an instance of ListDevicesResponse from a dict
list_devices_response_from_dict = ListDevicesResponse.from_dict(list_devices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


