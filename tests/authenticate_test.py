from passageidentity import Passage
from passageidentity import PassageError
import pytest
import os
import random
import string
from flask import Flask, request
from dotenv import load_dotenv
from werkzeug.http import dump_cookie

app = Flask(__name__)

load_dotenv()
PASSAGE_USER_ID = os.environ.get("PASSAGE_USER_ID")
PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
PASSAGE_AUTH_TOKEN = os.environ.get("PASSAGE_AUTH_TOKEN")
RANDOM_EMAIL = ''.join(random.choice(string.ascii_letters) for _ in range(14)) + "@email.com"

def testFlaskValidTokenInHeader():
    psg = Passage(PASSAGE_APP_ID, auth_strategy=Passage.HEADER_AUTH)
    # flask request context
    with app.test_request_context("thisisaurl.com",headers={'Authorization':f'Bearer {PASSAGE_AUTH_TOKEN}'}):
        user = psg.authenticateRequest(request)
        assert user == PASSAGE_USER_ID

def testValidJWT():
    psg = Passage(PASSAGE_APP_ID, auth_strategy=Passage.HEADER_AUTH)
    user = psg.authenticateJWT(PASSAGE_AUTH_TOKEN)
    assert user == PASSAGE_USER_ID

def testFlaskTokenInCookie():
    psg = Passage(PASSAGE_APP_ID)
    # flask request context
    cookie = dump_cookie('psg_auth_token', PASSAGE_AUTH_TOKEN)
    with app.test_request_context("thisisaurl.com",environ_base={'HTTP_COOKIE':cookie}):
        user = psg.authenticateRequest(request)
        assert user == PASSAGE_USER_ID

def testFlaskInValidToken():
    psg = Passage(PASSAGE_APP_ID)
    # flask request context
    with app.test_request_context("thisisaurl.com",headers={'Authorization':'Bearer invalidToken'}):
        with pytest.raises(PassageError) as e:
            user = psg.authenticateRequest(request)

def testGetUserInfoValid():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = psg.getUser(PASSAGE_USER_ID)
    assert user.email == "testEmail@domain.com"

def testActivateUser():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = psg.activateUser(PASSAGE_USER_ID)
    assert user.active == True

def testDeactivateUser():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    
    user = psg.getUser(PASSAGE_USER_ID)
    assert user.email == "testEmail@domain.com"
    user = psg.deactivateUser(user.id)
    assert user.active == False

def testUpdateEmail():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    user = psg.updateUser(PASSAGE_USER_ID, {"email": "testEmail2@domain.com"})
    assert user.email == "testEmail2@domain.com"
    user = psg.updateUser(PASSAGE_USER_ID, {"email": "testEmail@domain.com"})
    assert user.email == "testEmail@domain.com"

def testUpdateUserPhone():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    user = psg.updateUser(PASSAGE_USER_ID, {"phone": "+15005550001"})
    assert user.phone == "+15005550001"
    user = psg.updateUser(PASSAGE_USER_ID, {"phone": "+15005550008"})
    assert user.phone == "+15005550008"

def testUpdateUserEmail():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    user = psg.updateUser(PASSAGE_USER_ID, {"email":"testEmail2@domain.com"})
    assert user.email ==  "testEmail2@domain.com"
    user = psg.updateUser(PASSAGE_USER_ID, {"email":"testEmail@domain.com"})
    assert user.email ==  "testEmail@domain.com"

def testGetUserInfoUserDoesNotExist():
    pass

def testCreateAndDeleteUser():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    newUser = psg.createUser({"email": RANDOM_EMAIL})
    assert newUser.email == RANDOM_EMAIL

    deletedUser = psg.deleteUser(newUser.id)
    assert deletedUser == True
