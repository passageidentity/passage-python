# ListPaginatedUsersItem


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
**status** | [**UserStatus**](UserStatus.md) |  | 
**updated_at** | **datetime** |  | 
**user_metadata** | **object** |  | 

## Example

```python
from passageidentity.openapi_client.models.list_paginated_users_item import ListPaginatedUsersItem

# TODO update the JSON string below
json = "{}"
# create an instance of ListPaginatedUsersItem from a JSON string
list_paginated_users_item_instance = ListPaginatedUsersItem.from_json(json)
# print the JSON string representation of the object
print ListPaginatedUsersItem.to_json()

# convert the object into a dict
list_paginated_users_item_dict = list_paginated_users_item_instance.to_dict()
# create an instance of ListPaginatedUsersItem from a dict
list_paginated_users_item_form_dict = list_paginated_users_item.from_dict(list_paginated_users_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


