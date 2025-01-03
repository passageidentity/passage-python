"""Provides functions to make HTTP requests with optional API key authorization."""

from __future__ import annotations

from importlib import metadata

import requests

PACKAGE_VERSION = metadata.version("passage-identity")


def get_headers(api_key: str | None = None) -> dict[str, str]:
    """Create a new headers dict with the package version included."""
    headers = {"Passage-Version": f"passage-python {PACKAGE_VERSION}"}
    if api_key:
        headers["Authorization"] = "Bearer " + api_key

    return headers


def get(url: str, api_key: str | None = None) -> requests.Response:
    """Send a GET request with API key in Authorization header if provided."""
    return requests.get(url, headers=get_headers(api_key))  # noqa: S113
