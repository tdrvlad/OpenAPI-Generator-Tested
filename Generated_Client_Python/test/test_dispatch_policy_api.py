# coding: utf-8

"""
    DeepVISS TAG

    DeepVISS (Deep Vision Interoperability Specification Standard) allows several computer vision solutions to produce, consume and exchange events in the same format.  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: office@deepviss.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.dispatch_policy_api import DispatchPolicyApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDispatchPolicyApi(unittest.TestCase):
    """DispatchPolicyApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.dispatch_policy_api.DispatchPolicyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_dispatch_policy(self):
        """Test case for create_dispatch_policy

        Create a new dispatchPolicy.  # noqa: E501
        """
        pass

    def test_get_dispatch_policy_list(self):
        """Test case for get_dispatch_policy_list

        Retrieve list of dispatch policies  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
