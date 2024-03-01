# coding: utf-8

# flake8: noqa
"""
    Passage Management API

    Passage's management API to manage your Passage apps and users.

    The version of the OpenAPI document: 1
    Contact: support@passage.id
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from passageidentity.openapi_client.models.app_info import AppInfo
from passageidentity.openapi_client.models.app_response import AppResponse
from passageidentity.openapi_client.models.apple_user_social_connection import AppleUserSocialConnection
from passageidentity.openapi_client.models.auth_methods import AuthMethods
from passageidentity.openapi_client.models.create_magic_link_request import CreateMagicLinkRequest
from passageidentity.openapi_client.models.create_user_request import CreateUserRequest
from passageidentity.openapi_client.models.element_customization import ElementCustomization
from passageidentity.openapi_client.models.font_family import FontFamily
from passageidentity.openapi_client.models.github_user_social_connection import GithubUserSocialConnection
from passageidentity.openapi_client.models.google_user_social_connection import GoogleUserSocialConnection
from passageidentity.openapi_client.models.layout_config import LayoutConfig
from passageidentity.openapi_client.models.layouts import Layouts
from passageidentity.openapi_client.models.list_devices_response import ListDevicesResponse
from passageidentity.openapi_client.models.magic_link import MagicLink
from passageidentity.openapi_client.models.magic_link_auth_method import MagicLinkAuthMethod
from passageidentity.openapi_client.models.magic_link_channel import MagicLinkChannel
from passageidentity.openapi_client.models.magic_link_response import MagicLinkResponse
from passageidentity.openapi_client.models.magic_link_type import MagicLinkType
from passageidentity.openapi_client.models.model400_error import Model400Error
from passageidentity.openapi_client.models.model401_error import Model401Error
from passageidentity.openapi_client.models.model404_error import Model404Error
from passageidentity.openapi_client.models.model500_error import Model500Error
from passageidentity.openapi_client.models.otp_auth_method import OtpAuthMethod
from passageidentity.openapi_client.models.passkeys_auth_method import PasskeysAuthMethod
from passageidentity.openapi_client.models.technologies import Technologies
from passageidentity.openapi_client.models.ttl_display_unit import TtlDisplayUnit
from passageidentity.openapi_client.models.update_magic_link_auth_method import UpdateMagicLinkAuthMethod
from passageidentity.openapi_client.models.update_otp_auth_method import UpdateOtpAuthMethod
from passageidentity.openapi_client.models.update_passkeys_auth_method import UpdatePasskeysAuthMethod
from passageidentity.openapi_client.models.update_user_request import UpdateUserRequest
from passageidentity.openapi_client.models.user_event_status import UserEventStatus
from passageidentity.openapi_client.models.user_info import UserInfo
from passageidentity.openapi_client.models.user_metadata_field import UserMetadataField
from passageidentity.openapi_client.models.user_metadata_field_type import UserMetadataFieldType
from passageidentity.openapi_client.models.user_recent_event import UserRecentEvent
from passageidentity.openapi_client.models.user_response import UserResponse
from passageidentity.openapi_client.models.user_social_connections import UserSocialConnections
from passageidentity.openapi_client.models.user_status import UserStatus
from passageidentity.openapi_client.models.web_authn_devices import WebAuthnDevices
from passageidentity.openapi_client.models.web_authn_icons import WebAuthnIcons
from passageidentity.openapi_client.models.web_authn_type import WebAuthnType
