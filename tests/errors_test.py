from passageidentity import PassageError
from passageidentity.openapi_client.exceptions import ApiException


class MockApiException(ApiException):
    def __init__(self, status: int, body: dict) -> None:
        self.status = status
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
        body={"error": "some error", "code": "some_error_code"},
    )

    error = PassageError.from_response_error(response_error, "some message")
    assert error.message == "some message: some error"
    assert error.status_code == 400
    assert error.error_code == "some_error_code"
    assert error.status_text is None
    assert error.error is None


def test_from_response_error_without_message() -> None:
    response_error = MockApiException(
        status=400,
        body={"error": "some error", "code": "some_error_code"},
    )

    error = PassageError.from_response_error(response_error)
    assert error.message == "some error"
    assert error.status_code == 400
    assert error.error_code == "some_error_code"
    assert error.status_text is None
    assert error.error is None
