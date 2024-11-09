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
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator

from custom_components.ticktick_todo.pyticktick.openapi_client.models.checklist_item import ChecklistItem
from custom_components.ticktick_todo.pyticktick.openapi_client.models.task_response_all_of_completed_time import \
    TaskResponseAllOfCompletedTime
from custom_components.ticktick_todo.pyticktick.openapi_client.models.task_response_all_of_status import \
    TaskResponseAllOfStatus


class OpenV1TaskTaskIdPostRequest(BaseModel):
    """
    OpenV1TaskTaskIdPostRequest
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
    id: Optional[StrictStr] = Field(default=None, description="Task identifier")
    project_id: Optional[StrictStr] = Field(default=None, alias="projectId", description="Task project id")
    completed_time: Optional[TaskResponseAllOfCompletedTime] = Field(default=None, alias="completedTime")
    status: Optional[TaskResponseAllOfStatus] = None
    task_id: Optional[StrictStr] = Field(default=None, alias="taskId", description="Task identifier")
    additional_properties: Dict[str, Any] = {}
    __properties = ["title", "isAllDay", "content", "desc", "dueDate", "items", "priority", "reminders", "repeatFlag",
                    "sortOrder", "startDate", "timeZone", "id", "projectId", "completedTime", "status", "taskId"]

    @validator('priority')
    def priority_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (None, None, None, None, None, None):
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
    def from_json(cls, json_str: str) -> OpenV1TaskTaskIdPostRequest:
        """Create an instance of OpenV1TaskTaskIdPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                              "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of completed_time
        if self.completed_time:
            _dict['completedTime'] = self.completed_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OpenV1TaskTaskIdPostRequest:
        """Create an instance of OpenV1TaskTaskIdPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OpenV1TaskTaskIdPostRequest.parse_obj(obj)

        _obj = OpenV1TaskTaskIdPostRequest.parse_obj({
            "title": obj.get("title"),
            "is_all_day": obj.get("isAllDay"),
            "content": obj.get("content"),
            "desc": obj.get("desc"),
            "due_date": obj.get("dueDate"),
            "items": [ChecklistItem.from_dict(_item) for _item in obj.get("items")] if obj.get(
                "items") is not None else None,
            "priority": obj.get("priority"),
            "reminders": obj.get("reminders"),
            "repeat_flag": obj.get("repeatFlag"),
            "sort_order": obj.get("sortOrder"),
            "start_date": obj.get("startDate"),
            "time_zone": obj.get("timeZone"),
            "id": obj.get("id"),
            "project_id": obj.get("projectId"),
            "completed_time": TaskResponseAllOfCompletedTime.from_dict(obj.get("completedTime")) if obj.get(
                "completedTime") is not None else None,
            "status": TaskResponseAllOfStatus.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "task_id": obj.get("taskId")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
