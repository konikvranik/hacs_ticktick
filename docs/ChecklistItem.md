# ChecklistItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subtask identifier | [optional] 
**title** | **str** | Subtask title | [optional] 
**status** | **object** |  | [optional] 
**completed_time** | **datetime** | Subtask completed time in \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot; | [optional] 
**is_all_day** | **bool** | All day | [optional] 
**sort_order** | **int** | Subtask sort order | [optional] 
**start_date** | **datetime** | Subtask start date time in \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot; | [optional] 
**time_zone** | **object** |  | [optional] 

## Example

```python
from custom_components.ticktick_todo.pyticktick.openapi_client.models.checklist_item import ChecklistItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItem from a JSON string
checklist_item_instance = ChecklistItem.from_json(json)
# print the JSON string representation of the object
print ChecklistItem.to_json()

# convert the object into a dict
checklist_item_dict = checklist_item_instance.to_dict()
# create an instance of ChecklistItem from a dict
checklist_item_from_dict = ChecklistItem.from_dict(checklist_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


