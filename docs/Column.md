# Column


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of column | [optional] 
**project_id** | **str** | The ID of project which column in | [optional] 
**name** | **str** | Name of column | [optional] 
**sort_order** | **int** | Order value of column | [optional] 

## Example

```python
from custom_components.ticktick_todo.pyticktick.openapi_client.models.column import Column

# TODO update the JSON string below
json = "{}"
# create an instance of Column from a JSON string
column_instance = Column.from_json(json)
# print the JSON string representation of the object
print Column.to_json()

# convert the object into a dict
column_dict = column_instance.to_dict()
# create an instance of Column from a dict
column_from_dict = Column.from_dict(column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


