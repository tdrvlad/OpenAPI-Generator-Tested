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


class PermanentIdentifierSegment(object):
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
        'encoding': 'str',
        'index': 'int',
        'weight': 'float',
        'assignment_function': 'str',
        'value': 'str'
    }

    attribute_map = {
        'encoding': 'encoding',
        'index': 'index',
        'weight': 'weight',
        'assignment_function': 'assignmentFunction',
        'value': 'value'
    }

    def __init__(self, encoding=None, index=None, weight=None, assignment_function=None, value=None, local_vars_configuration=None):  # noqa: E501
        """PermanentIdentifierSegment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._encoding = None
        self._index = None
        self._weight = None
        self._assignment_function = None
        self._value = None
        self.discriminator = None

        if encoding is not None:
            self.encoding = encoding
        if index is not None:
            self.index = index
        if weight is not None:
            self.weight = weight
        if assignment_function is not None:
            self.assignment_function = assignment_function
        if value is not None:
            self.value = value

    @property
    def encoding(self):
        """Gets the encoding of this PermanentIdentifierSegment.  # noqa: E501

        The encoding used for deserializing the value, before distance and identity functions can be computed  # noqa: E501

        :return: The encoding of this PermanentIdentifierSegment.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this PermanentIdentifierSegment.

        The encoding used for deserializing the value, before distance and identity functions can be computed  # noqa: E501

        :param encoding: The encoding of this PermanentIdentifierSegment.  # noqa: E501
        :type: str
        """
        allowed_values = ["json-array", "base64-binary-float", "base64-binary-double", "base64-binary-int32", "base64-binary-int64", "text-ascii", "text-unicode"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and encoding not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `encoding` ({0}), must be one of {1}"  # noqa: E501
                .format(encoding, allowed_values)
            )

        self._encoding = encoding

    @property
    def index(self):
        """Gets the index of this PermanentIdentifierSegment.  # noqa: E501

        The index of the segment, so as to guarantee strict ordering of segment comparison  # noqa: E501

        :return: The index of this PermanentIdentifierSegment.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this PermanentIdentifierSegment.

        The index of the segment, so as to guarantee strict ordering of segment comparison  # noqa: E501

        :param index: The index of this PermanentIdentifierSegment.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def weight(self):
        """Gets the weight of this PermanentIdentifierSegment.  # noqa: E501

        The weight of the distance in the total distance  # noqa: E501

        :return: The weight of this PermanentIdentifierSegment.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this PermanentIdentifierSegment.

        The weight of the distance in the total distance  # noqa: E501

        :param weight: The weight of this PermanentIdentifierSegment.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def assignment_function(self):
        """Gets the assignment_function of this PermanentIdentifierSegment.  # noqa: E501

        The hashcode obtained by running a SHA-512 on the binary values of the segments, in their order.   # noqa: E501

        :return: The assignment_function of this PermanentIdentifierSegment.  # noqa: E501
        :rtype: str
        """
        return self._assignment_function

    @assignment_function.setter
    def assignment_function(self, assignment_function):
        """Sets the assignment_function of this PermanentIdentifierSegment.

        The hashcode obtained by running a SHA-512 on the binary values of the segments, in their order.   # noqa: E501

        :param assignment_function: The assignment_function of this PermanentIdentifierSegment.  # noqa: E501
        :type: str
        """
        allowed_values = ["hashed-from-data", "machine-random-uniform", "machine-timestamp", "machine-identifier", "remote-timestamp", "remote-generated", "entity-identifier-ledger", "enforced-unique-ledger", "sequential-enforced-volatile-ledger", "sequential-enforced-persistent-ledger"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and assignment_function not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `assignment_function` ({0}), must be one of {1}"  # noqa: E501
                .format(assignment_function, allowed_values)
            )

        self._assignment_function = assignment_function

    @property
    def value(self):
        """Gets the value of this PermanentIdentifierSegment.  # noqa: E501

        The serialized value of the segment  # noqa: E501

        :return: The value of this PermanentIdentifierSegment.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PermanentIdentifierSegment.

        The serialized value of the segment  # noqa: E501

        :param value: The value of this PermanentIdentifierSegment.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, PermanentIdentifierSegment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PermanentIdentifierSegment):
            return True

        return self.to_dict() != other.to_dict()
