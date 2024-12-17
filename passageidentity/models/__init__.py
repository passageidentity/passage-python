"""Arguments and options for creating a Magic Link."""

from passageidentity.models.create_user_args import CreateUserArgs
from passageidentity.models.magic_link_args import (
    MagicLinkArgs,
    MagicLinkWithEmailArgs,
    MagicLinkWithPhoneArgs,
    MagicLinkWithUserArgs,
)
from passageidentity.models.magic_link_options import MagicLinkOptions
from passageidentity.models.passage_user import PassageUser
from passageidentity.models.update_user_args import UpdateUserArgs

__all__ = [
    "CreateUserArgs",
    "MagicLinkArgs",
    "MagicLinkOptions",
    "MagicLinkWithEmailArgs",
    "MagicLinkWithPhoneArgs",
    "MagicLinkWithUserArgs",
    "PassageUser",
    "UpdateUserArgs",
]
