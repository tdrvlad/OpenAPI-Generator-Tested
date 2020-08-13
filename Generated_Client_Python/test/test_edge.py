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
from openapi_client.models.edge import Edge  # noqa: E501
from openapi_client.rest import ApiException

class TestEdge(unittest.TestCase):
    """Edge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Edge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.edge.Edge()  # noqa: E501
        if include_optional :
            return Edge(
                source_tag_id = '87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E', 
                destination_tag_id = '7300124455B07E91CB289F87791D78064ECC93754F19B13D419489F1', 
                source_text_box_id = '1', 
                destination_text_box_id = '1', 
                edge_type = 'has-greater-area', 
                slack = 0.0, 
                elasticity = 1.337, 
                internal_subjective_opinion = openapi_client.models.internal_subjective_opinion.InternalSubjectiveOpinion(
                    opinion_emitter_id = 'ocr', 
                    opinion_reason_id = 'unreadable', 
                    attributed_belief_numerator = 5, 
                    attributed_disbelief_numerator = 2, 
                    unattributed_uncertainty_numerator = 1, 
                    common_denominator = 1, 
                    base_rate_numerator = 1, )
            )
        else :
            return Edge(
        )

    def testEdge(self):
        """Test Edge"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
