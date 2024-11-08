# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Task title | [optional] 
**is_all_day** | **bool** | All day | [optional] 
**content** | **str** | Task content | [optional] 
**desc** | **str** | Task description of checklist | [optional] 
**due_date** | **object** |  | [optional] 
**items** | [**List[ChecklistItem]**](ChecklistItem.md) | Subtasks of Task | [optional] 
**priority** | **int** | Task priority | [optional] 
**reminders** | **List[str]** | List of reminder triggers | [optional] 
**repeat_flag** | **str** | Recurring rules of task | [optional] 
**sort_order** | **int** | Task sort order | [optional] 
**start_date** | **object** |  | [optional] 
**time_zone** | **object** |  | [optional] 

## Example

```python
from custom_components.ticktick_todo.pyticktick.openapi_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


