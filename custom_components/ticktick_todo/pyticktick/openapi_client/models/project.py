# coding: utf-8

"""
    TickTick API

    [TickTick](https://ticktick.com/) TODO task manager.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Optional

from pydantic import BaseModel, Field, StrictInt, StrictStr, validator


class Project(BaseModel):
    """
    Project
    """
    name: StrictStr = Field(default=..., description="name of the project")
    color: Optional[StrictStr] = Field(default=None, description="color of project, eg. \"#F18181\"")
    sort_order: Optional[StrictInt] = Field(default=None, alias="sortOrder", description="sort order value of the project")
    view_mode: Optional[StrictStr] = Field(default=None, alias="viewMode", description="view mode, \"list\", \"kanban\", \"timeline\"")
    kind: Optional[StrictStr] = Field(default=None, description="project kind, \"TASK\", \"NOTE\"")
    __properties = ["name", "color", "sortOrder", "viewMode", "kind"]

    @validator('view_mode')
    def view_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('list', 'kanban', 'timeline'):
            raise ValueError("must be one of enum values ('list', 'kanban', 'timeline')")
        return value

    @validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('TASK', 'NOTE'):
            raise ValueError("must be one of enum values ('TASK', 'NOTE')")
        return value

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
    def from_json(cls, json_str: str) -> Project:
        """Create an instance of Project from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Project:
        """Create an instance of Project from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Project.parse_obj(obj)

        _obj = Project.parse_obj({
            "name": obj.get("name"),
            "color": obj.get("color"),
            "sort_order": obj.get("sortOrder"),
            "view_mode": obj.get("viewMode"),
            "kind": obj.get("kind")
        })
        return _obj


