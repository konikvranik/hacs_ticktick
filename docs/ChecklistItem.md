# ChecklistItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of checklistItem | [optional] 
**title** | **str** | Title of checklistItem | [optional] 
**status** | **int** | The completion status of checklistItem, Normal is 0, Completed is 1 | [optional] 
**completed_time** | **str** | checklistItem completed time in \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot;, Example \&quot;2019-11-13T03:00:00+0000 | [optional] 
**is_all_day** | **str** | Is checklistItem all day, true or false | [optional] 
**sort_order** | **int** | Order value of checklistItem | [optional] 
**start_date** | **str** | checklistItem start date time in \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot;, Example \&quot;2019-11-13T03:00:00+0000\&quot; | [optional] 
**time_zone** | **str** | checklistItem timezone, Example \&quot;America/Los_Angeles\&quot; | [optional] 

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


