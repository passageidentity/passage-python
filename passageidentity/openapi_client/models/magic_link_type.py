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


class MagicLinkType(str, Enum):
    """
    The type of magic link to create: \"login\" or \"verify_identifier\". Defaults to \"login\".
    """

    """
    allowed enum values
    """
    LOGIN = 'login'
    VERIFY_IDENTIFIER = 'verify_identifier'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MagicLinkType from a JSON string"""
        return cls(json.loads(json_str))


