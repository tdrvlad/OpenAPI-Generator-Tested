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
from openapi_client.models.shape import Shape  # noqa: E501
from openapi_client.rest import ApiException

class TestShape(unittest.TestCase):
    """Shape unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Shape
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shape.Shape()  # noqa: E501
        if include_optional :
            return Shape(
                shape_id = '791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E', 
                shape_type = 'Shape2DReactangle'
            )
        else :
            return Shape(
                shape_id = '791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E',
                shape_type = 'Shape2DReactangle',
        )

    def testShape(self):
        """Test Shape"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
