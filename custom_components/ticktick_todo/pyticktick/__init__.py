import openapi
from openapi_core import OpenAPI
from pyopenapi import Specification

openapi = OpenAPI.from_file_path('openapi.yaml')

result = openapi.unmarshal_request(request)



