# ProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the project | 
**color** | **str** | color of project, eg. \&quot;#F18181\&quot; | [optional] 
**sort_order** | **int** | sort order value of the project | [optional] 
**view_mode** | **str** | view mode, \&quot;list\&quot;, \&quot;kanban\&quot;, \&quot;timeline\&quot; | [optional] 
**kind** | **str** | project kind, \&quot;TASK\&quot;, \&quot;NOTE\&quot; | [optional] 
**id** | **str** | Project identifier | [optional] 
**closed** | **bool** | Project closed | [optional] 
**group_id** | **str** | Project group identifier | [optional] 
**permission** | **str** | \&quot;read\&quot;, \&quot;write\&quot; or \&quot;comment\&quot; | [optional] 

## Example

```python
from openapi_client.models.project_response import ProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResponse from a JSON string
project_response_instance = ProjectResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectResponse.to_json())

# convert the object into a dict
project_response_dict = project_response_instance.to_dict()
# create an instance of ProjectResponse from a dict
project_response_from_dict = ProjectResponse.from_dict(project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


