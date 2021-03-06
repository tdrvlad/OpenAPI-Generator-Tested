# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Shape2DRectangleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, top=None, left=None, right=None, bottom=None):  # noqa: E501
        """Shape2DRectangleAllOf - a model defined in OpenAPI

        :param top: The top of this Shape2DRectangleAllOf.  # noqa: E501
        :type top: int
        :param left: The left of this Shape2DRectangleAllOf.  # noqa: E501
        :type left: int
        :param right: The right of this Shape2DRectangleAllOf.  # noqa: E501
        :type right: int
        :param bottom: The bottom of this Shape2DRectangleAllOf.  # noqa: E501
        :type bottom: int
        """
        self.openapi_types = {
            'top': int,
            'left': int,
            'right': int,
            'bottom': int
        }

        self.attribute_map = {
            'top': 'top',
            'left': 'left',
            'right': 'right',
            'bottom': 'bottom'
        }

        self._top = top
        self._left = left
        self._right = right
        self._bottom = bottom

    @classmethod
    def from_dict(cls, dikt) -> 'Shape2DRectangleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Shape2DRectangle_allOf of this Shape2DRectangleAllOf.  # noqa: E501
        :rtype: Shape2DRectangleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def top(self):
        """Gets the top of this Shape2DRectangleAllOf.

        Top coordinate of the tag, relative to media raster  # noqa: E501

        :return: The top of this Shape2DRectangleAllOf.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this Shape2DRectangleAllOf.

        Top coordinate of the tag, relative to media raster  # noqa: E501

        :param top: The top of this Shape2DRectangleAllOf.
        :type top: int
        """

        self._top = top

    @property
    def left(self):
        """Gets the left of this Shape2DRectangleAllOf.

        Left coordinate of the tag, relative to media raster  # noqa: E501

        :return: The left of this Shape2DRectangleAllOf.
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this Shape2DRectangleAllOf.

        Left coordinate of the tag, relative to media raster  # noqa: E501

        :param left: The left of this Shape2DRectangleAllOf.
        :type left: int
        """

        self._left = left

    @property
    def right(self):
        """Gets the right of this Shape2DRectangleAllOf.

        Right coordinate of the tag, relative to media raster  # noqa: E501

        :return: The right of this Shape2DRectangleAllOf.
        :rtype: int
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this Shape2DRectangleAllOf.

        Right coordinate of the tag, relative to media raster  # noqa: E501

        :param right: The right of this Shape2DRectangleAllOf.
        :type right: int
        """

        self._right = right

    @property
    def bottom(self):
        """Gets the bottom of this Shape2DRectangleAllOf.

        Bottom coordinate of the tag, relative to media raster  # noqa: E501

        :return: The bottom of this Shape2DRectangleAllOf.
        :rtype: int
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """Sets the bottom of this Shape2DRectangleAllOf.

        Bottom coordinate of the tag, relative to media raster  # noqa: E501

        :param bottom: The bottom of this Shape2DRectangleAllOf.
        :type bottom: int
        """

        self._bottom = bottom
