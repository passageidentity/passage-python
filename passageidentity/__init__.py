"""Initializes the Passage identity package."""

from .errors import PassageError
from .models import (
    MagicLinkArgs,
    MagicLinkOptions,
    MagicLinkWithEmailArgs,
    MagicLinkWithPhoneArgs,
    MagicLinkWithUserArgs,
)
from .passage import Passage

__all__ = [
    "MagicLinkArgs",
    "MagicLinkOptions",
    "MagicLinkWithEmailArgs",
    "MagicLinkWithPhoneArgs",
    "MagicLinkWithUserArgs",
    "Passage",
    "PassageError",
]
