"""Defines custom error classes for handling Passage-related errors."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from passageidentity.openapi_client.exceptions import ApiException


class PassageError(Exception):
    """Error class for handling Passage errors."""

    message: str
    status_code: int | None
    error_code: str | None

    def __str__(self) -> str:
        """Return the error message."""
        return self.message

    @classmethod
    def from_response_error(cls, response_error: ApiException) -> PassageError:
        """Initialize the error with a response body and optional message."""
        if response_error.data is not None:
            data_dict = response_error.data.to_dict()
            error_code = data_dict.get("code")
            error_msg = data_dict.get("error")
        else:
            error_code = None
            error_msg = str(response_error.body)

        psg_error = cls()
        psg_error.message = error_msg
        psg_error.status_code = response_error.status
        psg_error.error_code = error_code

        return psg_error
