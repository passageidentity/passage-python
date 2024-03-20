# PaginatedLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | [**Link**](Link.md) |  | 
**last** | [**Link**](Link.md) |  | 
**next** | [**Link**](Link.md) |  | 
**previous** | [**Link**](Link.md) |  | 
**var_self** | [**Link**](Link.md) |  | 

## Example

```python
from passageidentity.openapi_client.models.paginated_links import PaginatedLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLinks from a JSON string
paginated_links_instance = PaginatedLinks.from_json(json)
# print the JSON string representation of the object
print PaginatedLinks.to_json()

# convert the object into a dict
paginated_links_dict = paginated_links_instance.to_dict()
# create an instance of PaginatedLinks from a dict
paginated_links_form_dict = paginated_links.from_dict(paginated_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


