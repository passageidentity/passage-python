# ElementCustomization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passage_container_background_color** | **str** | Container background color in hex. Default is &#x60;#ffffff&#x60; in light mode &amp; &#x60;#383838&#x60; in dark mode.  | [optional] 
**passage_container_max_width** | **int** | Maximum width of container (px) | [optional] [default to 300]
**passage_input_box_background_color** | **str** | Input box background color in hex. Default is &#x60;#ffffff&#x60; in light mode &amp; &#x60;#4b4b4b&#x60; in dark mode.  | [optional] 
**passage_input_box_border_radius** | **int** | Input box border radius (px) | [optional] [default to 5]
**passage_header_font_family** | [**FontFamily**](FontFamily.md) |  | [optional] 
**passage_body_font_family** | [**FontFamily**](FontFamily.md) |  | [optional] 
**passage_header_text_color** | **str** | Header text color in hex. Default is &#x60;#222222&#x60; in light mode &amp; &#x60;#f3f3f3&#x60; in dark mode.  | [optional] 
**passage_body_text_color** | **str** | Body text color in hex. Default is &#x60;#222222&#x60; in light mode &amp; &#x60;#f3f3f3&#x60; in dark mode.  | [optional] 
**passage_primary_button_background_color** | **str** | Primary button background colour (hex) | [optional] [default to '#121212']
**passage_primary_button_text_color** | **str** | Primary button font colour (hex) | [optional] [default to '#f3f3f3']
**passage_primary_button_hover_color** | **str** | Primary button background on hover (hex) | [optional] [default to '#4d4d4d']
**passage_primary_button_border_radius** | **int** | Primary button border radius (px) | [optional] [default to 5]
**passage_primary_button_border_color** | **str** | Primary button border color | [optional] [default to '#121212']
**passage_primary_button_border_width** | **int** | Primary button border width (px) | [optional] [default to 0]
**passage_secondary_button_background_color** | **str** | Secondary button background colour (hex) | [optional] [default to '#ffffff']
**passage_secondary_button_text_color** | **str** | Secondary button font colour (hex) | [optional] [default to '#222222']
**passage_secondary_button_hover_color** | **str** | Secondary button background on hover (hex) | [optional] [default to '#d7d7d7']
**passage_secondary_button_border_radius** | **int** | Secondary button border radius (px) | [optional] [default to 5]
**passage_secondary_button_border_color** | **str** | Secondary button border color | [optional] [default to '#d7d7d7']
**passage_secondary_button_border_width** | **int** | Secondary button border width (px) | [optional] [default to 1]

## Example

```python
from openapi_client.models.element_customization import ElementCustomization

# TODO update the JSON string below
json = "{}"
# create an instance of ElementCustomization from a JSON string
element_customization_instance = ElementCustomization.from_json(json)
# print the JSON string representation of the object
print ElementCustomization.to_json()

# convert the object into a dict
element_customization_dict = element_customization_instance.to_dict()
# create an instance of ElementCustomization from a dict
element_customization_form_dict = element_customization.from_dict(element_customization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


