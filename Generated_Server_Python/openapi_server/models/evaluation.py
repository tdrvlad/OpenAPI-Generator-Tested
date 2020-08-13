# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.subjective_opinion import SubjectiveOpinion
from openapi_server import util

from openapi_server.models.subjective_opinion import SubjectiveOpinion  # noqa: E501

class Evaluation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, confidence=None, subjective_opinion=None):  # noqa: E501
        """Evaluation - a model defined in OpenAPI

        :param confidence: The confidence of this Evaluation.  # noqa: E501
        :type confidence: float
        :param subjective_opinion: The subjective_opinion of this Evaluation.  # noqa: E501
        :type subjective_opinion: SubjectiveOpinion
        """
        self.openapi_types = {
            'confidence': float,
            'subjective_opinion': SubjectiveOpinion
        }

        self.attribute_map = {
            'confidence': 'confidence',
            'subjective_opinion': 'subjectiveOpinion'
        }

        self._confidence = confidence
        self._subjective_opinion = subjective_opinion

    @classmethod
    def from_dict(cls, dikt) -> 'Evaluation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Evaluation of this Evaluation.  # noqa: E501
        :rtype: Evaluation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def confidence(self):
        """Gets the confidence of this Evaluation.

        The confidence of the merged tag (from several tags), based on IoU (Intersection over Union) of the composing tags. The confidence is the reduce form of the SubjectiveOpinion, representing only its belief part.  # noqa: E501

        :return: The confidence of this Evaluation.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Evaluation.

        The confidence of the merged tag (from several tags), based on IoU (Intersection over Union) of the composing tags. The confidence is the reduce form of the SubjectiveOpinion, representing only its belief part.  # noqa: E501

        :param confidence: The confidence of this Evaluation.
        :type confidence: float
        """

        self._confidence = confidence

    @property
    def subjective_opinion(self):
        """Gets the subjective_opinion of this Evaluation.


        :return: The subjective_opinion of this Evaluation.
        :rtype: SubjectiveOpinion
        """
        return self._subjective_opinion

    @subjective_opinion.setter
    def subjective_opinion(self, subjective_opinion):
        """Sets the subjective_opinion of this Evaluation.


        :param subjective_opinion: The subjective_opinion of this Evaluation.
        :type subjective_opinion: SubjectiveOpinion
        """

        self._subjective_opinion = subjective_opinion