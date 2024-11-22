"""Defines custom error classes for handling Passage-related errors."""

from __future__ import annotations


class PassageError(Exception):
    """Error class for handling Passage errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        status_text: str | None = None,
        body: dict | None = None,
    ) -> None:
        """Initialize the error with a message, status code, status text, and optional body."""
        self.message = message
        self.status_code = status_code
        self.status_text = status_text
        if body is not None:
            self.error = body["error"]
        else:
            self.error = None
