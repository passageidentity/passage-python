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

    def __init__(self, *, email: str, link_type: MagicLinkType, send: bool) -> None:
        """Initialize the MagicLinkWithEmailArgs with the email."""
        self.email = email
        self.type = link_type
        self.send = send


class MagicLinkWithPhoneArgs(MagicLinkArgsBase):
    """Arguments for creating a Magic Link with a phone number."""

    phone: str

    def __init__(self, *, phone: str, link_type: MagicLinkType, send: bool) -> None:
        """Initialize the MagicLinkWithPhoneArgs with the phone number."""
        self.phone = phone
        self.type = link_type
        self.send = send


class MagicLinkWithUserArgs(MagicLinkArgsBase):
    """Arguments for creating a Magic Link with a user ID."""

    user_id: str
    channel: MagicLinkChannel

    def __init__(self, *, user_id: str, channel: MagicLinkChannel, link_type: MagicLinkType, send: bool) -> None:
        """Initialize the MagicLinkWithUserArgs with the user ID."""
        self.user_id = user_id
        self.channel = channel
        self.type = link_type
        self.send = send


MagicLinkArgs = Union[MagicLinkWithEmailArgs, MagicLinkWithPhoneArgs, MagicLinkWithUserArgs]
