import requests
import sys

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata

PACKAGE_VERSION = metadata.version("passageidentity")

def get_headers():
    """Creates a new headers dict, with the package version included.

    :returns: dict

    """
    return {"Passage-Version": f'passage-python {PACKAGE_VERSION}')}

def get(url, api_key=None):
    """Creates GET request, with API key in Authorization header if provided.

    :url: string
    :api_key: string
    :returns: requests.Response

    """
    headers = get_headers()
    if api_key:
        headers["Authorization"] = "Bearer " + api_key

    return requests.get(url, headers=headers)

def post(url, api_key=None, data=None):
    """Creates POST request, with API key in Authorization header if provided, and the JSON-encoded data in the body.

    :url: string
    :api_key: string
    :data: dict
    :returns: requests.Response

    """
    headers = get_headers()
    if api_key:
        headers["Authorization"] = "Bearer " + api_key

    return requests.post(url, headers=headers, data=json.dumps(data) if data else None)

def patch(url, api_key=None, data=None):
    """Creates PATCH request, with API key in Authorization header if provided, and the JSON-encoded data in the body.

    :url: string
    :api_key: string
    :data: dict
    :returns: requests.Response

    """
    headers = get_headers()
    if api_key:
        headers["Authorization"] = "Bearer " + api_key

    return requests.patch(url, headers=headers, data=json.dumps(data) if data else None)

def delete(url, api_key=None):
    """Creates DELETE request, with API key in Authorization header if provided.

    :url: string
    :api_key: string
    :returns: requests.Response

    """
    headers = get_headers()
    if api_key:
        headers["Authorization"] = "Bearer " + api_key

    return requests.delete(url, headers=headers)
