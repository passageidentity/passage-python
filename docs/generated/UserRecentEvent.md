# UserRecentEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**id** | **str** |  | 
**ip_addr** | **str** |  | 
**status** | [**UserEventStatus**](UserEventStatus.md) |  | 
**type** | **str** |  | 
**user_agent** | **str** |  | 
**action** | [**UserEventAction**](UserEventAction.md) |  | 
**social_login_type** | [**SocialConnectionType**](SocialConnectionType.md) |  | 

## Example

```python
from passageidentity.openapi_client.models.user_recent_event import UserRecentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecentEvent from a JSON string
user_recent_event_instance = UserRecentEvent.from_json(json)
# print the JSON string representation of the object
print UserRecentEvent.to_json()

# convert the object into a dict
user_recent_event_dict = user_recent_event_instance.to_dict()
# create an instance of UserRecentEvent from a dict
user_recent_event_form_dict = user_recent_event.from_dict(user_recent_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


