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


class EvaluationPolicy(object):
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
        'evaluation_policy_id': 'str',
        'name': 'str',
        'spatial_overlap_threshold': 'float',
        'harshness': 'float',
        'rank_of_mean': 'float',
        'summation_type': 'str'
    }

    attribute_map = {
        'evaluation_policy_id': 'evaluationPolicyId',
        'name': 'name',
        'spatial_overlap_threshold': 'spatialOverlapThreshold',
        'harshness': 'harshness',
        'rank_of_mean': 'rankOfMean',
        'summation_type': 'summationType'
    }

    def __init__(self, evaluation_policy_id=None, name=None, spatial_overlap_threshold=None, harshness=None, rank_of_mean=None, summation_type=None, local_vars_configuration=None):  # noqa: E501
        """EvaluationPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._evaluation_policy_id = None
        self._name = None
        self._spatial_overlap_threshold = None
        self._harshness = None
        self._rank_of_mean = None
        self._summation_type = None
        self.discriminator = None

        if evaluation_policy_id is not None:
            self.evaluation_policy_id = evaluation_policy_id
        if name is not None:
            self.name = name
        if spatial_overlap_threshold is not None:
            self.spatial_overlap_threshold = spatial_overlap_threshold
        if harshness is not None:
            self.harshness = harshness
        if rank_of_mean is not None:
            self.rank_of_mean = rank_of_mean
        if summation_type is not None:
            self.summation_type = summation_type

    @property
    def evaluation_policy_id(self):
        """Gets the evaluation_policy_id of this EvaluationPolicy.  # noqa: E501

        Unique ID of evaluation policy  # noqa: E501

        :return: The evaluation_policy_id of this EvaluationPolicy.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_policy_id

    @evaluation_policy_id.setter
    def evaluation_policy_id(self, evaluation_policy_id):
        """Sets the evaluation_policy_id of this EvaluationPolicy.

        Unique ID of evaluation policy  # noqa: E501

        :param evaluation_policy_id: The evaluation_policy_id of this EvaluationPolicy.  # noqa: E501
        :type: str
        """

        self._evaluation_policy_id = evaluation_policy_id

    @property
    def name(self):
        """Gets the name of this EvaluationPolicy.  # noqa: E501

        name  # noqa: E501

        :return: The name of this EvaluationPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EvaluationPolicy.

        name  # noqa: E501

        :param name: The name of this EvaluationPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def spatial_overlap_threshold(self):
        """Gets the spatial_overlap_threshold of this EvaluationPolicy.  # noqa: E501

        The minimum amount of overlap between two tags, which, in conjuction with a matching object-type, is a condition for merging two tags  # noqa: E501

        :return: The spatial_overlap_threshold of this EvaluationPolicy.  # noqa: E501
        :rtype: float
        """
        return self._spatial_overlap_threshold

    @spatial_overlap_threshold.setter
    def spatial_overlap_threshold(self, spatial_overlap_threshold):
        """Sets the spatial_overlap_threshold of this EvaluationPolicy.

        The minimum amount of overlap between two tags, which, in conjuction with a matching object-type, is a condition for merging two tags  # noqa: E501

        :param spatial_overlap_threshold: The spatial_overlap_threshold of this EvaluationPolicy.  # noqa: E501
        :type: float
        """

        self._spatial_overlap_threshold = spatial_overlap_threshold

    @property
    def harshness(self):
        """Gets the harshness of this EvaluationPolicy.  # noqa: E501

        The penalty incurred for a tag that is NOT matched with other tags  # noqa: E501

        :return: The harshness of this EvaluationPolicy.  # noqa: E501
        :rtype: float
        """
        return self._harshness

    @harshness.setter
    def harshness(self, harshness):
        """Sets the harshness of this EvaluationPolicy.

        The penalty incurred for a tag that is NOT matched with other tags  # noqa: E501

        :param harshness: The harshness of this EvaluationPolicy.  # noqa: E501
        :type: float
        """

        self._harshness = harshness

    @property
    def rank_of_mean(self):
        """Gets the rank_of_mean of this EvaluationPolicy.  # noqa: E501

        The rank (power) of the generalized mean used for evaluating a task composed of several tags. Negative values mean harsher evaluations, values larger than 1.0 mean less harsh evaluations. Default value is 1.0 (arithmetic mean).   # noqa: E501

        :return: The rank_of_mean of this EvaluationPolicy.  # noqa: E501
        :rtype: float
        """
        return self._rank_of_mean

    @rank_of_mean.setter
    def rank_of_mean(self, rank_of_mean):
        """Sets the rank_of_mean of this EvaluationPolicy.

        The rank (power) of the generalized mean used for evaluating a task composed of several tags. Negative values mean harsher evaluations, values larger than 1.0 mean less harsh evaluations. Default value is 1.0 (arithmetic mean).   # noqa: E501

        :param rank_of_mean: The rank_of_mean of this EvaluationPolicy.  # noqa: E501
        :type: float
        """

        self._rank_of_mean = rank_of_mean

    @property
    def summation_type(self):
        """Gets the summation_type of this EvaluationPolicy.  # noqa: E501

        If set to 'algebraic', negative results on one task will be substracted from user payout.  # noqa: E501

        :return: The summation_type of this EvaluationPolicy.  # noqa: E501
        :rtype: str
        """
        return self._summation_type

    @summation_type.setter
    def summation_type(self, summation_type):
        """Sets the summation_type of this EvaluationPolicy.

        If set to 'algebraic', negative results on one task will be substracted from user payout.  # noqa: E501

        :param summation_type: The summation_type of this EvaluationPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["algebraic", "non-negative"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and summation_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `summation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(summation_type, allowed_values)
            )

        self._summation_type = summation_type

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
        if not isinstance(other, EvaluationPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EvaluationPolicy):
            return True

        return self.to_dict() != other.to_dict()
