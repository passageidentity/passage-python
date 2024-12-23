"""Provides the Passage class for interacting with the Passage API."""

from __future__ import annotations

from passageidentity.auth import Auth
from passageidentity.errors import PassageError
from passageidentity.user import User


class Passage:
    """Passage class for interacting with the Passage API."""

    COOKIE_AUTH = 1
    HEADER_AUTH = 2

    def __init__(self, app_id: str, api_key: str = "", auth_strategy: int = COOKIE_AUTH) -> None:
        """Initialize a new Passage instance."""
        if not app_id:
            msg = "A Passage app ID is required. Please include {app_id=YOUR_APP_ID, api_key=YOUR_API_KEY}."
            raise PassageError(msg)

        self.app_id: str = app_id
        self.passage_apikey: str = api_key
        self.auth_strategy: int = auth_strategy
        self.request_headers = {"Authorization": f"Bearer {api_key}"}

        self.auth = Auth(app_id, self.request_headers)
        self.user = User(app_id, self.request_headers)
