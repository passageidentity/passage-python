# GoogleSocialConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The external ID of the Social Connection. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.google_social_connection import GoogleSocialConnection

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSocialConnection from a JSON string
google_social_connection_instance = GoogleSocialConnection.from_json(json)
# print the JSON string representation of the object
print GoogleSocialConnection.to_json()

# convert the object into a dict
google_social_connection_dict = google_social_connection_instance.to_dict()
# create an instance of GoogleSocialConnection from a dict
google_social_connection_form_dict = google_social_connection.from_dict(google_social_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


