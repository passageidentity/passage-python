# CreateMagicLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**MagicLinkChannel**](MagicLinkChannel.md) |  | [optional] 
**email** | **str** |  | [optional] 
**language** | **str** | language of the email to send (optional) | [optional] 
**magic_link_path** | **str** | must be a relative url | [optional] 
**phone** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**send** | **bool** |  | [optional] 
**ttl** | **int** |  | [optional] 
**type** | [**MagicLinkType**](MagicLinkType.md) |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from passageidentity.openapi_client.models.create_magic_link_request import CreateMagicLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMagicLinkRequest from a JSON string
create_magic_link_request_instance = CreateMagicLinkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMagicLinkRequest.to_json())

# convert the object into a dict
create_magic_link_request_dict = create_magic_link_request_instance.to_dict()
# create an instance of CreateMagicLinkRequest from a dict
create_magic_link_request_from_dict = CreateMagicLinkRequest.from_dict(create_magic_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


