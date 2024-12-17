"""Arguments and options for creating a Magic Link."""

from passageidentity.models.magic_link_args import (
    MagicLinkArgs,
    MagicLinkWithEmailArgs,
    MagicLinkWithPhoneArgs,
    MagicLinkWithUserArgs,
)
from passageidentity.models.magic_link_options import MagicLinkOptions

__all__ = [
    "MagicLinkArgs",
    "MagicLinkOptions",
    "MagicLinkWithEmailArgs",
    "MagicLinkWithPhoneArgs",
    "MagicLinkWithUserArgs",
]
