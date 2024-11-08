# Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the project | 
**color** | **str** | color of project, eg. \&quot;#F18181\&quot; | [optional] 
**sort_order** | **int** | sort order value of the project | [optional] 
**view_mode** | **str** | view mode, \&quot;list\&quot;, \&quot;kanban\&quot;, \&quot;timeline\&quot; | [optional] 
**kind** | **str** | project kind, \&quot;TASK\&quot;, \&quot;NOTE\&quot; | [optional] 

## Example

```python
from openapi_client.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


