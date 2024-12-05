import os
from typing import cast

import pytest
from dotenv import load_dotenv
from faker import Faker

from passageidentity.errors import PassageError
from passageidentity.openapi_client.models.update_user_request import UpdateUserRequest
from passageidentity.openapi_client.models.user_info import UserInfo
from passageidentity.passage import Passage

load_dotenv()
f = Faker()

PASSAGE_USER_ID = os.environ.get("PASSAGE_USER_ID") or ""
PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID") or ""
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY") or ""
PASSAGE_AUTH_TOKEN = os.environ.get("PASSAGE_AUTH_TOKEN") or ""


def test_get_by_identifier_valid_upper_case() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    new_user = cast(UserInfo, psg.user.create({"email": email}))  # type: ignore[arg-type]
    assert new_user.email == email

    user_by_identifier = cast(UserInfo, psg.user.get_by_identifier(email.upper()))
    assert user_by_identifier.id == new_user.id

    user = cast(UserInfo, psg.user.get(new_user.id))
    assert user.id == new_user.id

    assert user_by_identifier == user
    assert psg.user.delete(new_user.id) is None


def test_get_by_identifier_user_not_exist() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    with pytest.raises(PassageError, match="Could not find user with identifier"):
        psg.user.get_by_identifier("error@passage.id")


def test_get_user_info_valid() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = cast(UserInfo, psg.getUser(PASSAGE_USER_ID))
    assert user.id == PASSAGE_USER_ID


def test_get_user_info_by_identifier_valid() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    new_user = cast(UserInfo, psg.createUser({"email": email}))  # type: ignore[arg-type]
    assert new_user.email == email

    user_by_identifier = cast(UserInfo, psg.getUserByIdentifier(email))
    assert user_by_identifier.id == new_user.id

    user = cast(UserInfo, psg.getUser(new_user.id))
    assert user.id == new_user.id

    assert user_by_identifier == user
    assert psg.deleteUser(new_user.id)


def test_get_user_info_by_identifier_phone_valid() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    phone = "+15005550030"
    new_user = cast(UserInfo, psg.createUser({"phone": phone}))  # type: ignore[arg-type]
    assert new_user.phone == phone

    user_by_identifier = cast(UserInfo, psg.getUserByIdentifier(phone))
    assert user_by_identifier.id == new_user.id

    user = cast(UserInfo, psg.getUser(new_user.id))
    assert user.id == new_user.id

    assert user_by_identifier == user
    assert psg.deleteUser(new_user.id)


def test_activate_user() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = cast(UserInfo, psg.activateUser(PASSAGE_USER_ID))
    assert user.status == "active"


def test_deactivate_user() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    user = cast(UserInfo, psg.getUser(PASSAGE_USER_ID))
    user = cast(UserInfo, psg.deactivateUser(user.id))
    assert user.status == "inactive"


def test_list_user_devices() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    devices = cast(list, psg.listUserDevices(PASSAGE_USER_ID))
    assert len(devices) == 2


def test_update_user_phone() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    phone = "+15005550021"
    new_user = cast(UserInfo, psg.createUser({"phone": phone}))  # type: ignore[arg-type]

    phone = "+15005550022"
    user = cast(UserInfo, psg.updateUser(new_user.id, {"phone": phone}))  # type: ignore[arg-type]
    assert user.phone == phone
    assert psg.deleteUser(new_user.id)


def test_update_user_email() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    req = UpdateUserRequest(email=email)
    user = cast(UserInfo, psg.updateUser(PASSAGE_USER_ID, req))
    assert user.email == email


def test_update_user_with_metadata() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    user = cast(UserInfo, psg.updateUser(PASSAGE_USER_ID, {"email": email, "user_metadata": {"example1": "qwe"}}))  # type: ignore[arg-type]
    assert user.email == email
    assert user.user_metadata["example1"] == "qwe"  # type: ignore[index]

    user = cast(UserInfo, psg.updateUser(PASSAGE_USER_ID, {"email": email, "user_metadata": {"example1": "asd"}}))  # type: ignore[arg-type]
    assert user.email == email
    assert user.user_metadata["example1"] == "asd"  # type: ignore[index]


def test_create_user_with_metadata() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    user = cast(UserInfo, psg.createUser({"email": email, "user_metadata": {"example1": "qwe"}}))  # type: ignore[arg-type]
    assert user.email == email
    assert user.user_metadata["example1"] == "qwe"  # type: ignore[index]
    assert psg.deleteUser(user.id)


def test_create_and_delete_user() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    new_user = cast(UserInfo, psg.createUser({"email": email}))  # type: ignore[arg-type]
    assert new_user.email == email
    assert psg.deleteUser(new_user.id)


def test_sign_out() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    assert psg.signOut(PASSAGE_USER_ID)


def test_revoke_user_refresh_tokens() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    assert psg.revokeUserRefreshTokens(PASSAGE_USER_ID)
