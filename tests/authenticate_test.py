import os
from typing import cast

import pytest
from dotenv import load_dotenv
from faker import Faker

from passageidentity import PassageError
from passageidentity.openapi_client.models.app_info import AppInfo
from passageidentity.openapi_client.models.magic_link import MagicLink
from passageidentity.passage import Passage

load_dotenv()
f = Faker()

PASSAGE_USER_ID = os.environ.get("PASSAGE_USER_ID") or ""
PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID") or ""
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY") or ""
PASSAGE_AUTH_TOKEN = os.environ.get("PASSAGE_AUTH_TOKEN") or ""


def test_valid_jwt() -> None:
    psg = Passage(PASSAGE_APP_ID, auth_strategy=Passage.HEADER_AUTH)
    user = psg.authenticateJWT(PASSAGE_AUTH_TOKEN)
    assert user == PASSAGE_USER_ID


def test_invalid_jwt() -> None:
    psg = Passage(PASSAGE_APP_ID, auth_strategy=Passage.HEADER_AUTH)
    with pytest.raises(PassageError):
        psg.authenticateJWT("invalid_token")


def test_validate_jwt() -> None:
    psg = Passage(PASSAGE_APP_ID, auth_strategy=Passage.HEADER_AUTH)
    user = psg.validateJwt(PASSAGE_AUTH_TOKEN)
    assert user == PASSAGE_USER_ID


def test_get_app() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    app = cast(AppInfo, psg.getApp())
    assert app.id == PASSAGE_APP_ID


def test_create_magic_link() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
    magic_link = psg.createMagicLink(
        {
            "email": "chris@passage.id",
            "channel": "email",
            "ttl": 12,
        },  # type: ignore[arg-type]
    )
    assert magic_link.identifier == "chris@passage.id"  # type: ignore[attr-defined]
    assert magic_link.ttl == 12  # type: ignore[attr-defined]


def test_smart_link_valid() -> None:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)

    email = f.email()
    magic_link = cast(MagicLink, psg.createMagicLink({"email": email}))  # type: ignore[arg-type]
    assert magic_link.identifier == email
    assert not magic_link.activated
