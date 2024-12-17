import os

import pytest
from dotenv import load_dotenv
from faker import Faker

from passageidentity import PassageError
from passageidentity.models.magic_link_args import MagicLinkWithEmailArgs
from passageidentity.models.magic_link_options import MagicLinkOptions
from passageidentity.openapi_client.models.magic_link_type import MagicLinkType
from passageidentity.passage import Passage

load_dotenv()
f = Faker()

PASSAGE_USER_ID = os.environ.get("PASSAGE_USER_ID") or ""
PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID") or ""
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY") or ""
PASSAGE_AUTH_TOKEN = os.environ.get("PASSAGE_AUTH_TOKEN") or ""


def test_valid_jwt() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = psg.auth.validate_jwt(PASSAGE_AUTH_TOKEN)
    assert user == PASSAGE_USER_ID


def test_invalid_jwt() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    with pytest.raises(PassageError):
        psg.auth.validate_jwt("invalid_token")


def test_validate_jwt() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    user = psg.auth.validate_jwt(PASSAGE_AUTH_TOKEN)
    assert user == PASSAGE_USER_ID


def test_create_magic_link() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    args = MagicLinkWithEmailArgs(email="user@passage.id", link_type=MagicLinkType.LOGIN, send=True)
    opts = MagicLinkOptions(ttl=12)

    magic_link = psg.auth.create_magic_link(args, opts)
    assert magic_link.identifier == "user@passage.id"
    assert magic_link.ttl == 12


def test_smart_link_valid() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    args = MagicLinkWithEmailArgs(email=email, link_type=MagicLinkType.LOGIN, send=False)

    magic_link = psg.auth.create_magic_link(args)
    assert magic_link.identifier == email
    assert not magic_link.activated
