# ProjectDataResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**ProjectResponse**](ProjectResponse.md) |  | [optional] 
**tasks** | [**List[TaskResponse]**](TaskResponse.md) |  | [optional] 
**columns** | [**List[Column]**](Column.md) |  | [optional] 

## Example

```python
from custom_components.ticktick_todo.pyticktick.openapi_client.models.project_data_response import ProjectDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataResponse from a JSON string
project_data_response_instance = ProjectDataResponse.from_json(json)
# print the JSON string representation of the object
print ProjectDataResponse.to_json()

# convert the object into a dict
project_data_response_dict = project_data_response_instance.to_dict()
# create an instance of ProjectDataResponse from a dict
project_data_response_from_dict = ProjectDataResponse.from_dict(project_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


