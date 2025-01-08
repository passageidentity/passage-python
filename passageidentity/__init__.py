"""Initializes the Passage identity package."""

from .errors import PassageError
from .models import (
    MagicLinkArgs,
    MagicLinkOptions,
    MagicLinkWithEmailArgs,
    MagicLinkWithPhoneArgs,
    MagicLinkWithUserArgs,
)
from .openapi_client.models import (
    CreateUserArgs,
    MagicLink,
    MagicLinkChannel,
    MagicLinkLanguage,
    MagicLinkType,
    PassageUser,
    UpdateUserArgs,
    UserStatus,
    WebAuthnDevices,
    WebAuthnType,
)
from .passage import Passage

__all__ = [
    "CreateUserArgs",
    "MagicLink",
    "MagicLinkArgs",
    "MagicLinkChannel",
    "MagicLinkLanguage",
    "MagicLinkOptions",
    "MagicLinkType",
    "MagicLinkWithEmailArgs",
    "MagicLinkWithPhoneArgs",
    "MagicLinkWithUserArgs",
    "Passage",
    "PassageError",
    "PassageUser",
    "UpdateUserArgs",
    "UserStatus",
    "WebAuthnDevices",
    "WebAuthnType",
]
