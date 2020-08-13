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


class Tag(object):
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
        'tag_id': 'str',
        'submission_timestamp': 'datetime',
        'node_type': 'str',
        'geometry': 'list[Shape]',
        'task_id': 'str',
        'internal_subjective_opinion': 'InternalSubjectiveOpinion'
    }

    attribute_map = {
        'tag_id': 'tagId',
        'submission_timestamp': 'submissionTimestamp',
        'node_type': 'nodeType',
        'geometry': 'geometry',
        'task_id': 'taskId',
        'internal_subjective_opinion': 'internalSubjectiveOpinion'
    }

    def __init__(self, tag_id=None, submission_timestamp=None, node_type=None, geometry=None, task_id=None, internal_subjective_opinion=None, local_vars_configuration=None):  # noqa: E501
        """Tag - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tag_id = None
        self._submission_timestamp = None
        self._node_type = None
        self._geometry = None
        self._task_id = None
        self._internal_subjective_opinion = None
        self.discriminator = None

        if tag_id is not None:
            self.tag_id = tag_id
        if submission_timestamp is not None:
            self.submission_timestamp = submission_timestamp
        if node_type is not None:
            self.node_type = node_type
        if geometry is not None:
            self.geometry = geometry
        if task_id is not None:
            self.task_id = task_id
        if internal_subjective_opinion is not None:
            self.internal_subjective_opinion = internal_subjective_opinion

    @property
    def tag_id(self):
        """Gets the tag_id of this Tag.  # noqa: E501

        Alpha-numeric, unique id of tagged object  # noqa: E501

        :return: The tag_id of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this Tag.

        Alpha-numeric, unique id of tagged object  # noqa: E501

        :param tag_id: The tag_id of this Tag.  # noqa: E501
        :type: str
        """

        self._tag_id = tag_id

    @property
    def submission_timestamp(self):
        """Gets the submission_timestamp of this Tag.  # noqa: E501

        Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00)  # noqa: E501

        :return: The submission_timestamp of this Tag.  # noqa: E501
        :rtype: datetime
        """
        return self._submission_timestamp

    @submission_timestamp.setter
    def submission_timestamp(self, submission_timestamp):
        """Sets the submission_timestamp of this Tag.

        Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00)  # noqa: E501

        :param submission_timestamp: The submission_timestamp of this Tag.  # noqa: E501
        :type: datetime
        """

        self._submission_timestamp = submission_timestamp

    @property
    def node_type(self):
        """Gets the node_type of this Tag.  # noqa: E501

        What does the object that has been detected represent. Can be extended to discrete histogram of types.  # noqa: E501

        :return: The node_type of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this Tag.

        What does the object that has been detected represent. Can be extended to discrete histogram of types.  # noqa: E501

        :param node_type: The node_type of this Tag.  # noqa: E501
        :type: str
        """

        self._node_type = node_type

    @property
    def geometry(self):
        """Gets the geometry of this Tag.  # noqa: E501

        What are the shapes that compose the tag?  # noqa: E501

        :return: The geometry of this Tag.  # noqa: E501
        :rtype: list[Shape]
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this Tag.

        What are the shapes that compose the tag?  # noqa: E501

        :param geometry: The geometry of this Tag.  # noqa: E501
        :type: list[Shape]
        """

        self._geometry = geometry

    @property
    def task_id(self):
        """Gets the task_id of this Tag.  # noqa: E501

        Alpha-numeric, unique id of task object  # noqa: E501

        :return: The task_id of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this Tag.

        Alpha-numeric, unique id of task object  # noqa: E501

        :param task_id: The task_id of this Tag.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def internal_subjective_opinion(self):
        """Gets the internal_subjective_opinion of this Tag.  # noqa: E501


        :return: The internal_subjective_opinion of this Tag.  # noqa: E501
        :rtype: InternalSubjectiveOpinion
        """
        return self._internal_subjective_opinion

    @internal_subjective_opinion.setter
    def internal_subjective_opinion(self, internal_subjective_opinion):
        """Sets the internal_subjective_opinion of this Tag.


        :param internal_subjective_opinion: The internal_subjective_opinion of this Tag.  # noqa: E501
        :type: InternalSubjectiveOpinion
        """

        self._internal_subjective_opinion = internal_subjective_opinion

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
        if not isinstance(other, Tag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tag):
            return True

        return self.to_dict() != other.to_dict()
