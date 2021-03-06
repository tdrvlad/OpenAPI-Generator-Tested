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
from openapi_client.models.shape2_d_polygon_all_of import Shape2DPolygonAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestShape2DPolygonAllOf(unittest.TestCase):
    """Shape2DPolygonAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Shape2DPolygonAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shape2_d_polygon_all_of.Shape2DPolygonAllOf()  # noqa: E501
        if include_optional :
            return Shape2DPolygonAllOf(
                points = [
                    openapi_client.models.point2_d.Point2D(
                        x = 56, 
                        y = 56, )
                    ]
            )
        else :
            return Shape2DPolygonAllOf(
        )

    def testShape2DPolygonAllOf(self):
        """Test Shape2DPolygonAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
