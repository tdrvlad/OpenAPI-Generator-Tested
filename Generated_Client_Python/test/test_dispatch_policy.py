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
import datetime

import openapi_client
from openapi_client.models.dispatch_policy import DispatchPolicy  # noqa: E501
from openapi_client.rest import ApiException

class TestDispatchPolicy(unittest.TestCase):
    """DispatchPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DispatchPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.dispatch_policy.DispatchPolicy()  # noqa: E501
        if include_optional :
            return DispatchPolicy(
                dispatch_policy_id = '0', 
                name = 'Fast', 
                number_of_users = 3, 
                media_item_lock_timeout = 10
            )
        else :
            return DispatchPolicy(
        )

    def testDispatchPolicy(self):
        """Test DispatchPolicy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
