"""Initializes the Passage identity package."""

from .errors import PassageError
from .models import MagicLinkArgs, MagicLinkOptions
from .passage import Passage

__all__ = [
    "MagicLinkArgs",
    "MagicLinkOptions",
    "Passage",
    "PassageError",
]
