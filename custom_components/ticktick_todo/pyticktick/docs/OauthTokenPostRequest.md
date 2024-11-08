# OauthTokenPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** | The code obtained in the second step | [optional] 
**grant_type** | **object** | grant type, now only authorization_code | [optional] 
**scope** | **object** | spaces-separated permission scope. The currently available scopes are tasks:write, tasks:read | [optional] 
**redirect_uri** | **object** | user-configured redirect url | [optional] 

## Example

```python
from openapi_client.models.oauth_token_post_request import OauthTokenPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OauthTokenPostRequest from a JSON string
oauth_token_post_request_instance = OauthTokenPostRequest.from_json(json)
# print the JSON string representation of the object
print(OauthTokenPostRequest.to_json())

# convert the object into a dict
oauth_token_post_request_dict = oauth_token_post_request_instance.to_dict()
# create an instance of OauthTokenPostRequest from a dict
oauth_token_post_request_from_dict = OauthTokenPostRequest.from_dict(oauth_token_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


