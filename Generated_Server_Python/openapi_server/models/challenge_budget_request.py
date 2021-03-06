# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.shape_type_enum import ShapeTypeEnum
from openapi_server import util

from openapi_server.models.shape_type_enum import ShapeTypeEnum  # noqa: E501

class ChallengeBudgetRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dataset_id=None, evaluation_policy_id=None, dispatch_policy_id=None, tag_type=None, estimated_tags_per_media_item=None):  # noqa: E501
        """ChallengeBudgetRequest - a model defined in OpenAPI

        :param dataset_id: The dataset_id of this ChallengeBudgetRequest.  # noqa: E501
        :type dataset_id: str
        :param evaluation_policy_id: The evaluation_policy_id of this ChallengeBudgetRequest.  # noqa: E501
        :type evaluation_policy_id: str
        :param dispatch_policy_id: The dispatch_policy_id of this ChallengeBudgetRequest.  # noqa: E501
        :type dispatch_policy_id: str
        :param tag_type: The tag_type of this ChallengeBudgetRequest.  # noqa: E501
        :type tag_type: ShapeTypeEnum
        :param estimated_tags_per_media_item: The estimated_tags_per_media_item of this ChallengeBudgetRequest.  # noqa: E501
        :type estimated_tags_per_media_item: float
        """
        self.openapi_types = {
            'dataset_id': str,
            'evaluation_policy_id': str,
            'dispatch_policy_id': str,
            'tag_type': ShapeTypeEnum,
            'estimated_tags_per_media_item': float
        }

        self.attribute_map = {
            'dataset_id': 'datasetId',
            'evaluation_policy_id': 'evaluationPolicyId',
            'dispatch_policy_id': 'dispatchPolicyId',
            'tag_type': 'tagType',
            'estimated_tags_per_media_item': 'estimatedTagsPerMediaItem'
        }

        self._dataset_id = dataset_id
        self._evaluation_policy_id = evaluation_policy_id
        self._dispatch_policy_id = dispatch_policy_id
        self._tag_type = tag_type
        self._estimated_tags_per_media_item = estimated_tags_per_media_item

    @classmethod
    def from_dict(cls, dikt) -> 'ChallengeBudgetRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChallengeBudgetRequest of this ChallengeBudgetRequest.  # noqa: E501
        :rtype: ChallengeBudgetRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dataset_id(self):
        """Gets the dataset_id of this ChallengeBudgetRequest.

        [TBD] Alpha-numeric, unique id of dataset  # noqa: E501

        :return: The dataset_id of this ChallengeBudgetRequest.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this ChallengeBudgetRequest.

        [TBD] Alpha-numeric, unique id of dataset  # noqa: E501

        :param dataset_id: The dataset_id of this ChallengeBudgetRequest.
        :type dataset_id: str
        """

        self._dataset_id = dataset_id

    @property
    def evaluation_policy_id(self):
        """Gets the evaluation_policy_id of this ChallengeBudgetRequest.

        Alpha-numeric, unique id of evaluation policy  # noqa: E501

        :return: The evaluation_policy_id of this ChallengeBudgetRequest.
        :rtype: str
        """
        return self._evaluation_policy_id

    @evaluation_policy_id.setter
    def evaluation_policy_id(self, evaluation_policy_id):
        """Sets the evaluation_policy_id of this ChallengeBudgetRequest.

        Alpha-numeric, unique id of evaluation policy  # noqa: E501

        :param evaluation_policy_id: The evaluation_policy_id of this ChallengeBudgetRequest.
        :type evaluation_policy_id: str
        """

        self._evaluation_policy_id = evaluation_policy_id

    @property
    def dispatch_policy_id(self):
        """Gets the dispatch_policy_id of this ChallengeBudgetRequest.

        Alpha-numeric, unique id of dispatch policy  # noqa: E501

        :return: The dispatch_policy_id of this ChallengeBudgetRequest.
        :rtype: str
        """
        return self._dispatch_policy_id

    @dispatch_policy_id.setter
    def dispatch_policy_id(self, dispatch_policy_id):
        """Sets the dispatch_policy_id of this ChallengeBudgetRequest.

        Alpha-numeric, unique id of dispatch policy  # noqa: E501

        :param dispatch_policy_id: The dispatch_policy_id of this ChallengeBudgetRequest.
        :type dispatch_policy_id: str
        """

        self._dispatch_policy_id = dispatch_policy_id

    @property
    def tag_type(self):
        """Gets the tag_type of this ChallengeBudgetRequest.


        :return: The tag_type of this ChallengeBudgetRequest.
        :rtype: ShapeTypeEnum
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        """Sets the tag_type of this ChallengeBudgetRequest.


        :param tag_type: The tag_type of this ChallengeBudgetRequest.
        :type tag_type: ShapeTypeEnum
        """

        self._tag_type = tag_type

    @property
    def estimated_tags_per_media_item(self):
        """Gets the estimated_tags_per_media_item of this ChallengeBudgetRequest.

        estimated Tags Per Media Item  # noqa: E501

        :return: The estimated_tags_per_media_item of this ChallengeBudgetRequest.
        :rtype: float
        """
        return self._estimated_tags_per_media_item

    @estimated_tags_per_media_item.setter
    def estimated_tags_per_media_item(self, estimated_tags_per_media_item):
        """Sets the estimated_tags_per_media_item of this ChallengeBudgetRequest.

        estimated Tags Per Media Item  # noqa: E501

        :param estimated_tags_per_media_item: The estimated_tags_per_media_item of this ChallengeBudgetRequest.
        :type estimated_tags_per_media_item: float
        """

        self._estimated_tags_per_media_item = estimated_tags_per_media_item
