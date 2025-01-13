# Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of project | [optional] 
**name** | **str** | Name of project | [optional] 
**color** | **str** | Color of project | [optional] 
**sort_order** | **int** | Order value of project | [optional] 
**closed** | **str** | Project closed, true or false | [optional] 
**group_id** | **str** | ID of project group | [optional] 
**view_mode** | **str** | View mode of project, \&quot;list\&quot; or \&quot;kanban\&quot; or \&quot;timeline\&quot; | [optional] 
**permission** | **str** | Permission of project, \&quot;read\&quot; or \&quot;write\&quot; or \&quot;comment\&quot; | [optional] 
**kind** | **str** | Kind of project, \&quot;Task\&quot; or \&quot;NOTE\&quot; | [optional] 

## Example

```python
from custom_components.ticktick_todo.pyticktick.openapi_client.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print Project.to_json()

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


