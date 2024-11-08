# OpenV1ProjectProjectIdPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the project | 
**color** | **str** | color of project, eg. \&quot;#F18181\&quot; | [optional] 
**sort_order** | **int** | sort order value of the project | [optional] 
**view_mode** | **str** | view mode, \&quot;list\&quot;, \&quot;kanban\&quot;, \&quot;timeline\&quot; | [optional] 
**kind** | **str** | project kind, \&quot;TASK\&quot;, \&quot;NOTE\&quot; | [optional] 
**project_id** | **str** | project identifier | [optional] 

## Example

```python
from openapi_client.models.open_v1_project_project_id_post_request import OpenV1ProjectProjectIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenV1ProjectProjectIdPostRequest from a JSON string
open_v1_project_project_id_post_request_instance = OpenV1ProjectProjectIdPostRequest.from_json(json)
# print the JSON string representation of the object
print(OpenV1ProjectProjectIdPostRequest.to_json())

# convert the object into a dict
open_v1_project_project_id_post_request_dict = open_v1_project_project_id_post_request_instance.to_dict()
# create an instance of OpenV1ProjectProjectIdPostRequest from a dict
open_v1_project_project_id_post_request_from_dict = OpenV1ProjectProjectIdPostRequest.from_dict(open_v1_project_project_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


