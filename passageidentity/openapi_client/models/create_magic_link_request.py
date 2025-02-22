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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from passageidentity.openapi_client.models.magic_link_channel import MagicLinkChannel
from passageidentity.openapi_client.models.magic_link_language import MagicLinkLanguage
from passageidentity.openapi_client.models.magic_link_type import MagicLinkType
from typing import Optional, Set
from typing_extensions import Self

class CreateMagicLinkRequest(BaseModel):
    """
    CreateMagicLinkRequest
    """ # noqa: E501
    channel: Optional[MagicLinkChannel] = None
    email: Optional[StrictStr] = None
    language: Optional[MagicLinkLanguage] = None
    magic_link_path: Optional[StrictStr] = Field(default=None, description="must be a relative url")
    phone: Optional[StrictStr] = None
    redirect_url: Optional[StrictStr] = None
    send: Optional[StrictBool] = None
    ttl: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="time to live in minutes")
    type: Optional[MagicLinkType] = None
    user_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["channel", "email", "language", "magic_link_path", "phone", "redirect_url", "send", "ttl", "type", "user_id"]

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
        """Create an instance of CreateMagicLinkRequest from a JSON string"""
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
        """Create an instance of CreateMagicLinkRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "channel": obj.get("channel"),
            "email": obj.get("email"),
            "language": obj.get("language"),
            "magic_link_path": obj.get("magic_link_path"),
            "phone": obj.get("phone"),
            "redirect_url": obj.get("redirect_url"),
            "send": obj.get("send"),
            "ttl": obj.get("ttl"),
            "type": obj.get("type"),
            "user_id": obj.get("user_id")
        })
        return _obj


