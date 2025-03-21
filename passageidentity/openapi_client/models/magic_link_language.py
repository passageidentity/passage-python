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


class MagicLinkLanguage(str, Enum):
    """
    language of the email or sms to send
    """

    """
    allowed enum values
    """
    DE = 'de'
    EN = 'en'
    ES = 'es'
    IT = 'it'
    PL = 'pl'
    PT = 'pt'
    ZH = 'zh'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MagicLinkLanguage from a JSON string"""
        return cls(json.loads(json_str))


