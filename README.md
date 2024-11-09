# custom-components.ticktick-todo.pyticktick.openapi-client
[TickTick](https://ticktick.com/) TODO task manager.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Generator version: 7.7.0
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import custom_components.ticktick_todo.pyticktick.openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import custom_components.ticktick_todo.pyticktick.openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import custom_components.ticktick_todo.pyticktick.openapi_client
from custom_components.ticktick_todo.pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = custom_components.ticktick_todo.pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = custom_components.ticktick_todo.pyticktick.openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)


# Enter a context with an instance of the API client
with custom_components.ticktick_todo.pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = custom_components.ticktick_todo.pyticktick.openapi_client.DefaultApi(api_client)
    oauth_token_post_request = custom_components.ticktick_todo.pyticktick.openapi_client.OauthTokenPostRequest() # OauthTokenPostRequest |  (optional)

    try:
        # Get token
        api_response = api_instance.oauth_token_post(oauth_token_post_request=oauth_token_post_request)
        print("The response of DefaultApi->oauth_token_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->oauth_token_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.ticktick.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**oauth_token_post**](docs/DefaultApi.md#oauth_token_post) | **POST** /oauth/token | Get token
*DefaultApi* | [**open_v1_project_get**](docs/DefaultApi.md#open_v1_project_get) | **GET** /open/v1/project | Get User Project.
*DefaultApi* | [**open_v1_project_post**](docs/DefaultApi.md#open_v1_project_post) | **POST** /open/v1/project | Create Project
*DefaultApi* | [**open_v1_project_project_id_data_get**](docs/DefaultApi.md#open_v1_project_project_id_data_get) | **GET** /open/v1/project/{projectId}/data | 
*DefaultApi* | [**open_v1_project_project_id_delete**](docs/DefaultApi.md#open_v1_project_project_id_delete) | **DELETE** /open/v1/project/{projectId} | 
*DefaultApi* | [**open_v1_project_project_id_get**](docs/DefaultApi.md#open_v1_project_project_id_get) | **GET** /open/v1/project/{projectId} | 
*DefaultApi* | [**open_v1_project_project_id_post**](docs/DefaultApi.md#open_v1_project_project_id_post) | **POST** /open/v1/project/{projectId} | Update Project
*DefaultApi* | [**open_v1_project_project_id_task_task_id_complete_post**](docs/DefaultApi.md#open_v1_project_project_id_task_task_id_complete_post) | **POST** /open/v1/project/{projectId}/task/{taskId}/complete | Update Task
*DefaultApi* | [**open_v1_project_project_id_task_task_id_delete**](docs/DefaultApi.md#open_v1_project_project_id_task_task_id_delete) | **DELETE** /open/v1/project/{projectId}/task/{taskId} | Delete task.
*DefaultApi* | [**open_v1_project_project_id_task_task_id_get**](docs/DefaultApi.md#open_v1_project_project_id_task_task_id_get) | **GET** /open/v1/project/{projectId}/task/{taskId} | Get Task By Project ID And Task ID.
*DefaultApi* | [**open_v1_task_post**](docs/DefaultApi.md#open_v1_task_post) | **POST** /open/v1/task | Create Task
*DefaultApi* | [**open_v1_task_task_id_post**](docs/DefaultApi.md#open_v1_task_task_id_post) | **POST** /open/v1/task/{taskId} | Update Task


## Documentation For Models

 - [ChecklistItem](docs/ChecklistItem.md)
 - [Column](docs/Column.md)
 - [OauthTokenPost200Response](docs/OauthTokenPost200Response.md)
 - [OauthTokenPostRequest](docs/OauthTokenPostRequest.md)
 - [OpenV1ProjectProjectIdPostRequest](docs/OpenV1ProjectProjectIdPostRequest.md)
 - [OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest](docs/OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest.md)
 - [OpenV1TaskTaskIdPostRequest](docs/OpenV1TaskTaskIdPostRequest.md)
 - [Project](docs/Project.md)
 - [ProjectDataResponse](docs/ProjectDataResponse.md)
 - [ProjectResponse](docs/ProjectResponse.md)
 - [Status](docs/Status.md)
 - [Task](docs/Task.md)
 - [TaskResponse](docs/TaskResponse.md)
 - [TaskResponseAllOfCompletedTime](docs/TaskResponseAllOfCompletedTime.md)
 - [TaskResponseAllOfStatus](docs/TaskResponseAllOfStatus.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BasicAuth"></a>
### BasicAuth

- **Type**: HTTP basic authentication

<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication

<a id="OAuth2"></a>
### OAuth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://ticktick.com/oauth/authorize?scope={scope}&client_id={client_id}&state={state}&redirect_uri={redirect_uri}&response_type=code
- **Scopes**: 
 - **tasks:write**: 
 - **tasks:read**: 


## Author




