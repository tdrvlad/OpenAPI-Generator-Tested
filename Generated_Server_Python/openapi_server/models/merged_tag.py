# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.evaluation import Evaluation
from openapi_server.models.permanent_identifier import PermanentIdentifier
from openapi_server.models.shape import Shape
from openapi_server import util

from openapi_server.models.evaluation import Evaluation  # noqa: E501
from openapi_server.models.permanent_identifier import PermanentIdentifier  # noqa: E501
from openapi_server.models.shape import Shape  # noqa: E501

class MergedTag(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, merged_tag_id=None, media_item_id=None, challenge_id=None, permanent_identifier=None, node_type=None, geometry=None, evaluation=None, composing_tags=None, evaluation_status=None):  # noqa: E501
        """MergedTag - a model defined in OpenAPI

        :param merged_tag_id: The merged_tag_id of this MergedTag.  # noqa: E501
        :type merged_tag_id: str
        :param media_item_id: The media_item_id of this MergedTag.  # noqa: E501
        :type media_item_id: str
        :param challenge_id: The challenge_id of this MergedTag.  # noqa: E501
        :type challenge_id: str
        :param permanent_identifier: The permanent_identifier of this MergedTag.  # noqa: E501
        :type permanent_identifier: PermanentIdentifier
        :param node_type: The node_type of this MergedTag.  # noqa: E501
        :type node_type: str
        :param geometry: The geometry of this MergedTag.  # noqa: E501
        :type geometry: List[Shape]
        :param evaluation: The evaluation of this MergedTag.  # noqa: E501
        :type evaluation: Evaluation
        :param composing_tags: The composing_tags of this MergedTag.  # noqa: E501
        :type composing_tags: List[str]
        :param evaluation_status: The evaluation_status of this MergedTag.  # noqa: E501
        :type evaluation_status: str
        """
        self.openapi_types = {
            'merged_tag_id': str,
            'media_item_id': str,
            'challenge_id': str,
            'permanent_identifier': PermanentIdentifier,
            'node_type': str,
            'geometry': List[Shape],
            'evaluation': Evaluation,
            'composing_tags': List[str],
            'evaluation_status': str
        }

        self.attribute_map = {
            'merged_tag_id': 'mergedTagId',
            'media_item_id': 'mediaItemId',
            'challenge_id': 'challengeId',
            'permanent_identifier': 'permanentIdentifier',
            'node_type': 'nodeType',
            'geometry': 'geometry',
            'evaluation': 'evaluation',
            'composing_tags': 'composingTags',
            'evaluation_status': 'evaluationStatus'
        }

        self._merged_tag_id = merged_tag_id
        self._media_item_id = media_item_id
        self._challenge_id = challenge_id
        self._permanent_identifier = permanent_identifier
        self._node_type = node_type
        self._geometry = geometry
        self._evaluation = evaluation
        self._composing_tags = composing_tags
        self._evaluation_status = evaluation_status

    @classmethod
    def from_dict(cls, dikt) -> 'MergedTag':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MergedTag of this MergedTag.  # noqa: E501
        :rtype: MergedTag
        """
        return util.deserialize_model(dikt, cls)

    @property
    def merged_tag_id(self):
        """Gets the merged_tag_id of this MergedTag.

        Alpha-numeric, unique id of tagged object  # noqa: E501

        :return: The merged_tag_id of this MergedTag.
        :rtype: str
        """
        return self._merged_tag_id

    @merged_tag_id.setter
    def merged_tag_id(self, merged_tag_id):
        """Sets the merged_tag_id of this MergedTag.

        Alpha-numeric, unique id of tagged object  # noqa: E501

        :param merged_tag_id: The merged_tag_id of this MergedTag.
        :type merged_tag_id: str
        """

        self._merged_tag_id = merged_tag_id

    @property
    def media_item_id(self):
        """Gets the media_item_id of this MergedTag.

        Alpha-numeric, unique id of tagged object  # noqa: E501

        :return: The media_item_id of this MergedTag.
        :rtype: str
        """
        return self._media_item_id

    @media_item_id.setter
    def media_item_id(self, media_item_id):
        """Sets the media_item_id of this MergedTag.

        Alpha-numeric, unique id of tagged object  # noqa: E501

        :param media_item_id: The media_item_id of this MergedTag.
        :type media_item_id: str
        """

        self._media_item_id = media_item_id

    @property
    def challenge_id(self):
        """Gets the challenge_id of this MergedTag.

        Alpha-numeric, unique id of tagged object  # noqa: E501

        :return: The challenge_id of this MergedTag.
        :rtype: str
        """
        return self._challenge_id

    @challenge_id.setter
    def challenge_id(self, challenge_id):
        """Sets the challenge_id of this MergedTag.

        Alpha-numeric, unique id of tagged object  # noqa: E501

        :param challenge_id: The challenge_id of this MergedTag.
        :type challenge_id: str
        """

        self._challenge_id = challenge_id

    @property
    def permanent_identifier(self):
        """Gets the permanent_identifier of this MergedTag.


        :return: The permanent_identifier of this MergedTag.
        :rtype: PermanentIdentifier
        """
        return self._permanent_identifier

    @permanent_identifier.setter
    def permanent_identifier(self, permanent_identifier):
        """Sets the permanent_identifier of this MergedTag.


        :param permanent_identifier: The permanent_identifier of this MergedTag.
        :type permanent_identifier: PermanentIdentifier
        """

        self._permanent_identifier = permanent_identifier

    @property
    def node_type(self):
        """Gets the node_type of this MergedTag.

        What type of object/event has been detected?  # noqa: E501

        :return: The node_type of this MergedTag.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this MergedTag.

        What type of object/event has been detected?  # noqa: E501

        :param node_type: The node_type of this MergedTag.
        :type node_type: str
        """

        self._node_type = node_type

    @property
    def geometry(self):
        """Gets the geometry of this MergedTag.

        What are the shapes that have been merged to determine this tag?  # noqa: E501

        :return: The geometry of this MergedTag.
        :rtype: List[Shape]
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this MergedTag.

        What are the shapes that have been merged to determine this tag?  # noqa: E501

        :param geometry: The geometry of this MergedTag.
        :type geometry: List[Shape]
        """

        self._geometry = geometry

    @property
    def evaluation(self):
        """Gets the evaluation of this MergedTag.


        :return: The evaluation of this MergedTag.
        :rtype: Evaluation
        """
        return self._evaluation

    @evaluation.setter
    def evaluation(self, evaluation):
        """Sets the evaluation of this MergedTag.


        :param evaluation: The evaluation of this MergedTag.
        :type evaluation: Evaluation
        """

        self._evaluation = evaluation

    @property
    def composing_tags(self):
        """Gets the composing_tags of this MergedTag.

        What are the tags which have been merged?  # noqa: E501

        :return: The composing_tags of this MergedTag.
        :rtype: List[str]
        """
        return self._composing_tags

    @composing_tags.setter
    def composing_tags(self, composing_tags):
        """Sets the composing_tags of this MergedTag.

        What are the tags which have been merged?  # noqa: E501

        :param composing_tags: The composing_tags of this MergedTag.
        :type composing_tags: List[str]
        """

        self._composing_tags = composing_tags

    @property
    def evaluation_status(self):
        """Gets the evaluation_status of this MergedTag.


        :return: The evaluation_status of this MergedTag.
        :rtype: str
        """
        return self._evaluation_status

    @evaluation_status.setter
    def evaluation_status(self, evaluation_status):
        """Sets the evaluation_status of this MergedTag.


        :param evaluation_status: The evaluation_status of this MergedTag.
        :type evaluation_status: str
        """
        allowed_values = ["passed", "failed", "incomplete"]  # noqa: E501
        if evaluation_status not in allowed_values:
            raise ValueError(
                "Invalid value for `evaluation_status` ({0}), must be one of {1}"
                .format(evaluation_status, allowed_values)
            )

        self._evaluation_status = evaluation_status
