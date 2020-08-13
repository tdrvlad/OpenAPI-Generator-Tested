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
from openapi_client.models.shape2_d_rectangle_text_block import Shape2DRectangleTextBlock  # noqa: E501
from openapi_client.rest import ApiException

class TestShape2DRectangleTextBlock(unittest.TestCase):
    """Shape2DRectangleTextBlock unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Shape2DRectangleTextBlock
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shape2_d_rectangle_text_block.Shape2DRectangleTextBlock()  # noqa: E501
        if include_optional :
            return Shape2DRectangleTextBlock(
                transliteration = openapi_client.models.transliteration.Transliteration(
                    language_code = 'en', 
                    compressed_character_sequence = 'word', 
                    encoding = 'UTF-8', 
                    charset = 'latin1', 
                    direction = 'left-to-right', 
                    collation_language = 'utf8_romanian_ci', 
                    character_sequence = [
                        openapi_client.models.observable_symbol.ObservableSymbol(
                            superposed_character = [
                                openapi_client.models.latent_symbol.LatentSymbol(
                                    value = '0', 
                                    subjective_opinion = openapi_client.models.internal_subjective_opinion.InternalSubjectiveOpinion(
                                        opinion_emitter_id = 'ocr', 
                                        opinion_reason_id = 'unreadable', 
                                        attributed_belief_numerator = 5, 
                                        attributed_disbelief_numerator = 2, 
                                        unattributed_uncertainty_numerator = 1, 
                                        common_denominator = 1, 
                                        base_rate_numerator = 1, ), )
                                ], )
                        ], ), 
                style = openapi_client.models.style.Style(
                    font_style = 'serif', 
                    font_variant = 'serif', 
                    font_size = 12, 
                    font_color = '#030F01', )
            )
        else :
            return Shape2DRectangleTextBlock(
        )

    def testShape2DRectangleTextBlock(self):
        """Test Shape2DRectangleTextBlock"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
