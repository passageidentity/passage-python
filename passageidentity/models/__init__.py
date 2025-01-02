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
from passageidentity.models.update_magic_link_auth_method import (
    UpdateMagicLinkAuthMethod,
)
from passageidentity.models.update_passkey_auth_method import UpdatePasskeysAuthMethod
from passageidentity.models.update_otp_auth_method import UpdateOtpAuthMethod
from passageidentity.models.magic_link_args import MagicLinkArgs, MagicLinkWithEmailArgs, MagicLinkWithPhoneArgs, MagicLinkWithUserArgs
from passageidentity.models.magic_link_options import MagicLinkOptions
