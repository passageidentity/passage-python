"""Defines custom error classes for handling Passage-related errors."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from passageidentity.openapi_client.exceptions import ApiException


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
            self.error_code = body["code"]
        else:
            self.error = None
            self.error_code = None

    @staticmethod
    def from_response_error(response_error: ApiException, message: str | None) -> PassageError:
        """Initialize the error with a response body and optional message."""
        error_code = response_error.body["code"] if response_error.body else None
        error_msg = response_error.body["error"] if response_error.body else None
        msg = ": ".join(filter(None, [message, error_msg]))

        psg_error = PassageError(msg)
        psg_error.status_code = response_error.status
        psg_error.error_code = error_code

        return psg_error
