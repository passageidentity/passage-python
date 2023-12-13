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
import datetime

from openapi_client.models.update_user_request import UpdateUserRequest

class TestUpdateUserRequest(unittest.TestCase):
    """UpdateUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateUserRequest:
        """Test UpdateUserRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateUserRequest`
        """
        model = UpdateUserRequest()
        if include_optional:
            return UpdateUserRequest(
                email = '',
                phone = '',
                user_metadata = None
            )
        else:
            return UpdateUserRequest(
        )
        """

    def testUpdateUserRequest(self):
        """Test UpdateUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
