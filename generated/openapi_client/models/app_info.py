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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from openapi_client.models.auth_methods import AuthMethods
from openapi_client.models.element_customization import ElementCustomization
from openapi_client.models.layouts import Layouts
from openapi_client.models.technologies import Technologies
from openapi_client.models.user_metadata_field import UserMetadataField
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppInfo(BaseModel):
    """
    AppInfo
    """ # noqa: E501
    additional_auth_origins: List[StrictStr]
    allowed_callback_urls: List[StrictStr] = Field(description="The valid URLs where users can be redirected after authentication.")
    allowed_identifier: StrictStr
    allowed_logout_urls: List[StrictStr] = Field(description="The valid URLs where users can be redirected after logging out.")
    application_login_uri: StrictStr = Field(description="A route within your application that redirects to the Authorization URL endpoint.")
    auth_fallback_method: StrictStr = Field(description="Deprecated Property. Please refer to `auth_methods` to view settings for individual authentication methods.")
    auth_fallback_method_ttl: StrictInt = Field(description="Deprecated Property. Please refer to `auth_methods` to view settings for individual authentication methods.")
    auth_methods: AuthMethods
    auth_origin: StrictStr
    created_at: datetime
    default_language: StrictStr
    id: StrictStr
    layouts: Layouts
    login_url: StrictStr
    light_logo_url: Optional[StrictStr] = None
    dark_logo_url: Optional[StrictStr] = None
    name: StrictStr
    hosted: StrictBool = Field(description="whether or not the app's login page hosted by passage")
    hosted_subdomain: StrictStr = Field(description="the subdomain of the app's hosted login page")
    id_token_lifetime: Optional[StrictInt] = None
    passage_branding: StrictBool
    profile_management: StrictBool
    public_signup: StrictBool
    redirect_url: StrictStr
    refresh_absolute_lifetime: StrictInt
    refresh_enabled: StrictBool
    refresh_inactivity_lifetime: StrictInt
    require_email_verification: StrictBool
    require_identifier_verification: StrictBool
    required_identifier: StrictStr
    role: StrictStr
    rsa_public_key: StrictStr
    secret: Optional[StrictStr] = Field(default=None, description="can only be retrieved by an app admin")
    session_timeout_length: StrictInt
    type: StrictStr
    user_metadata_schema: List[UserMetadataField]
    technologies: List[Technologies]
    element_customization: ElementCustomization
    element_customization_dark: ElementCustomization
    __properties: ClassVar[List[str]] = ["additional_auth_origins", "allowed_callback_urls", "allowed_identifier", "allowed_logout_urls", "application_login_uri", "auth_fallback_method", "auth_fallback_method_ttl", "auth_methods", "auth_origin", "created_at", "default_language", "id", "layouts", "login_url", "light_logo_url", "dark_logo_url", "name", "hosted", "hosted_subdomain", "id_token_lifetime", "passage_branding", "profile_management", "public_signup", "redirect_url", "refresh_absolute_lifetime", "refresh_enabled", "refresh_inactivity_lifetime", "require_email_verification", "require_identifier_verification", "required_identifier", "role", "rsa_public_key", "secret", "session_timeout_length", "type", "user_metadata_schema", "technologies", "element_customization", "element_customization_dark"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('complete', 'flex'):
            raise ValueError("must be one of enum values ('complete', 'flex')")
        return value

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
        """Create an instance of AppInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auth_methods
        if self.auth_methods:
            _dict['auth_methods'] = self.auth_methods.to_dict()
        # override the default output from pydantic by calling `to_dict()` of layouts
        if self.layouts:
            _dict['layouts'] = self.layouts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in user_metadata_schema (list)
        _items = []
        if self.user_metadata_schema:
            for _item in self.user_metadata_schema:
                if _item:
                    _items.append(_item.to_dict())
            _dict['user_metadata_schema'] = _items
        # override the default output from pydantic by calling `to_dict()` of element_customization
        if self.element_customization:
            _dict['element_customization'] = self.element_customization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of element_customization_dark
        if self.element_customization_dark:
            _dict['element_customization_dark'] = self.element_customization_dark.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "additional_auth_origins": obj.get("additional_auth_origins"),
            "allowed_callback_urls": obj.get("allowed_callback_urls"),
            "allowed_identifier": obj.get("allowed_identifier"),
            "allowed_logout_urls": obj.get("allowed_logout_urls"),
            "application_login_uri": obj.get("application_login_uri"),
            "auth_fallback_method": obj.get("auth_fallback_method"),
            "auth_fallback_method_ttl": obj.get("auth_fallback_method_ttl"),
            "auth_methods": AuthMethods.from_dict(obj.get("auth_methods")) if obj.get("auth_methods") is not None else None,
            "auth_origin": obj.get("auth_origin"),
            "created_at": obj.get("created_at"),
            "default_language": obj.get("default_language"),
            "id": obj.get("id"),
            "layouts": Layouts.from_dict(obj.get("layouts")) if obj.get("layouts") is not None else None,
            "login_url": obj.get("login_url"),
            "light_logo_url": obj.get("light_logo_url"),
            "dark_logo_url": obj.get("dark_logo_url"),
            "name": obj.get("name"),
            "hosted": obj.get("hosted"),
            "hosted_subdomain": obj.get("hosted_subdomain"),
            "id_token_lifetime": obj.get("id_token_lifetime"),
            "passage_branding": obj.get("passage_branding"),
            "profile_management": obj.get("profile_management"),
            "public_signup": obj.get("public_signup"),
            "redirect_url": obj.get("redirect_url"),
            "refresh_absolute_lifetime": obj.get("refresh_absolute_lifetime"),
            "refresh_enabled": obj.get("refresh_enabled"),
            "refresh_inactivity_lifetime": obj.get("refresh_inactivity_lifetime"),
            "require_email_verification": obj.get("require_email_verification"),
            "require_identifier_verification": obj.get("require_identifier_verification"),
            "required_identifier": obj.get("required_identifier"),
            "role": obj.get("role"),
            "rsa_public_key": obj.get("rsa_public_key"),
            "secret": obj.get("secret"),
            "session_timeout_length": obj.get("session_timeout_length"),
            "type": obj.get("type"),
            "user_metadata_schema": [UserMetadataField.from_dict(_item) for _item in obj.get("user_metadata_schema")] if obj.get("user_metadata_schema") is not None else None,
            "technologies": obj.get("technologies"),
            "element_customization": ElementCustomization.from_dict(obj.get("element_customization")) if obj.get("element_customization") is not None else None,
            "element_customization_dark": ElementCustomization.from_dict(obj.get("element_customization_dark")) if obj.get("element_customization_dark") is not None else None
        })
        return _obj


