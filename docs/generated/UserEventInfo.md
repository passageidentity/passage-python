# UserEventInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**ip_addr** | **str** |  | 
**type** | **str** |  | 
**user_agent** | **str** |  | 

## Example

```python
from passageidentity.openapi_client.models.user_event_info import UserEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserEventInfo from a JSON string
user_event_info_instance = UserEventInfo.from_json(json)
# print the JSON string representation of the object
print UserEventInfo.to_json()

# convert the object into a dict
user_event_info_dict = user_event_info_instance.to_dict()
# create an instance of UserEventInfo from a dict
user_event_info_form_dict = user_event_info.from_dict(user_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


