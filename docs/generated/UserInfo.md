# UserInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**email** | **str** |  | 
**email_verified** | **bool** |  | 
**external_id** | **str** | The external ID of the user. Only set if the user was created in a Flex app. | 
**id** | **str** |  | 
**last_login_at** | **datetime** |  | 
**login_count** | **int** |  | 
**phone** | **str** |  | 
**phone_verified** | **bool** |  | 
**recent_events** | [**List[UserRecentEvent]**](UserRecentEvent.md) |  | 
**social_connections** | [**UserSocialConnections**](UserSocialConnections.md) |  | 
**status** | [**UserStatus**](UserStatus.md) |  | 
**updated_at** | **datetime** |  | 
**user_metadata** | **object** |  | 
**webauthn** | **bool** |  | 
**webauthn_devices** | [**List[WebAuthnDevices]**](WebAuthnDevices.md) |  | 
**webauthn_types** | [**List[WebAuthnType]**](WebAuthnType.md) | List of credential types that have been used for authentication | 

## Example

```python
from passageidentity.openapi_client.models.user_info import UserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfo from a JSON string
user_info_instance = UserInfo.from_json(json)
# print the JSON string representation of the object
print(UserInfo.to_json())

# convert the object into a dict
user_info_dict = user_info_instance.to_dict()
# create an instance of UserInfo from a dict
user_info_from_dict = UserInfo.from_dict(user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


