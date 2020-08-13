# coding: utf-8

"""
    DeepVISS TAG

    DeepVISS (Deep Vision Interoperability Specification Standard) allows several computer vision solutions to produce, consume and exchange events in the same format.  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: office@deepviss.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class SubjectiveOpinion(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'opinion_emitter_id': 'str',
        'opinion_reason_id': 'str',
        'belief': 'float',
        'disbelief': 'float',
        'uncertainty': 'float',
        'base_rate_probability': 'float'
    }

    attribute_map = {
        'opinion_emitter_id': 'opinionEmitterId',
        'opinion_reason_id': 'opinionReasonId',
        'belief': 'belief',
        'disbelief': 'disbelief',
        'uncertainty': 'uncertainty',
        'base_rate_probability': 'baseRateProbability'
    }

    def __init__(self, opinion_emitter_id=None, opinion_reason_id=None, belief=None, disbelief=None, uncertainty=None, base_rate_probability=None, local_vars_configuration=None):  # noqa: E501
        """SubjectiveOpinion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._opinion_emitter_id = None
        self._opinion_reason_id = None
        self._belief = None
        self._disbelief = None
        self._uncertainty = None
        self._base_rate_probability = None
        self.discriminator = None

        if opinion_emitter_id is not None:
            self.opinion_emitter_id = opinion_emitter_id
        if opinion_reason_id is not None:
            self.opinion_reason_id = opinion_reason_id
        if belief is not None:
            self.belief = belief
        if disbelief is not None:
            self.disbelief = disbelief
        if uncertainty is not None:
            self.uncertainty = uncertainty
        if base_rate_probability is not None:
            self.base_rate_probability = base_rate_probability

    @property
    def opinion_emitter_id(self):
        """Gets the opinion_emitter_id of this SubjectiveOpinion.  # noqa: E501

        Functional source, if any, for this opinion, such a specific condition or internal state encoutered. May be empty.  # noqa: E501

        :return: The opinion_emitter_id of this SubjectiveOpinion.  # noqa: E501
        :rtype: str
        """
        return self._opinion_emitter_id

    @opinion_emitter_id.setter
    def opinion_emitter_id(self, opinion_emitter_id):
        """Sets the opinion_emitter_id of this SubjectiveOpinion.

        Functional source, if any, for this opinion, such a specific condition or internal state encoutered. May be empty.  # noqa: E501

        :param opinion_emitter_id: The opinion_emitter_id of this SubjectiveOpinion.  # noqa: E501
        :type: str
        """

        self._opinion_emitter_id = opinion_emitter_id

    @property
    def opinion_reason_id(self):
        """Gets the opinion_reason_id of this SubjectiveOpinion.  # noqa: E501

        Reason evoked, invoked or inferred by source for this opinion. May be empty.  # noqa: E501

        :return: The opinion_reason_id of this SubjectiveOpinion.  # noqa: E501
        :rtype: str
        """
        return self._opinion_reason_id

    @opinion_reason_id.setter
    def opinion_reason_id(self, opinion_reason_id):
        """Sets the opinion_reason_id of this SubjectiveOpinion.

        Reason evoked, invoked or inferred by source for this opinion. May be empty.  # noqa: E501

        :param opinion_reason_id: The opinion_reason_id of this SubjectiveOpinion.  # noqa: E501
        :type: str
        """

        self._opinion_reason_id = opinion_reason_id

    @property
    def belief(self):
        """Gets the belief of this SubjectiveOpinion.  # noqa: E501

        attributed to belief that the opinion is TRUE. belief mass (bx) normalized.  # noqa: E501

        :return: The belief of this SubjectiveOpinion.  # noqa: E501
        :rtype: float
        """
        return self._belief

    @belief.setter
    def belief(self, belief):
        """Sets the belief of this SubjectiveOpinion.

        attributed to belief that the opinion is TRUE. belief mass (bx) normalized.  # noqa: E501

        :param belief: The belief of this SubjectiveOpinion.  # noqa: E501
        :type: float
        """

        self._belief = belief

    @property
    def disbelief(self):
        """Gets the disbelief of this SubjectiveOpinion.  # noqa: E501

        attributed to belief that the opinion is FALSE. disbelief mass (dx)  normalized  # noqa: E501

        :return: The disbelief of this SubjectiveOpinion.  # noqa: E501
        :rtype: float
        """
        return self._disbelief

    @disbelief.setter
    def disbelief(self, disbelief):
        """Sets the disbelief of this SubjectiveOpinion.

        attributed to belief that the opinion is FALSE. disbelief mass (dx)  normalized  # noqa: E501

        :param disbelief: The disbelief of this SubjectiveOpinion.  # noqa: E501
        :type: float
        """

        self._disbelief = disbelief

    @property
    def uncertainty(self):
        """Gets the uncertainty of this SubjectiveOpinion.  # noqa: E501

        unattributed to either belief or disbelief and thus represent uncertainty. uncertainty mass (ux) normalized.  # noqa: E501

        :return: The uncertainty of this SubjectiveOpinion.  # noqa: E501
        :rtype: float
        """
        return self._uncertainty

    @uncertainty.setter
    def uncertainty(self, uncertainty):
        """Sets the uncertainty of this SubjectiveOpinion.

        unattributed to either belief or disbelief and thus represent uncertainty. uncertainty mass (ux) normalized.  # noqa: E501

        :param uncertainty: The uncertainty of this SubjectiveOpinion.  # noqa: E501
        :type: float
        """

        self._uncertainty = uncertainty

    @property
    def base_rate_probability(self):
        """Gets the base_rate_probability of this SubjectiveOpinion.  # noqa: E501

        The probability of the opinion being true in the absence of the information generating it.  # noqa: E501

        :return: The base_rate_probability of this SubjectiveOpinion.  # noqa: E501
        :rtype: float
        """
        return self._base_rate_probability

    @base_rate_probability.setter
    def base_rate_probability(self, base_rate_probability):
        """Sets the base_rate_probability of this SubjectiveOpinion.

        The probability of the opinion being true in the absence of the information generating it.  # noqa: E501

        :param base_rate_probability: The base_rate_probability of this SubjectiveOpinion.  # noqa: E501
        :type: float
        """

        self._base_rate_probability = base_rate_probability

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubjectiveOpinion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubjectiveOpinion):
            return True

        return self.to_dict() != other.to_dict()