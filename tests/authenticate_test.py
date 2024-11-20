from passageidentity.passage import Passage
from passageidentity import PassageError
from faker import Faker
import pytest
import os
import random
import string
from dotenv import load_dotenv

load_dotenv()
f = Faker()
PASSAGE_USER_ID = os.environ.get("PASSAGE_USER_ID")
PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
PASSAGE_AUTH_TOKEN = os.environ.get("PASSAGE_AUTH_TOKEN")


def randomEmail():
    return f.email() 


def randomPhone():
    return "+1512" + ''.join(str(f.random_number(digits=1, fix_len=True)) for _ in range(7))


def testValidJWT():
    psg = Passage(PASSAGE_APP_ID, auth_strategy=Passage.HEADER_AUTH)
    user = psg.authenticateJWT(PASSAGE_AUTH_TOKEN)
    assert user == PASSAGE_USER_ID


def testInvalidJWT():
    psg = Passage(PASSAGE_APP_ID, auth_strategy=Passage.HEADER_AUTH)
    with pytest.raises(PassageError):
        psg.authenticateJWT("invalid_token")


def testValidateJWT():
    psg = Passage(PASSAGE_APP_ID, auth_strategy=Passage.HEADER_AUTH)
    user = psg.validateJwt(PASSAGE_AUTH_TOKEN)
    assert user == PASSAGE_USER_ID


def testFetchJWKS():
    psg = Passage(PASSAGE_APP_ID, auth_strategy=Passage.HEADER_AUTH)
    assert len(psg.jwks) > 0


def testGetApp():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    app = psg.getApp()
    assert PASSAGE_APP_ID == app.id


def testCreateMagicLink():
    magicLinkAttributes = {
        "email": "chris@passage.id",
        "channel": "email",
        "ttl": 12,
    }
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    magicLink = psg.createMagicLink(magicLinkAttributes)
    assert magicLink.identifier == "chris@passage.id"
    assert magicLink.ttl == 12


def testGetUserInfoValid():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = psg.getUser(PASSAGE_USER_ID)
    assert user.id == PASSAGE_USER_ID


def testGetUserInfoByIdentifierValid():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = randomEmail()
    newUser = psg.createUser({"email": email})
    assert newUser.email == email

    userByIdentifier = psg.getUserByIdentifier(email)
    assert userByIdentifier.id == newUser.id

    user = psg.getUser(newUser.id)
    assert user.id == newUser.id

    assert userByIdentifier == user
    assert psg.deleteUser(newUser.id)


def testGetUserInfoByIdentifierValidUpperCase():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = randomEmail()
    newUser = psg.createUser({"email": email})
    assert newUser.email == email

    userByIdentifier = psg.getUserByIdentifier(email.upper())
    assert userByIdentifier.id == newUser.id

    user = psg.getUser(newUser.id)
    assert user.id == newUser.id

    assert userByIdentifier == user
    assert psg.deleteUser(newUser.id)


def testGetUserInfoByIdentifierPhoneValid():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    phone = randomPhone()
    newUser = psg.createUser({"phone": phone})
    assert newUser.phone == phone

    userByIdentifier = psg.getUserByIdentifier(phone)
    assert userByIdentifier.id == newUser.id

    user = psg.getUser(newUser.id)
    assert user.id == newUser.id

    assert userByIdentifier == user
    assert psg.deleteUser(newUser.id)


def testGetUserInfoByIdentifierError():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    with pytest.raises(PassageError, match="Failed to find user data"):
        psg.getUserByIdentifier("error@passage.id")


def testActivateUser():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = psg.activateUser(PASSAGE_USER_ID)
    assert user.status == "active"


def testDeactivateUser():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    user = psg.getUser(PASSAGE_USER_ID)
    user = psg.deactivateUser(user.id)
    assert user.status == "inactive"


# def testListUserDevices():
#     psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

#     devices = psg.listUserDevices(PASSAGE_USER_ID)
#     assert len(devices) == 2

# listUserDevices & revokeUserDevice are not tested because it is impossible to spoof webauthn to create a device to then revoke


def testUpdateUserPhone():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    phone1 = randomPhone()
    user = psg.updateUser(PASSAGE_USER_ID, {"phone": phone1})
    assert user.phone == phone1


def testUpdateUserEmail():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email1 = randomEmail()
    user = psg.updateUser(PASSAGE_USER_ID, {"email": email1})
    assert user.email == email1


def testUpdateUserWithMetadata():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = randomEmail()
    user = psg.updateUser(
        PASSAGE_USER_ID, {"email": email, "user_metadata": {"example1": "qwe"}}
    )
    assert user.email == email
    assert user.user_metadata["example1"] == "qwe"

    user = psg.updateUser(
        PASSAGE_USER_ID, {"email": email, "user_metadata": {"example1": "asd"}}
    )
    assert user.email == email
    assert user.user_metadata["example1"] == "asd"


def testCreateUserWithMetadata():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = randomEmail()
    user = psg.createUser({"email": email, "user_metadata": {"example1": "qwe"}})
    assert user.email == email
    assert user.user_metadata["example1"] == "qwe"
    assert psg.deleteUser(user.id)


def testGetUserInfoUserDoesNotExist():
    pass


def testCreateAndDeleteUser():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = randomEmail()
    newUser = psg.createUser({"email": email})
    assert newUser.email == email
    assert psg.deleteUser(newUser.id)


def testSmartLinkValid():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = randomEmail()
    magicLink = psg.createMagicLink({"email": email})
    assert magicLink.identifier == email
    assert not magicLink.activated


def testsignOut():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    assert psg.signOut(PASSAGE_USER_ID)


def testrevokeUserRefreshTokens():
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    assert psg.revokeUserRefreshTokens(PASSAGE_USER_ID)
