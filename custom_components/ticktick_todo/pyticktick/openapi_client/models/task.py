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


from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from custom_components.ticktick_todo.pyticktick.openapi_client.models.checklist_item import ChecklistItem

class Task(BaseModel):
    """
    Task
    """
    title: Optional[StrictStr] = Field(default=None, description="Task title")
    is_all_day: Optional[StrictBool] = Field(default=None, alias="isAllDay", description="All day")
    content: Optional[StrictStr] = Field(default=None, description="Task content")
    desc: Optional[StrictStr] = Field(default=None, description="Task description of checklist")
    due_date: Optional[Any] = Field(default=None, alias="dueDate")
    items: Optional[conlist(ChecklistItem)] = Field(default=None, description="Subtasks of Task")
    priority: Optional[StrictInt] = Field(default=None, description="Task priority")
    reminders: Optional[conlist(StrictStr)] = Field(default=None, description="List of reminder triggers")
    repeat_flag: Optional[StrictStr] = Field(default=None, alias="repeatFlag", description="Recurring rules of task")
    sort_order: Optional[StrictInt] = Field(default=None, alias="sortOrder", description="Task sort order")
    start_date: Optional[Any] = Field(default=None, alias="startDate")
    time_zone: Optional[Any] = Field(default=None, alias="timeZone")
    __properties = ["title", "isAllDay", "content", "desc", "dueDate", "items", "priority", "reminders", "repeatFlag", "sortOrder", "startDate", "timeZone"]

    @validator('priority')
    def priority_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (null, null, null, null, null, null):
            raise ValueError("must be one of enum values (null, null, null, null, null, null)")
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
    def from_json(cls, json_str: str) -> Task:
        """Create an instance of Task from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Task:
        """Create an instance of Task from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Task.parse_obj(obj)

        _obj = Task.parse_obj({
            "title": obj.get("title"),
            "is_all_day": obj.get("isAllDay"),
            "content": obj.get("content"),
            "desc": obj.get("desc"),
            "due_date": obj.get("dueDate"),
            "items": [ChecklistItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "priority": obj.get("priority"),
            "reminders": obj.get("reminders"),
            "repeat_flag": obj.get("repeatFlag"),
            "sort_order": obj.get("sortOrder"),
            "start_date": obj.get("startDate"),
            "time_zone": obj.get("timeZone")
        })
        return _obj


