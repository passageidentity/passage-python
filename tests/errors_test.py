from ast import Pass
from passageidentity import PassageError
import pytest

def testErrorWithAllValues():
    error = PassageError("some message", 400, "Bad Request", {"error": "some error"})
    assert error.message == "some message"
    assert error.status_code == 400
    assert error.status_text == "Bad Request"
    assert error.error == "some error"
    
def testErrorWithOnlyMessage():
    error = PassageError("some message")
    assert error.message == "some message"
    assert error.status_code == None 
    assert error.status_text == None
    assert error.error == None
