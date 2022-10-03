import json
import requests
import sys

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata

PACKAGE_VERSION = metadata.version("passage-identity")


def get_headers(api_key=None):
    """Creates a new headers dict, with the package version included.

    :returns: dict

    """
    headers = {"Passage-Version": f"passage-python {PACKAGE_VERSION}"}
    if api_key:
        headers["Authorization"] = "Bearer " + api_key

    return headers


def get(url, api_key=None):
    """Creates GET request, with API key in Authorization header if provided.

    :url: string
    :api_key: string
    :returns: requests.Response

    """
    return requests.get(url, headers=get_headers(api_key))


def post(url, api_key=None, data=None):
    """Creates POST request, with API key in Authorization header if provided, and the JSON-encoded data in the body.

    :url: string
    :api_key: string
    :data: dict
    :returns: requests.Response

    """
    return requests.post(
        url, headers=get_headers(api_key), data=json.dumps(data) if data else None
    )


def patch(url, api_key=None, data=None):
    """Creates PATCH request, with API key in Authorization header if provided, and the JSON-encoded data in the body.

    :url: string
    :api_key: string
    :data: dict
    :returns: requests.Response

    """
    return requests.patch(
        url, headers=get_headers(api_key), data=json.dumps(data) if data else None
    )


def delete(url, api_key=None):
    """Creates DELETE request, with API key in Authorization header if provided.

    :url: string
    :api_key: string
    :returns: requests.Response

    """
    return requests.delete(url, headers=get_headers(api_key))
