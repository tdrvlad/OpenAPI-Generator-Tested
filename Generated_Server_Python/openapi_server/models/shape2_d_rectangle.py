# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.shape import Shape
from openapi_server.models.shape2_d_rectangle_all_of import Shape2DRectangleAllOf
from openapi_server import util

from openapi_server.models.shape import Shape  # noqa: E501
from openapi_server.models.shape2_d_rectangle_all_of import Shape2DRectangleAllOf  # noqa: E501

class Shape2DRectangle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, shape_id=None, shape_type=None, top=None, left=None, right=None, bottom=None):  # noqa: E501
        """Shape2DRectangle - a model defined in OpenAPI

        :param shape_id: The shape_id of this Shape2DRectangle.  # noqa: E501
        :type shape_id: str
        :param shape_type: The shape_type of this Shape2DRectangle.  # noqa: E501
        :type shape_type: str
        :param top: The top of this Shape2DRectangle.  # noqa: E501
        :type top: int
        :param left: The left of this Shape2DRectangle.  # noqa: E501
        :type left: int
        :param right: The right of this Shape2DRectangle.  # noqa: E501
        :type right: int
        :param bottom: The bottom of this Shape2DRectangle.  # noqa: E501
        :type bottom: int
        """
        self.openapi_types = {
            'shape_id': str,
            'shape_type': str,
            'top': int,
            'left': int,
            'right': int,
            'bottom': int
        }

        self.attribute_map = {
            'shape_id': 'shapeId',
            'shape_type': 'shapeType',
            'top': 'top',
            'left': 'left',
            'right': 'right',
            'bottom': 'bottom'
        }

        self._shape_id = shape_id
        self._shape_type = shape_type
        self._top = top
        self._left = left
        self._right = right
        self._bottom = bottom

    @classmethod
    def from_dict(cls, dikt) -> 'Shape2DRectangle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Shape2DRectangle of this Shape2DRectangle.  # noqa: E501
        :rtype: Shape2DRectangle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def shape_id(self):
        """Gets the shape_id of this Shape2DRectangle.

        [TBD] Alpha-numeric, unique id of dataset  # noqa: E501

        :return: The shape_id of this Shape2DRectangle.
        :rtype: str
        """
        return self._shape_id

    @shape_id.setter
    def shape_id(self, shape_id):
        """Sets the shape_id of this Shape2DRectangle.

        [TBD] Alpha-numeric, unique id of dataset  # noqa: E501

        :param shape_id: The shape_id of this Shape2DRectangle.
        :type shape_id: str
        """
        if shape_id is None:
            raise ValueError("Invalid value for `shape_id`, must not be `None`")  # noqa: E501

        self._shape_id = shape_id

    @property
    def shape_type(self):
        """Gets the shape_type of this Shape2DRectangle.

        descriminator  # noqa: E501

        :return: The shape_type of this Shape2DRectangle.
        :rtype: str
        """
        return self._shape_type

    @shape_type.setter
    def shape_type(self, shape_type):
        """Sets the shape_type of this Shape2DRectangle.

        descriminator  # noqa: E501

        :param shape_type: The shape_type of this Shape2DRectangle.
        :type shape_type: str
        """
        if shape_type is None:
            raise ValueError("Invalid value for `shape_type`, must not be `None`")  # noqa: E501

        self._shape_type = shape_type

    @property
    def top(self):
        """Gets the top of this Shape2DRectangle.

        Top coordinate of the tag, relative to media raster  # noqa: E501

        :return: The top of this Shape2DRectangle.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this Shape2DRectangle.

        Top coordinate of the tag, relative to media raster  # noqa: E501

        :param top: The top of this Shape2DRectangle.
        :type top: int
        """

        self._top = top

    @property
    def left(self):
        """Gets the left of this Shape2DRectangle.

        Left coordinate of the tag, relative to media raster  # noqa: E501

        :return: The left of this Shape2DRectangle.
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this Shape2DRectangle.

        Left coordinate of the tag, relative to media raster  # noqa: E501

        :param left: The left of this Shape2DRectangle.
        :type left: int
        """

        self._left = left

    @property
    def right(self):
        """Gets the right of this Shape2DRectangle.

        Right coordinate of the tag, relative to media raster  # noqa: E501

        :return: The right of this Shape2DRectangle.
        :rtype: int
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this Shape2DRectangle.

        Right coordinate of the tag, relative to media raster  # noqa: E501

        :param right: The right of this Shape2DRectangle.
        :type right: int
        """

        self._right = right

    @property
    def bottom(self):
        """Gets the bottom of this Shape2DRectangle.

        Bottom coordinate of the tag, relative to media raster  # noqa: E501

        :return: The bottom of this Shape2DRectangle.
        :rtype: int
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """Sets the bottom of this Shape2DRectangle.

        Bottom coordinate of the tag, relative to media raster  # noqa: E501

        :param bottom: The bottom of this Shape2DRectangle.
        :type bottom: int
        """

        self._bottom = bottom
