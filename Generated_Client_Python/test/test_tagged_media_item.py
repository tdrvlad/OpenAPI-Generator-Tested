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
from openapi_client.models.tagged_media_item import TaggedMediaItem  # noqa: E501
from openapi_client.rest import ApiException

class TestTaggedMediaItem(unittest.TestCase):
    """TaggedMediaItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaggedMediaItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.tagged_media_item.TaggedMediaItem()  # noqa: E501
        if include_optional :
            return TaggedMediaItem(
                tagged_media_item_id = '7E43358680768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E', 
                media_item_id = '7E43358680768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E', 
                challenge_id = '7E43358680768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E', 
                composing_tasks = [
                    '0'
                    ], 
                merged_tags = [
                    openapi_client.models.merged_tag.MergedTag(
                        merged_tag_id = '7E43358680768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E', 
                        media_item_id = '7E43358680768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E', 
                        challenge_id = '7E43358680768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E', 
                        permanent_identifier = openapi_client.models.permanent_identifier.PermanentIdentifier(
                            hash_code = '0', 
                            segments = [
                                openapi_client.models.permanent_identifier_segment.PermanentIdentifierSegment(
                                    encoding = 'json-array', 
                                    index = 56, 
                                    weight = 1.337, 
                                    assignment_function = 'hashed-from-data', 
                                    value = '0', )
                                ], ), 
                        node_type = 'vehicle', 
                        geometry = [
                            openapi_client.models.shape.Shape(
                                shape_id = '791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E', 
                                shape_type = 'Shape2DReactangle', )
                            ], 
                        evaluation = openapi_client.models.evaluation.Evaluation(
                            confidence = 1.337, 
                            subjective_opinion = openapi_client.models.subjective_opinion.SubjectiveOpinion(
                                opinion_emitter_id = 'ocr', 
                                opinion_reason_id = 'unreadable', 
                                belief = 0.75, 
                                disbelief = 0.2, 
                                uncertainty = 0.1, 
                                base_rate_probability = 0.001, ), ), 
                        composing_tags = [
                            '0'
                            ], 
                        evaluation_status = 'passed', )
                    ], 
                image = openapi_client.models.image.Image(
                    image_url = '0', 
                    image_base64 = '0', 
                    image_content_type = '0', ), 
                merged_edges = [
                    openapi_client.models.edge.Edge(
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
                            base_rate_numerator = 1, ), )
                    ]
            )
        else :
            return TaggedMediaItem(
        )

    def testTaggedMediaItem(self):
        """Test TaggedMediaItem"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
