# Nonce

the nonce to exchange for an authentication token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** |  | 

## Example

```python
from passageidentity.openapi_client.models.nonce import Nonce

# TODO update the JSON string below
json = "{}"
# create an instance of Nonce from a JSON string
nonce_instance = Nonce.from_json(json)
# print the JSON string representation of the object
print Nonce.to_json()

# convert the object into a dict
nonce_dict = nonce_instance.to_dict()
# create an instance of Nonce from a dict
nonce_form_dict = nonce.from_dict(nonce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


