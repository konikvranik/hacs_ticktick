# coding: utf-8

"""
    TickTick API

    [TickTick](https://ticktick.com/) TODO task manager.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import json
import re  # noqa: F401
import custom_components

from aenum import Enum

class Status(int, Enum):
    """
    Task completion status
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_2 = 2

    @classmethod
    def from_json(cls, json_str: str) -> Status:
        """Create an instance of Status from a JSON string"""
        return Status(json.loads(json_str))
