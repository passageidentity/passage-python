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

def randomEmail():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(14)) + "@email.com"

def randomPhone():
    return  "+1512" + ''.join(random.choice('23456789') for _ in range(7))

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

def testFetchJWKS():
    psg = Passage(PASSAGE_APP_ID, auth_strategy=Passage.HEADER_AUTH)
    assert len(psg.jwks) > 0

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

def testGetApp():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    app = psg.getApp()
    assert PASSAGE_APP_ID == app.id


def testCreateMagicLink():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    magicLink = psg.createMagicLink(magicLinkAttributes={"email": "chris@passage.id", "channel": "email", "ttl": 12})
    assert magicLink.identifier == "chris@passage.id"
    assert magicLink.ttl == 12

def testGetUserInfoValid():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = psg.getUser(PASSAGE_USER_ID)
    assert user.id == PASSAGE_USER_ID

def testActivateUser():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = psg.activateUser(PASSAGE_USER_ID)
    assert user.status == "active"

def testDeactivateUser():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    user = psg.getUser(PASSAGE_USER_ID)
    user = psg.deactivateUser(user.id)
    assert user.status == "inactive"

def testListUserDevices():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    devices = psg.listUserDevices(PASSAGE_USER_ID)
    assert len(devices) == 2

# revokeUserDevice is not tested because it is impossible to spoof webauthn to create a device to then revoke

def testUpdateUserPhone():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    phone1 = randomPhone()
    print(phone1)
    user = psg.updateUser(PASSAGE_USER_ID, {"phone": phone1})
    assert user.phone == phone1

def testUpdateUserEmail():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email1 = randomEmail()
    user = psg.updateUser(PASSAGE_USER_ID, {"email":email1})
    assert user.email ==  email1

def testUpdateUserWithMetadata():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = randomEmail()
    user = psg.updateUser(PASSAGE_USER_ID, {"email": email, "user_metadata": { "example1": "qwe"}})
    assert user.email ==  email
    assert user.user_metadata["example1"] == "qwe"

    user = psg.updateUser(PASSAGE_USER_ID, {"email": email,  "user_metadata": { "example1": "asd"}})
    assert user.email ==  email
    assert user.user_metadata["example1"] == "asd"

def testCreateUserWithMetadata():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = randomEmail()
    user = psg.createUser({"email": email, "user_metadata": { "example1": "qwe"}})
    assert user.email ==  email
    assert user.user_metadata["example1"] == "qwe"

def testGetUserInfoUserDoesNotExist():
    pass

def testCreateAndDeleteUser():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = randomEmail()
    newUser = psg.createUser({"email": email})
    assert newUser.email == email

    deletedUser = psg.deleteUser(newUser.id)
    assert deletedUser == True

def testSmartLinkValid():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = randomEmail()
    magicLink = psg.createMagicLink({"email": email})
    assert magicLink.identifier == email
    assert magicLink.activated == False

def testsignOut():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    success = psg.signOut(PASSAGE_USER_ID)
    assert success == True
