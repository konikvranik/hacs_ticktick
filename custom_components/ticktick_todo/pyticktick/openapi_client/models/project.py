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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Project(BaseModel):
    """
    Project
    """ # noqa: E501
    name: StrictStr = Field(description="name of the project")
    color: Optional[StrictStr] = Field(default=None, description="color of project, eg. \"#F18181\"")
    sort_order: Optional[StrictInt] = Field(default=None, description="sort order value of the project", alias="sortOrder")
    view_mode: Optional[StrictStr] = Field(default=None, description="view mode, \"list\", \"kanban\", \"timeline\"", alias="viewMode")
    kind: Optional[StrictStr] = Field(default=None, description="project kind, \"TASK\", \"NOTE\"")
    __properties: ClassVar[List[str]] = ["name", "color", "sortOrder", "viewMode", "kind"]

    @field_validator('view_mode')
    def view_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['list', 'kanban', 'timeline']):
            raise ValueError("must be one of enum values ('list', 'kanban', 'timeline')")
        return value

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['TASK', 'NOTE']):
            raise ValueError("must be one of enum values ('TASK', 'NOTE')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Project from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Project from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "color": obj.get("color"),
            "sortOrder": obj.get("sortOrder"),
            "viewMode": obj.get("viewMode"),
            "kind": obj.get("kind")
        })
        return _obj


