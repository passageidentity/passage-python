# coding: utf-8

"""
    Passage Management API

    Passage's management API to manage your Passage apps and users.

    The version of the OpenAPI document: 1
    Contact: support@passage.id
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.tokens_api import TokensApi


class TestTokensApi(unittest.TestCase):
    """TokensApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TokensApi()

    def tearDown(self) -> None:
        pass

    def test_revoke_user_refresh_tokens(self) -> None:
        """Test case for revoke_user_refresh_tokens

        Revokes refresh tokens
        """
        pass


if __name__ == '__main__':
    unittest.main()
