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


class Shape2DTimeboundPolygon(object):
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
        'start_frame_counter': 'int',
        'end_frame_counter': 'int',
        'points': 'list[Point2D]'
    }

    attribute_map = {
        'start_frame_counter': 'startFrameCounter',
        'end_frame_counter': 'endFrameCounter',
        'points': 'points'
    }

    def __init__(self, start_frame_counter=None, end_frame_counter=None, points=None, local_vars_configuration=None):  # noqa: E501
        """Shape2DTimeboundPolygon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start_frame_counter = None
        self._end_frame_counter = None
        self._points = None
        self.discriminator = None

        if start_frame_counter is not None:
            self.start_frame_counter = start_frame_counter
        if end_frame_counter is not None:
            self.end_frame_counter = end_frame_counter
        if points is not None:
            self.points = points

    @property
    def start_frame_counter(self):
        """Gets the start_frame_counter of this Shape2DTimeboundPolygon.  # noqa: E501

        Frame where the described tag begins  # noqa: E501

        :return: The start_frame_counter of this Shape2DTimeboundPolygon.  # noqa: E501
        :rtype: int
        """
        return self._start_frame_counter

    @start_frame_counter.setter
    def start_frame_counter(self, start_frame_counter):
        """Sets the start_frame_counter of this Shape2DTimeboundPolygon.

        Frame where the described tag begins  # noqa: E501

        :param start_frame_counter: The start_frame_counter of this Shape2DTimeboundPolygon.  # noqa: E501
        :type: int
        """

        self._start_frame_counter = start_frame_counter

    @property
    def end_frame_counter(self):
        """Gets the end_frame_counter of this Shape2DTimeboundPolygon.  # noqa: E501

        Frame where the described tag begins  # noqa: E501

        :return: The end_frame_counter of this Shape2DTimeboundPolygon.  # noqa: E501
        :rtype: int
        """
        return self._end_frame_counter

    @end_frame_counter.setter
    def end_frame_counter(self, end_frame_counter):
        """Sets the end_frame_counter of this Shape2DTimeboundPolygon.

        Frame where the described tag begins  # noqa: E501

        :param end_frame_counter: The end_frame_counter of this Shape2DTimeboundPolygon.  # noqa: E501
        :type: int
        """

        self._end_frame_counter = end_frame_counter

    @property
    def points(self):
        """Gets the points of this Shape2DTimeboundPolygon.  # noqa: E501


        :return: The points of this Shape2DTimeboundPolygon.  # noqa: E501
        :rtype: list[Point2D]
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this Shape2DTimeboundPolygon.


        :param points: The points of this Shape2DTimeboundPolygon.  # noqa: E501
        :type: list[Point2D]
        """

        self._points = points

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
        if not isinstance(other, Shape2DTimeboundPolygon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Shape2DTimeboundPolygon):
            return True

        return self.to_dict() != other.to_dict()
