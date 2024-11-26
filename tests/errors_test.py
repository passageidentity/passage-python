from passageidentity import PassageError


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
