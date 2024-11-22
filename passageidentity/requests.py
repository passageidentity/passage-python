"""Provides functions to make HTTP requests with optional API key authorization."""

from __future__ import annotations

import json
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


def post(url: str, api_key: str | None = None, data: dict | None = None) -> requests.Response:
    """Send a POST request with API key in Authorization header if provided, and the JSON-encoded data in the body."""
    return requests.post(  # noqa: S113
        url,
        headers=get_headers(api_key),
        data=json.dumps(data) if data else None,
    )


def patch(url: str, api_key: str | None = None, data: dict | None = None) -> requests.Response:
    """Send a PATCH request with API key in Authorization header if provided, and the JSON-encoded data in the body."""
    return requests.patch(  # noqa: S113
        url,
        headers=get_headers(api_key),
        data=json.dumps(data) if data else None,
    )


def delete(url: str, api_key: str | None = None) -> requests.Response:
    """Send a DELETE request with API key in Authorization header if provided."""
    return requests.delete(url, headers=get_headers(api_key))  # noqa: S113
