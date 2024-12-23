"""Provides helper functions for interacting with the Passage Identity API."""

from http import HTTPStatus

from passageidentity import requests
from passageidentity.errors import PassageError


def fetch_app(app_id: str) -> dict:
    """Fetch the public key for the given app id from Passage."""
    # unauthenticated request to get the public key
    r = requests.get(f"https://api.passage.id/v1/apps/{app_id}")

    if r.status_code != HTTPStatus.OK:
        msg = f"Could not fetch app information for app id {app_id}"
        raise PassageError(msg)

    return r.json()["app"]
