# coding: utf-8

"""
    TickTick API

    [TickTick](https://ticktick.com/) TODO task manager.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest(BaseModel):
    """
    OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest
    """
    project_id: Optional[StrictStr] = Field(default=None, alias="projectId")
    task_id: Optional[StrictStr] = Field(default=None, alias="taskId")
    __properties = ["projectId", "taskId"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest:
        """Create an instance of OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest:
        """Create an instance of OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest.parse_obj(obj)

        _obj = OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest.parse_obj({
            "project_id": obj.get("projectId"),
            "task_id": obj.get("taskId")
        })
        return _obj


