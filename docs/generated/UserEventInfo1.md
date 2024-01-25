# UserEventInfo1


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
from passageidentity.openapi_client.models.user_event_info1 import UserEventInfo1

# TODO update the JSON string below
json = "{}"
# create an instance of UserEventInfo1 from a JSON string
user_event_info1_instance = UserEventInfo1.from_json(json)
# print the JSON string representation of the object
print UserEventInfo1.to_json()

# convert the object into a dict
user_event_info1_dict = user_event_info1_instance.to_dict()
# create an instance of UserEventInfo1 from a dict
user_event_info1_form_dict = user_event_info1.from_dict(user_event_info1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


