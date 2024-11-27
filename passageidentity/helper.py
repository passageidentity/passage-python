"""Provides helper functions for interacting with the Passage Identity API."""

import re
from http import HTTPStatus

from requests.sessions import Request

from passageidentity import requests
from passageidentity.errors import PassageError

BEARER_PATTERN = r"Bearer ([^\s,]+)"
BASE_URL = "https://api.passage.id/v1/apps/"


def extract_token(auth_header: str) -> str:
    """Extract the JWT from an Authorization header."""
    expression = re.escape(BEARER_PATTERN)
    match = re.search(expression, auth_header)

    if match:
        return match.group(1)

    msg = "No Passage authorization header."
    raise PassageError(msg)


def get_auth_token_from_request(request: Request, auth_strategy: int) -> str:
    """Get the auth token from a request.

    Checks the Authorization header first, then the psg_auth_token cookie.
    """
    if auth_strategy == 2:  # noqa: PLR2004
        auth_header = request.headers["Authorization"]
        expression = re.escape(BEARER_PATTERN)
        match = re.search(expression, auth_header)

        if match:
            return match.group(1)

        msg = "No Passage authorization header."
        raise PassageError(msg)

    if "psg_auth_token" not in request.cookies:
        msg = "No Passage authentication token."
        raise PassageError(msg)

    return request.cookies["psg_auth_token"]


def fetch_app(app_id: str) -> dict:
    """Fetch the public key for the given app id from Passage."""
    # unauthenticated request to get the public key
    r = requests.get(BASE_URL + app_id)

    if r.status_code != HTTPStatus.OK:
        raise PassageError("Could not fetch app information for app id " + app_id)

    return r.json()["app"]
