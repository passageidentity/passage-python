import os

import pytest
from dotenv import load_dotenv
from faker import Faker

from passageidentity.errors import PassageError
from passageidentity.openapi_client.models.create_user_args import CreateUserArgs
from passageidentity.openapi_client.models.update_user_args import UpdateUserArgs
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
    args = CreateUserArgs(email=email)
    new_user = psg.user.create(args)
    assert new_user.email == email

    user_by_identifier = psg.user.get_by_identifier(email.upper())
    assert user_by_identifier.id == new_user.id

    user = psg.user.get(new_user.id)
    assert user.id == new_user.id

    assert user_by_identifier == user
    assert psg.user.delete(new_user.id) is None


def test_get_by_identifier_user_not_exist() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    with pytest.raises(PassageError, match="User not found."):
        psg.user.get_by_identifier("error@passage.id")


def test_get_user_info_valid() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = psg.user.get(PASSAGE_USER_ID)
    assert user.id == PASSAGE_USER_ID


def test_get_user_info_by_identifier_valid() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    args = CreateUserArgs(email=email)
    new_user = psg.user.create(args)
    assert new_user.email == email

    user_by_identifier = psg.user.get_by_identifier(email)
    assert user_by_identifier.id == new_user.id

    user = psg.user.get(new_user.id)
    assert user.id == new_user.id

    assert user_by_identifier == user
    assert psg.user.delete(new_user.id) is None


def test_get_user_info_by_identifier_phone_valid() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    phone = "+15005550030"
    args = CreateUserArgs(phone=phone)
    new_user = psg.user.create(args)
    assert new_user.phone == phone

    user_by_identifier = psg.user.get_by_identifier(phone)
    assert user_by_identifier.id == new_user.id

    user = psg.user.get(new_user.id)
    assert user.id == new_user.id

    assert user_by_identifier == user
    assert psg.user.delete(new_user.id) is None


def test_activate_user() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = psg.user.activate(PASSAGE_USER_ID)
    assert user.status == "active"


def test_deactivate_user() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    user = psg.user.get(PASSAGE_USER_ID)
    user = psg.user.deactivate(user.id)
    assert user.status == "inactive"


def test_list_user_devices() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    devices = psg.user.list_devices(PASSAGE_USER_ID)
    assert len(devices) == 2


def test_update_user_phone() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    phone = "+15005550021"
    args = CreateUserArgs(phone=phone)
    new_user = psg.user.create(args)

    phone = "+15005550022"
    update_args = UpdateUserArgs(phone=phone)
    user = psg.user.update(new_user.id, update_args)
    assert user.phone == phone
    assert psg.user.delete(new_user.id) is None


def test_update_user_email() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    req = UpdateUserArgs(email=email)
    user = psg.user.update(PASSAGE_USER_ID, req)
    assert user.email == email


def test_update_user_with_metadata() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    args = UpdateUserArgs(email=email, user_metadata={"example1": "qwe"})
    user = psg.user.update(PASSAGE_USER_ID, args)
    assert user.email == email
    assert user.user_metadata["example1"] == "qwe"  # type: ignore[index]

    args = UpdateUserArgs(email=email, user_metadata={"example1": "asd"})
    user = psg.user.update(PASSAGE_USER_ID, args)
    assert user.email == email
    assert user.user_metadata["example1"] == "asd"  # type: ignore[index]


def test_create_user_with_metadata() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    args = CreateUserArgs(email=email, user_metadata={"example1": "qwe"})
    user = psg.user.create(args)
    assert user.email == email
    assert user.user_metadata["example1"] == "qwe"  # type: ignore[index]
    assert psg.user.delete(user.id) is None


def test_create_and_delete_user() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    args = CreateUserArgs(email=email)
    new_user = psg.user.create(args)
    assert new_user.email == email
    assert psg.user.delete(new_user.id) is None


def test_revoke_user_refresh_tokens() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    assert psg.user.revoke_refresh_tokens(PASSAGE_USER_ID) is None
