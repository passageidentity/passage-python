# ListPaginatedUsersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | 
**created_before** | **int** | time anchor (Unix timestamp) --&gt; all users returned created before this timestamp | 
**limit** | **int** |  | 
**page** | **int** |  | 
**total_users** | **int** | total number of users for a particular query | 
**users** | [**List[ListPaginatedUsersItem]**](ListPaginatedUsersItem.md) |  | 

## Example

```python
from passageidentity.openapi_client.models.list_paginated_users_response import ListPaginatedUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPaginatedUsersResponse from a JSON string
list_paginated_users_response_instance = ListPaginatedUsersResponse.from_json(json)
# print the JSON string representation of the object
print ListPaginatedUsersResponse.to_json()

# convert the object into a dict
list_paginated_users_response_dict = list_paginated_users_response_instance.to_dict()
# create an instance of ListPaginatedUsersResponse from a dict
list_paginated_users_response_form_dict = list_paginated_users_response.from_dict(list_paginated_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


