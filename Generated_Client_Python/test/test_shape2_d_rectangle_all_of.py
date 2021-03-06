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
from openapi_client.models.shape2_d_rectangle_all_of import Shape2DRectangleAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestShape2DRectangleAllOf(unittest.TestCase):
    """Shape2DRectangleAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Shape2DRectangleAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shape2_d_rectangle_all_of.Shape2DRectangleAllOf()  # noqa: E501
        if include_optional :
            return Shape2DRectangleAllOf(
                top = 145, 
                left = 182, 
                right = 295, 
                bottom = 244
            )
        else :
            return Shape2DRectangleAllOf(
        )

    def testShape2DRectangleAllOf(self):
        """Test Shape2DRectangleAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
