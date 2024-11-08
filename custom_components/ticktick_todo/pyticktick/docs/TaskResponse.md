# TaskResponse


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
**id** | **str** | Task identifier | [optional] 
**project_id** | **str** | Task project id | [optional] 
**completed_time** | [**TaskResponseAllOfCompletedTime**](TaskResponseAllOfCompletedTime.md) |  | [optional] 
**status** | [**TaskResponseAllOfStatus**](TaskResponseAllOfStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.task_response import TaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResponse from a JSON string
task_response_instance = TaskResponse.from_json(json)
# print the JSON string representation of the object
print(TaskResponse.to_json())

# convert the object into a dict
task_response_dict = task_response_instance.to_dict()
# create an instance of TaskResponse from a dict
task_response_from_dict = TaskResponse.from_dict(task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


