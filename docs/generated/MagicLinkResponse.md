# MagicLinkResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**magic_link** | [**MagicLink**](MagicLink.md) |  | 

## Example

```python
from openapi_client.models.magic_link_response import MagicLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MagicLinkResponse from a JSON string
magic_link_response_instance = MagicLinkResponse.from_json(json)
# print the JSON string representation of the object
print MagicLinkResponse.to_json()

# convert the object into a dict
magic_link_response_dict = magic_link_response_instance.to_dict()
# create an instance of MagicLinkResponse from a dict
magic_link_response_form_dict = magic_link_response.from_dict(magic_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


