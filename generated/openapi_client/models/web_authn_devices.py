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

from datetime import datetime
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.web_authn_icons import WebAuthnIcons
from openapi_client.models.web_authn_type import WebAuthnType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WebAuthnDevices(BaseModel):
    """
    WebAuthnDevices
    """ # noqa: E501
    created_at: datetime = Field(description="The first time this webAuthn device was used to authenticate the user")
    cred_id: StrictStr = Field(description="The CredID for this webAuthn device")
    friendly_name: StrictStr = Field(description="The friendly name for the webAuthn device used to authenticate")
    id: StrictStr = Field(description="The ID of the webAuthn device used for authentication")
    last_login_at: datetime = Field(description="The last time this webAuthn device was used to authenticate the user")
    type: WebAuthnType
    updated_at: datetime = Field(description="The last time this webAuthn device was updated")
    usage_count: StrictInt = Field(description="How many times this webAuthn device has been used to authenticate the user")
    icons: WebAuthnIcons
    __properties: ClassVar[List[str]] = ["created_at", "cred_id", "friendly_name", "id", "last_login_at", "type", "updated_at", "usage_count", "icons"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WebAuthnDevices from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of icons
        if self.icons:
            _dict['icons'] = self.icons.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WebAuthnDevices from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "cred_id": obj.get("cred_id"),
            "friendly_name": obj.get("friendly_name"),
            "id": obj.get("id"),
            "last_login_at": obj.get("last_login_at"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "usage_count": obj.get("usage_count"),
            "icons": WebAuthnIcons.from_dict(obj.get("icons")) if obj.get("icons") is not None else None
        })
        return _obj


