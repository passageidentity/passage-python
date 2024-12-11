"""Defines required arguments for creating a Magic Link."""

from typing import Union

from passageidentity.openapi_client.models.magic_link_channel import MagicLinkChannel
from passageidentity.openapi_client.models.magic_link_type import MagicLinkType


class MagicLinkArgsBase:
    """Base class for MagicLinkArgs."""

    type: MagicLinkType
    send: bool


class MagicLinkWithEmailArgs(MagicLinkArgsBase):
    """Arguments for creating a Magic Link with an email."""

    email: str


class MagicLinkWithPhoneArgs(MagicLinkArgsBase):
    """Arguments for creating a Magic Link with a phone number."""

    phone: str


class MagicLinkWithUserArgs(MagicLinkArgsBase):
    """Arguments for creating a Magic Link with a user ID."""

    user_id: str
    channel: MagicLinkChannel


MagicLinkArgs = Union[MagicLinkWithEmailArgs, MagicLinkWithPhoneArgs, MagicLinkWithUserArgs]
