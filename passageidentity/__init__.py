"""Initializes the Passage identity package."""

from .errors import PassageError
from .passage import Passage

__all__ = [
    "Passage",
    "PassageError",
]
