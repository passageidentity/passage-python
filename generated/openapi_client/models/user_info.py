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
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.user_event_info import UserEventInfo
from openapi_client.models.user_social_connections import UserSocialConnections
from openapi_client.models.user_status import UserStatus
from openapi_client.models.web_authn_devices import WebAuthnDevices
from openapi_client.models.web_authn_type import WebAuthnType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UserInfo(BaseModel):
    """
    UserInfo
    """ # noqa: E501
    created_at: datetime
    email: StrictStr
    email_verified: StrictBool
    id: StrictStr
    last_login_at: datetime
    login_count: StrictInt
    phone: StrictStr
    phone_verified: StrictBool
    recent_events: List[UserEventInfo]
    social_connections: UserSocialConnections
    status: UserStatus
    updated_at: datetime
    user_metadata: Optional[Union[str, Any]]
    webauthn: StrictBool
    webauthn_devices: List[WebAuthnDevices]
    webauthn_types: List[WebAuthnType] = Field(description="List of credential types that have been used for authentication")
    __properties: ClassVar[List[str]] = ["created_at", "email", "email_verified", "id", "last_login_at", "login_count", "phone", "phone_verified", "recent_events", "social_connections", "status", "updated_at", "user_metadata", "webauthn", "webauthn_devices", "webauthn_types"]

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
        """Create an instance of UserInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in recent_events (list)
        _items = []
        if self.recent_events:
            for _item in self.recent_events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recent_events'] = _items
        # override the default output from pydantic by calling `to_dict()` of social_connections
        if self.social_connections:
            _dict['social_connections'] = self.social_connections.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in webauthn_devices (list)
        _items = []
        if self.webauthn_devices:
            for _item in self.webauthn_devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['webauthn_devices'] = _items
        # set to None if user_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.user_metadata is None and "user_metadata" in self.model_fields_set:
            _dict['user_metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UserInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "email": obj.get("email"),
            "email_verified": obj.get("email_verified"),
            "id": obj.get("id"),
            "last_login_at": obj.get("last_login_at"),
            "login_count": obj.get("login_count"),
            "phone": obj.get("phone"),
            "phone_verified": obj.get("phone_verified"),
            "recent_events": [UserEventInfo.from_dict(_item) for _item in obj.get("recent_events")] if obj.get("recent_events") is not None else None,
            "social_connections": UserSocialConnections.from_dict(obj.get("social_connections")) if obj.get("social_connections") is not None else None,
            "status": obj.get("status"),
            "updated_at": obj.get("updated_at"),
            "user_metadata": obj.get("user_metadata"),
            "webauthn": obj.get("webauthn"),
            "webauthn_devices": [WebAuthnDevices.from_dict(_item) for _item in obj.get("webauthn_devices")] if obj.get("webauthn_devices") is not None else None,
            "webauthn_types": obj.get("webauthn_types")
        })
        return _obj


