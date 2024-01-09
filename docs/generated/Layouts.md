# Layouts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**List[LayoutConfig]**](LayoutConfig.md) |  | 
**registration** | [**List[LayoutConfig]**](LayoutConfig.md) |  | 

## Example

```python
from passageidentity.openapi_client.models.layouts import Layouts

# TODO update the JSON string below
json = "{}"
# create an instance of Layouts from a JSON string
layouts_instance = Layouts.from_json(json)
# print the JSON string representation of the object
print Layouts.to_json()

# convert the object into a dict
layouts_dict = layouts_instance.to_dict()
# create an instance of Layouts from a dict
layouts_form_dict = layouts.from_dict(layouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


