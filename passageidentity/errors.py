"""Defines custom error classes for handling Passage-related errors."""

from __future__ import annotations

from typing import TYPE_CHECKING

import typing_extensions

if TYPE_CHECKING:
    from passageidentity.openapi_client.exceptions import ApiException


class PassageError(Exception):
    """Error class for handling Passage errors."""

    @typing_extensions.deprecated(
        "This should only be constructed by the Passage SDK. Use this type just for type checking.",
    )
    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        status_text: str | None = None,
        body: dict | None = None,
        error_code: str | None = None,
    ) -> None:
        """Initialize the error with a message, status code, status text, and optional body."""
        self.message = message
        self.status_code = status_code
        self.status_text = status_text

        self.error_code = error_code
        self.error = None

        if body is not None:
            self.error = body["error"]
            self.error_code = body["code"]

    @classmethod
    def from_response_error(cls, response_error: ApiException, message: str | None = None) -> PassageError:
        """Initialize the error with a response body and optional message."""
        error_code = response_error.body["code"] if response_error.body else None
        error_msg = response_error.body["error"] if response_error.body else None
        msg = ": ".join(filter(None, [message, error_msg]))

        return cls(message=msg, status_code=response_error.status, error_code=error_code)
