# Task


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of task | [optional] 
**project_id** | **str** | The ID of project which task in | [optional] 
**title** | **str** | Title of task | [optional] 
**is_all_day** | **str** | Is task all day, true or false | [optional] 
**completed_time** | **str** | Task completed time in \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot;, Example \&quot;2019-11-13T03:00:00+0000 | [optional] 
**content** | **str** | Content of task | [optional] 
**desc** | **str** | Description of checklist | [optional] 
**due_date** | **str** | Task due date time in \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot;, Example \&quot;2019-11-13T03:00:00+0000\&quot; | [optional] 
**items** | [**List[ChecklistItem]**](ChecklistItem.md) |  | [optional] 
**priority** | **int** | Task priority, None is 0, Low is 1, Medium is 3, High is 5 | [optional] 
**reminders** | **List[str]** | List of reminder trigger, Example [\&quot;TRIGGER:P0DT9H0M0S\&quot;,\&quot;TRIGGER:PT0S\&quot;] | [optional] 
**repeat_flag** | **str** | Recurring rules of task, Example \&quot;RRULE:FREQ&#x3D;DAILY;INTERVAL&#x3D;1\&quot; | [optional] 
**sort_order** | **int** | Sort order value of task, Example 12345 | [optional] 
**start_date** | **str** | Start data time in \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot;, Example \&quot;2023-04-23T12:00:00+0000\&quot; | [optional] 
**status** | **int** | Task completion status, Normal is 0, Completed is 2 | [optional] 
**time_zone** | **str** | Task timezone, Example \&quot;America/Los_Angeles\&quot; | [optional] 

## Example

```python
from custom_components.ticktick_todo.pyticktick.openapi_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print Task.to_json()

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


