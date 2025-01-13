# custom_components.ticktick_todo.pyticktick.openapi_client.DefaultApi

All URIs are relative to *https://ticktick.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_specify_task**](DefaultApi.md#complete_specify_task) | **POST** /open/v1/project/{projectId}/task/{taskId}/complete | Complete a task by project ID and task ID
[**create_single_task**](DefaultApi.md#create_single_task) | **POST** /open/v1/task | Create a task to TickTick
[**delete_specify_task**](DefaultApi.md#delete_specify_task) | **DELETE** /open/v1/project/{projectId}/task/{taskId} | Delete a task by project ID and task ID
[**get_all_projects**](DefaultApi.md#get_all_projects) | **GET** /open/v1/project | Get the list of projects
[**get_project_by_id**](DefaultApi.md#get_project_by_id) | **GET** /open/v1/project/{projectId} | Get a project by ID
[**get_project_with_data_by_id**](DefaultApi.md#get_project_with_data_by_id) | **GET** /open/v1/project/{projectId}/data | Get project with data by ID


# **complete_specify_task**
> complete_specify_task(project_id, task_id)

Complete a task by project ID and task ID

### Example

```python
import time
import os
import custom_components.ticktick_todo.pyticktick.openapi_client
from custom_components.ticktick_todo.pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = custom_components.ticktick_todo.pyticktick.openapi_client.Configuration(
    host = "https://ticktick.com"
)


# Enter a context with an instance of the API client
async with custom_components.ticktick_todo.pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = custom_components.ticktick_todo.pyticktick.openapi_client.DefaultApi(api_client)
    project_id = 'project_id_example' # str | The ID of project which task in
    task_id = 'task_id_example' # str | The ID of task

    try:
        # Complete a task by project ID and task ID
        await api_instance.complete_specify_task(project_id, task_id)
    except Exception as e:
        print("Exception when calling DefaultApi->complete_specify_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of project which task in | 
 **task_id** | **str**| The ID of task | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_single_task**
> Task create_single_task(task=task)

Create a task to TickTick

### Example

```python
import time
import os
import custom_components.ticktick_todo.pyticktick.openapi_client
from custom_components.ticktick_todo.pyticktick.openapi_client.models.task import Task
from custom_components.ticktick_todo.pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = custom_components.ticktick_todo.pyticktick.openapi_client.Configuration(
    host = "https://ticktick.com"
)


# Enter a context with an instance of the API client
async with custom_components.ticktick_todo.pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = custom_components.ticktick_todo.pyticktick.openapi_client.DefaultApi(api_client)
    task = {"title":"new task title"} # Task | New task info (optional)

    try:
        # Create a task to TickTick
        api_response = await api_instance.create_single_task(task=task)
        print("The response of DefaultApi->create_single_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_single_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task** | [**Task**](Task.md)| New task info | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_specify_task**
> delete_specify_task(project_id, task_id)

Delete a task by project ID and task ID

### Example

```python
import time
import os
import custom_components.ticktick_todo.pyticktick.openapi_client
from custom_components.ticktick_todo.pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = custom_components.ticktick_todo.pyticktick.openapi_client.Configuration(
    host = "https://ticktick.com"
)


# Enter a context with an instance of the API client
async with custom_components.ticktick_todo.pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = custom_components.ticktick_todo.pyticktick.openapi_client.DefaultApi(api_client)
    project_id = 'project_id_example' # str | The ID of project which task in
    task_id = 'task_id_example' # str | The ID of task

    try:
        # Delete a task by project ID and task ID
        await api_instance.delete_specify_task(project_id, task_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_specify_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of project which task in | 
 **task_id** | **str**| The ID of task | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects**
> List[Project] get_all_projects()

Get the list of projects

### Example

```python
import time
import os
import custom_components.ticktick_todo.pyticktick.openapi_client
from custom_components.ticktick_todo.pyticktick.openapi_client.models.project import Project
from custom_components.ticktick_todo.pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = custom_components.ticktick_todo.pyticktick.openapi_client.Configuration(
    host = "https://ticktick.com"
)


# Enter a context with an instance of the API client
async with custom_components.ticktick_todo.pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = custom_components.ticktick_todo.pyticktick.openapi_client.DefaultApi(api_client)

    try:
        # Get the list of projects
        api_response = await api_instance.get_all_projects()
        print("The response of DefaultApi->get_all_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_projects: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_id**
> Project get_project_by_id(project_id)

Get a project by ID

### Example

```python
import time
import os
import custom_components.ticktick_todo.pyticktick.openapi_client
from custom_components.ticktick_todo.pyticktick.openapi_client.models.project import Project
from custom_components.ticktick_todo.pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = custom_components.ticktick_todo.pyticktick.openapi_client.Configuration(
    host = "https://ticktick.com"
)


# Enter a context with an instance of the API client
async with custom_components.ticktick_todo.pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = custom_components.ticktick_todo.pyticktick.openapi_client.DefaultApi(api_client)
    project_id = 'project_id_example' # str | The ID of project.

    try:
        # Get a project by ID
        api_response = await api_instance.get_project_by_id(project_id)
        print("The response of DefaultApi->get_project_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of project. | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_with_data_by_id**
> ProjectData get_project_with_data_by_id(project_id)

Get project with data by ID

### Example

```python
import time
import os
import custom_components.ticktick_todo.pyticktick.openapi_client
from custom_components.ticktick_todo.pyticktick.openapi_client.models.project_data import ProjectData
from custom_components.ticktick_todo.pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = custom_components.ticktick_todo.pyticktick.openapi_client.Configuration(
    host = "https://ticktick.com"
)


# Enter a context with an instance of the API client
async with custom_components.ticktick_todo.pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = custom_components.ticktick_todo.pyticktick.openapi_client.DefaultApi(api_client)
    project_id = 'project_id_example' # str | The ID of project.

    try:
        # Get project with data by ID
        api_response = await api_instance.get_project_with_data_by_id(project_id)
        print("The response of DefaultApi->get_project_with_data_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_with_data_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of project. | 

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

