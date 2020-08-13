# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Point2D(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x=None, y=None):  # noqa: E501
        """Point2D - a model defined in OpenAPI

        :param x: The x of this Point2D.  # noqa: E501
        :type x: int
        :param y: The y of this Point2D.  # noqa: E501
        :type y: int
        """
        self.openapi_types = {
            'x': int,
            'y': int
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y'
        }

        self._x = x
        self._y = y

    @classmethod
    def from_dict(cls, dikt) -> 'Point2D':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Point2D of this Point2D.  # noqa: E501
        :rtype: Point2D
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self):
        """Gets the x of this Point2D.

        X-coordinate as integer number of pixels measured from the left to the right.  # noqa: E501

        :return: The x of this Point2D.
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this Point2D.

        X-coordinate as integer number of pixels measured from the left to the right.  # noqa: E501

        :param x: The x of this Point2D.
        :type x: int
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this Point2D.

        Y-coordinate as integer number of pixels measured from the top to the bottom.  # noqa: E501

        :return: The y of this Point2D.
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this Point2D.

        Y-coordinate as integer number of pixels measured from the top to the bottom.  # noqa: E501

        :param y: The y of this Point2D.
        :type y: int
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y