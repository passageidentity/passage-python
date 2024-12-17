"""Provides the Passage class for interacting with the Passage API."""

from passageidentity.auth import Auth
from passageidentity.user import User


class Passage:
    """Passage class for interacting with the Passage API."""

    def __init__(self, app_id: str, api_key: str) -> None:
        """Initialize a new Passage instance."""
        if not app_id:
            msg = "A Passage app ID is required. Please include (app_id=YOUR_APP_ID, api_key=YOUR_API_KEY)."
            raise ValueError(msg)

        if not api_key:
            msg = "A Passage API key is required. Please include (app_id=YOUR_APP_ID, api_key=YOUR_API_KEY)."
            raise ValueError(msg)

        request_headers = {"Authorization": f"Bearer {api_key}"}

        self.auth = Auth(app_id, request_headers)
        self.user = User(app_id, request_headers)
