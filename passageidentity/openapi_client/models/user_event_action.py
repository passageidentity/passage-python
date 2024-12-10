# coding: utf-8

"""
    Passage Management API

    Passage's management API to manage your Passage apps and users.

    The version of the OpenAPI document: 1
    Contact: support@passage.id
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UserEventAction(str, Enum):
    """
    UserEventAction
    """

    """
    allowed enum values
    """
    REGISTER = 'register'
    LOGIN = 'login'
    OTHER = 'other'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserEventAction from a JSON string"""
        return cls(json.loads(json_str))

