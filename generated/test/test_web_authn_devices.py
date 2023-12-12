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

from openapi_client.models.web_authn_devices import WebAuthnDevices

class TestWebAuthnDevices(unittest.TestCase):
    """WebAuthnDevices unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebAuthnDevices:
        """Test WebAuthnDevices
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebAuthnDevices`
        """
        model = WebAuthnDevices()
        if include_optional:
            return WebAuthnDevices(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                cred_id = '',
                friendly_name = '',
                id = '',
                last_login_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type = 'passkey',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                usage_count = 56,
                icons = openapi_client.models.web_authn_icons.WebAuthnIcons(
                    light = '', 
                    dark = '', )
            )
        else:
            return WebAuthnDevices(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                cred_id = '',
                friendly_name = '',
                id = '',
                last_login_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type = 'passkey',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                usage_count = 56,
                icons = openapi_client.models.web_authn_icons.WebAuthnIcons(
                    light = '', 
                    dark = '', ),
        )
        """

    def testWebAuthnDevices(self):
        """Test WebAuthnDevices"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
