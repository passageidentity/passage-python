# MagicLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated** | **bool** |  | 
**app_id** | **str** |  | 
**id** | **str** |  | 
**identifier** | **str** |  | 
**redirect_url** | **str** |  | 
**secret** | **str** |  | 
**ttl** | **int** |  | 
**type** | [**MagicLinkType**](MagicLinkType.md) |  | 
**url** | **str** |  | 
**user_id** | **str** |  | 

## Example

```python
from passageidentity.openapi_client.models.magic_link import MagicLink

# TODO update the JSON string below
json = "{}"
# create an instance of MagicLink from a JSON string
magic_link_instance = MagicLink.from_json(json)
# print the JSON string representation of the object
print MagicLink.to_json()

# convert the object into a dict
magic_link_dict = magic_link_instance.to_dict()
# create an instance of MagicLink from a dict
magic_link_form_dict = magic_link.from_dict(magic_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


