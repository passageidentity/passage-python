from __future__ import annotations

from passageidentity import PassageError
from passageidentity.openapi_client.exceptions import ApiException
from passageidentity.openapi_client.models.model400_error import Model400Error


class MockApiException(ApiException):
    def __init__(self, status: int, data: Model400Error | None, body: str | None = None) -> None:
        self.status = status
        self.data = data
        self.body = body


def test_error_with_all_values() -> None:
    error = PassageError("some message", 400, "Bad Request", {"error": "some error", "code": "some_error_code"})
    assert error.message == "some message"
    assert error.status_code == 400
    assert error.status_text == "Bad Request"
    assert error.error == "some error"
    assert error.error_code == "some_error_code"


def test_error_with_only_message() -> None:
    error = PassageError("some message")
    assert error.message == "some message"
    assert error.status_code is None
    assert error.status_text is None
    assert error.error is None
    assert error.error_code is None


def test_from_response_error() -> None:
    response_error = MockApiException(
        status=400,
        data=Model400Error(code="invalid_request", error="some error"),
    )

    error = PassageError.from_response_error(response_error, "some message")
    assert error.message == "some message: some error"
    assert error.status_code == 400
    assert error.error_code == "invalid_request"
    assert error.status_text is None
    assert error.error is None


def test_from_response_error_without_message() -> None:
    response_error = MockApiException(
        status=400,
        data=Model400Error(code="invalid_request", error="some error"),
    )

    error = PassageError.from_response_error(response_error)
    assert error.message == "some error"
    assert error.status_code == 400
    assert error.error_code == "invalid_request"
    assert error.status_text is None
    assert error.error is None


def test_from_response_error_without_data() -> None:
    response_error = MockApiException(
        status=400,
        data=None,
        body="some error",
    )

    error = PassageError.from_response_error(response_error)
    assert error.message == "some error"
    assert error.status_code == 400
    assert error.error_code is None
    assert error.status_text is None
    assert error.error is None
