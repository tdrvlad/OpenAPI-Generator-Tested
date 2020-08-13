# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.internal_subjective_opinion import InternalSubjectiveOpinion
from openapi_server.models.shape import Shape
from openapi_server import util

from openapi_server.models.internal_subjective_opinion import InternalSubjectiveOpinion  # noqa: E501
from openapi_server.models.shape import Shape  # noqa: E501

class Tag(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tag_id=None, submission_timestamp=None, node_type=None, geometry=None, task_id=None, internal_subjective_opinion=None):  # noqa: E501
        """Tag - a model defined in OpenAPI

        :param tag_id: The tag_id of this Tag.  # noqa: E501
        :type tag_id: str
        :param submission_timestamp: The submission_timestamp of this Tag.  # noqa: E501
        :type submission_timestamp: datetime
        :param node_type: The node_type of this Tag.  # noqa: E501
        :type node_type: str
        :param geometry: The geometry of this Tag.  # noqa: E501
        :type geometry: List[Shape]
        :param task_id: The task_id of this Tag.  # noqa: E501
        :type task_id: str
        :param internal_subjective_opinion: The internal_subjective_opinion of this Tag.  # noqa: E501
        :type internal_subjective_opinion: InternalSubjectiveOpinion
        """
        self.openapi_types = {
            'tag_id': str,
            'submission_timestamp': datetime,
            'node_type': str,
            'geometry': List[Shape],
            'task_id': str,
            'internal_subjective_opinion': InternalSubjectiveOpinion
        }

        self.attribute_map = {
            'tag_id': 'tagId',
            'submission_timestamp': 'submissionTimestamp',
            'node_type': 'nodeType',
            'geometry': 'geometry',
            'task_id': 'taskId',
            'internal_subjective_opinion': 'internalSubjectiveOpinion'
        }

        self._tag_id = tag_id
        self._submission_timestamp = submission_timestamp
        self._node_type = node_type
        self._geometry = geometry
        self._task_id = task_id
        self._internal_subjective_opinion = internal_subjective_opinion

    @classmethod
    def from_dict(cls, dikt) -> 'Tag':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Tag of this Tag.  # noqa: E501
        :rtype: Tag
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tag_id(self):
        """Gets the tag_id of this Tag.

        Alpha-numeric, unique id of tagged object  # noqa: E501

        :return: The tag_id of this Tag.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this Tag.

        Alpha-numeric, unique id of tagged object  # noqa: E501

        :param tag_id: The tag_id of this Tag.
        :type tag_id: str
        """

        self._tag_id = tag_id

    @property
    def submission_timestamp(self):
        """Gets the submission_timestamp of this Tag.

        Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00)  # noqa: E501

        :return: The submission_timestamp of this Tag.
        :rtype: datetime
        """
        return self._submission_timestamp

    @submission_timestamp.setter
    def submission_timestamp(self, submission_timestamp):
        """Sets the submission_timestamp of this Tag.

        Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00)  # noqa: E501

        :param submission_timestamp: The submission_timestamp of this Tag.
        :type submission_timestamp: datetime
        """

        self._submission_timestamp = submission_timestamp

    @property
    def node_type(self):
        """Gets the node_type of this Tag.

        What does the object that has been detected represent. Can be extended to discrete histogram of types.  # noqa: E501

        :return: The node_type of this Tag.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this Tag.

        What does the object that has been detected represent. Can be extended to discrete histogram of types.  # noqa: E501

        :param node_type: The node_type of this Tag.
        :type node_type: str
        """

        self._node_type = node_type

    @property
    def geometry(self):
        """Gets the geometry of this Tag.

        What are the shapes that compose the tag?  # noqa: E501

        :return: The geometry of this Tag.
        :rtype: List[Shape]
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this Tag.

        What are the shapes that compose the tag?  # noqa: E501

        :param geometry: The geometry of this Tag.
        :type geometry: List[Shape]
        """

        self._geometry = geometry

    @property
    def task_id(self):
        """Gets the task_id of this Tag.

        Alpha-numeric, unique id of task object  # noqa: E501

        :return: The task_id of this Tag.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this Tag.

        Alpha-numeric, unique id of task object  # noqa: E501

        :param task_id: The task_id of this Tag.
        :type task_id: str
        """

        self._task_id = task_id

    @property
    def internal_subjective_opinion(self):
        """Gets the internal_subjective_opinion of this Tag.


        :return: The internal_subjective_opinion of this Tag.
        :rtype: InternalSubjectiveOpinion
        """
        return self._internal_subjective_opinion

    @internal_subjective_opinion.setter
    def internal_subjective_opinion(self, internal_subjective_opinion):
        """Sets the internal_subjective_opinion of this Tag.


        :param internal_subjective_opinion: The internal_subjective_opinion of this Tag.
        :type internal_subjective_opinion: InternalSubjectiveOpinion
        """

        self._internal_subjective_opinion = internal_subjective_opinion