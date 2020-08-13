# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class EvaluationPolicy(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, evaluation_policy_id=None, name=None, spatial_overlap_threshold=None, harshness=None, rank_of_mean=None, summation_type=None):  # noqa: E501
        """EvaluationPolicy - a model defined in OpenAPI

        :param evaluation_policy_id: The evaluation_policy_id of this EvaluationPolicy.  # noqa: E501
        :type evaluation_policy_id: str
        :param name: The name of this EvaluationPolicy.  # noqa: E501
        :type name: str
        :param spatial_overlap_threshold: The spatial_overlap_threshold of this EvaluationPolicy.  # noqa: E501
        :type spatial_overlap_threshold: float
        :param harshness: The harshness of this EvaluationPolicy.  # noqa: E501
        :type harshness: float
        :param rank_of_mean: The rank_of_mean of this EvaluationPolicy.  # noqa: E501
        :type rank_of_mean: float
        :param summation_type: The summation_type of this EvaluationPolicy.  # noqa: E501
        :type summation_type: str
        """
        self.openapi_types = {
            'evaluation_policy_id': str,
            'name': str,
            'spatial_overlap_threshold': float,
            'harshness': float,
            'rank_of_mean': float,
            'summation_type': str
        }

        self.attribute_map = {
            'evaluation_policy_id': 'evaluationPolicyId',
            'name': 'name',
            'spatial_overlap_threshold': 'spatialOverlapThreshold',
            'harshness': 'harshness',
            'rank_of_mean': 'rankOfMean',
            'summation_type': 'summationType'
        }

        self._evaluation_policy_id = evaluation_policy_id
        self._name = name
        self._spatial_overlap_threshold = spatial_overlap_threshold
        self._harshness = harshness
        self._rank_of_mean = rank_of_mean
        self._summation_type = summation_type

    @classmethod
    def from_dict(cls, dikt) -> 'EvaluationPolicy':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EvaluationPolicy of this EvaluationPolicy.  # noqa: E501
        :rtype: EvaluationPolicy
        """
        return util.deserialize_model(dikt, cls)

    @property
    def evaluation_policy_id(self):
        """Gets the evaluation_policy_id of this EvaluationPolicy.

        Unique ID of evaluation policy  # noqa: E501

        :return: The evaluation_policy_id of this EvaluationPolicy.
        :rtype: str
        """
        return self._evaluation_policy_id

    @evaluation_policy_id.setter
    def evaluation_policy_id(self, evaluation_policy_id):
        """Sets the evaluation_policy_id of this EvaluationPolicy.

        Unique ID of evaluation policy  # noqa: E501

        :param evaluation_policy_id: The evaluation_policy_id of this EvaluationPolicy.
        :type evaluation_policy_id: str
        """

        self._evaluation_policy_id = evaluation_policy_id

    @property
    def name(self):
        """Gets the name of this EvaluationPolicy.

        name  # noqa: E501

        :return: The name of this EvaluationPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EvaluationPolicy.

        name  # noqa: E501

        :param name: The name of this EvaluationPolicy.
        :type name: str
        """

        self._name = name

    @property
    def spatial_overlap_threshold(self):
        """Gets the spatial_overlap_threshold of this EvaluationPolicy.

        The minimum amount of overlap between two tags, which, in conjuction with a matching object-type, is a condition for merging two tags  # noqa: E501

        :return: The spatial_overlap_threshold of this EvaluationPolicy.
        :rtype: float
        """
        return self._spatial_overlap_threshold

    @spatial_overlap_threshold.setter
    def spatial_overlap_threshold(self, spatial_overlap_threshold):
        """Sets the spatial_overlap_threshold of this EvaluationPolicy.

        The minimum amount of overlap between two tags, which, in conjuction with a matching object-type, is a condition for merging two tags  # noqa: E501

        :param spatial_overlap_threshold: The spatial_overlap_threshold of this EvaluationPolicy.
        :type spatial_overlap_threshold: float
        """

        self._spatial_overlap_threshold = spatial_overlap_threshold

    @property
    def harshness(self):
        """Gets the harshness of this EvaluationPolicy.

        The penalty incurred for a tag that is NOT matched with other tags  # noqa: E501

        :return: The harshness of this EvaluationPolicy.
        :rtype: float
        """
        return self._harshness

    @harshness.setter
    def harshness(self, harshness):
        """Sets the harshness of this EvaluationPolicy.

        The penalty incurred for a tag that is NOT matched with other tags  # noqa: E501

        :param harshness: The harshness of this EvaluationPolicy.
        :type harshness: float
        """

        self._harshness = harshness

    @property
    def rank_of_mean(self):
        """Gets the rank_of_mean of this EvaluationPolicy.

        The rank (power) of the generalized mean used for evaluating a task composed of several tags. Negative values mean harsher evaluations, values larger than 1.0 mean less harsh evaluations. Default value is 1.0 (arithmetic mean).   # noqa: E501

        :return: The rank_of_mean of this EvaluationPolicy.
        :rtype: float
        """
        return self._rank_of_mean

    @rank_of_mean.setter
    def rank_of_mean(self, rank_of_mean):
        """Sets the rank_of_mean of this EvaluationPolicy.

        The rank (power) of the generalized mean used for evaluating a task composed of several tags. Negative values mean harsher evaluations, values larger than 1.0 mean less harsh evaluations. Default value is 1.0 (arithmetic mean).   # noqa: E501

        :param rank_of_mean: The rank_of_mean of this EvaluationPolicy.
        :type rank_of_mean: float
        """

        self._rank_of_mean = rank_of_mean

    @property
    def summation_type(self):
        """Gets the summation_type of this EvaluationPolicy.

        If set to 'algebraic', negative results on one task will be substracted from user payout.  # noqa: E501

        :return: The summation_type of this EvaluationPolicy.
        :rtype: str
        """
        return self._summation_type

    @summation_type.setter
    def summation_type(self, summation_type):
        """Sets the summation_type of this EvaluationPolicy.

        If set to 'algebraic', negative results on one task will be substracted from user payout.  # noqa: E501

        :param summation_type: The summation_type of this EvaluationPolicy.
        :type summation_type: str
        """
        allowed_values = ["algebraic", "non-negative"]  # noqa: E501
        if summation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `summation_type` ({0}), must be one of {1}"
                .format(summation_type, allowed_values)
            )

        self._summation_type = summation_type
