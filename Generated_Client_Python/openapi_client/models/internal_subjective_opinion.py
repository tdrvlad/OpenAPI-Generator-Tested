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


class InternalSubjectiveOpinion(object):
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
        'attributed_belief_numerator': 'int',
        'attributed_disbelief_numerator': 'int',
        'unattributed_uncertainty_numerator': 'int',
        'common_denominator': 'int',
        'base_rate_numerator': 'int'
    }

    attribute_map = {
        'opinion_emitter_id': 'opinionEmitterId',
        'opinion_reason_id': 'opinionReasonId',
        'attributed_belief_numerator': 'attributedBeliefNumerator',
        'attributed_disbelief_numerator': 'attributedDisbeliefNumerator',
        'unattributed_uncertainty_numerator': 'unattributedUncertaintyNumerator',
        'common_denominator': 'commonDenominator',
        'base_rate_numerator': 'baseRateNumerator'
    }

    def __init__(self, opinion_emitter_id=None, opinion_reason_id=None, attributed_belief_numerator=None, attributed_disbelief_numerator=None, unattributed_uncertainty_numerator=None, common_denominator=None, base_rate_numerator=None, local_vars_configuration=None):  # noqa: E501
        """InternalSubjectiveOpinion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._opinion_emitter_id = None
        self._opinion_reason_id = None
        self._attributed_belief_numerator = None
        self._attributed_disbelief_numerator = None
        self._unattributed_uncertainty_numerator = None
        self._common_denominator = None
        self._base_rate_numerator = None
        self.discriminator = None

        if opinion_emitter_id is not None:
            self.opinion_emitter_id = opinion_emitter_id
        if opinion_reason_id is not None:
            self.opinion_reason_id = opinion_reason_id
        if attributed_belief_numerator is not None:
            self.attributed_belief_numerator = attributed_belief_numerator
        if attributed_disbelief_numerator is not None:
            self.attributed_disbelief_numerator = attributed_disbelief_numerator
        if unattributed_uncertainty_numerator is not None:
            self.unattributed_uncertainty_numerator = unattributed_uncertainty_numerator
        if common_denominator is not None:
            self.common_denominator = common_denominator
        if base_rate_numerator is not None:
            self.base_rate_numerator = base_rate_numerator

    @property
    def opinion_emitter_id(self):
        """Gets the opinion_emitter_id of this InternalSubjectiveOpinion.  # noqa: E501

        Functional source, if any, for this opinion, such a specific condition   # noqa: E501

        :return: The opinion_emitter_id of this InternalSubjectiveOpinion.  # noqa: E501
        :rtype: str
        """
        return self._opinion_emitter_id

    @opinion_emitter_id.setter
    def opinion_emitter_id(self, opinion_emitter_id):
        """Sets the opinion_emitter_id of this InternalSubjectiveOpinion.

        Functional source, if any, for this opinion, such a specific condition   # noqa: E501

        :param opinion_emitter_id: The opinion_emitter_id of this InternalSubjectiveOpinion.  # noqa: E501
        :type: str
        """

        self._opinion_emitter_id = opinion_emitter_id

    @property
    def opinion_reason_id(self):
        """Gets the opinion_reason_id of this InternalSubjectiveOpinion.  # noqa: E501

        Reason evoked, invoked or inferred by source for this opinion.  # noqa: E501

        :return: The opinion_reason_id of this InternalSubjectiveOpinion.  # noqa: E501
        :rtype: str
        """
        return self._opinion_reason_id

    @opinion_reason_id.setter
    def opinion_reason_id(self, opinion_reason_id):
        """Sets the opinion_reason_id of this InternalSubjectiveOpinion.

        Reason evoked, invoked or inferred by source for this opinion.  # noqa: E501

        :param opinion_reason_id: The opinion_reason_id of this InternalSubjectiveOpinion.  # noqa: E501
        :type: str
        """

        self._opinion_reason_id = opinion_reason_id

    @property
    def attributed_belief_numerator(self):
        """Gets the attributed_belief_numerator of this InternalSubjectiveOpinion.  # noqa: E501

        Number, signed and additive, of fulfillment points out of total that are attributed to belief that the opinion is TRUE. belief mass (bx) numerator accumulator.  # noqa: E501

        :return: The attributed_belief_numerator of this InternalSubjectiveOpinion.  # noqa: E501
        :rtype: int
        """
        return self._attributed_belief_numerator

    @attributed_belief_numerator.setter
    def attributed_belief_numerator(self, attributed_belief_numerator):
        """Sets the attributed_belief_numerator of this InternalSubjectiveOpinion.

        Number, signed and additive, of fulfillment points out of total that are attributed to belief that the opinion is TRUE. belief mass (bx) numerator accumulator.  # noqa: E501

        :param attributed_belief_numerator: The attributed_belief_numerator of this InternalSubjectiveOpinion.  # noqa: E501
        :type: int
        """

        self._attributed_belief_numerator = attributed_belief_numerator

    @property
    def attributed_disbelief_numerator(self):
        """Gets the attributed_disbelief_numerator of this InternalSubjectiveOpinion.  # noqa: E501

        Number, signed and additive, of fulfillment points out of total that are attributed to belief that the opinion is FALSE. belief mass (dx) numerator accumulator  # noqa: E501

        :return: The attributed_disbelief_numerator of this InternalSubjectiveOpinion.  # noqa: E501
        :rtype: int
        """
        return self._attributed_disbelief_numerator

    @attributed_disbelief_numerator.setter
    def attributed_disbelief_numerator(self, attributed_disbelief_numerator):
        """Sets the attributed_disbelief_numerator of this InternalSubjectiveOpinion.

        Number, signed and additive, of fulfillment points out of total that are attributed to belief that the opinion is FALSE. belief mass (dx) numerator accumulator  # noqa: E501

        :param attributed_disbelief_numerator: The attributed_disbelief_numerator of this InternalSubjectiveOpinion.  # noqa: E501
        :type: int
        """

        self._attributed_disbelief_numerator = attributed_disbelief_numerator

    @property
    def unattributed_uncertainty_numerator(self):
        """Gets the unattributed_uncertainty_numerator of this InternalSubjectiveOpinion.  # noqa: E501

        Number, signed and additive, of fulfillment points out of total that are unattributed to either belief or disbelief and thus represent uncertainty. uncertainty mass (ux) numerator accumulator.  # noqa: E501

        :return: The unattributed_uncertainty_numerator of this InternalSubjectiveOpinion.  # noqa: E501
        :rtype: int
        """
        return self._unattributed_uncertainty_numerator

    @unattributed_uncertainty_numerator.setter
    def unattributed_uncertainty_numerator(self, unattributed_uncertainty_numerator):
        """Sets the unattributed_uncertainty_numerator of this InternalSubjectiveOpinion.

        Number, signed and additive, of fulfillment points out of total that are unattributed to either belief or disbelief and thus represent uncertainty. uncertainty mass (ux) numerator accumulator.  # noqa: E501

        :param unattributed_uncertainty_numerator: The unattributed_uncertainty_numerator of this InternalSubjectiveOpinion.  # noqa: E501
        :type: int
        """

        self._unattributed_uncertainty_numerator = unattributed_uncertainty_numerator

    @property
    def common_denominator(self):
        """Gets the common_denominator of this InternalSubjectiveOpinion.  # noqa: E501

        The normalizing factor (the common denominator) of uncertainty, belief and disbelief.  # noqa: E501

        :return: The common_denominator of this InternalSubjectiveOpinion.  # noqa: E501
        :rtype: int
        """
        return self._common_denominator

    @common_denominator.setter
    def common_denominator(self, common_denominator):
        """Sets the common_denominator of this InternalSubjectiveOpinion.

        The normalizing factor (the common denominator) of uncertainty, belief and disbelief.  # noqa: E501

        :param common_denominator: The common_denominator of this InternalSubjectiveOpinion.  # noqa: E501
        :type: int
        """

        self._common_denominator = common_denominator

    @property
    def base_rate_numerator(self):
        """Gets the base_rate_numerator of this InternalSubjectiveOpinion.  # noqa: E501

        The probability of the opinion being true in the absence of the information generating it; this represents the default probability of a an element or character or letter appearing in a specific context  # noqa: E501

        :return: The base_rate_numerator of this InternalSubjectiveOpinion.  # noqa: E501
        :rtype: int
        """
        return self._base_rate_numerator

    @base_rate_numerator.setter
    def base_rate_numerator(self, base_rate_numerator):
        """Sets the base_rate_numerator of this InternalSubjectiveOpinion.

        The probability of the opinion being true in the absence of the information generating it; this represents the default probability of a an element or character or letter appearing in a specific context  # noqa: E501

        :param base_rate_numerator: The base_rate_numerator of this InternalSubjectiveOpinion.  # noqa: E501
        :type: int
        """

        self._base_rate_numerator = base_rate_numerator

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
        if not isinstance(other, InternalSubjectiveOpinion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InternalSubjectiveOpinion):
            return True

        return self.to_dict() != other.to_dict()
