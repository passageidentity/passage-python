# UserMetadataField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | 
**friendly_name** | **str** |  | 
**id** | **str** |  | 
**profile** | **bool** |  | 
**registration** | **bool** |  | 
**type** | [**UserMetadataFieldType**](UserMetadataFieldType.md) |  | 

## Example

```python
from passageidentity.openapi_client.models.user_metadata_field import UserMetadataField

# TODO update the JSON string below
json = "{}"
# create an instance of UserMetadataField from a JSON string
user_metadata_field_instance = UserMetadataField.from_json(json)
# print the JSON string representation of the object
print UserMetadataField.to_json()

# convert the object into a dict
user_metadata_field_dict = user_metadata_field_instance.to_dict()
# create an instance of UserMetadataField from a dict
user_metadata_field_form_dict = user_metadata_field.from_dict(user_metadata_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


