# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Shape(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, shape_id=None, shape_type=None):  # noqa: E501
        """Shape - a model defined in OpenAPI

        :param shape_id: The shape_id of this Shape.  # noqa: E501
        :type shape_id: str
        :param shape_type: The shape_type of this Shape.  # noqa: E501
        :type shape_type: str
        """
        self.openapi_types = {
            'shape_id': str,
            'shape_type': str
        }

        self.attribute_map = {
            'shape_id': 'shapeId',
            'shape_type': 'shapeType'
        }

        self._shape_id = shape_id
        self._shape_type = shape_type

    @classmethod
    def from_dict(cls, dikt) -> 'Shape':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Shape of this Shape.  # noqa: E501
        :rtype: Shape
        """
        return util.deserialize_model(dikt, cls)

    @property
    def shape_id(self):
        """Gets the shape_id of this Shape.

        [TBD] Alpha-numeric, unique id of dataset  # noqa: E501

        :return: The shape_id of this Shape.
        :rtype: str
        """
        return self._shape_id

    @shape_id.setter
    def shape_id(self, shape_id):
        """Sets the shape_id of this Shape.

        [TBD] Alpha-numeric, unique id of dataset  # noqa: E501

        :param shape_id: The shape_id of this Shape.
        :type shape_id: str
        """
        if shape_id is None:
            raise ValueError("Invalid value for `shape_id`, must not be `None`")  # noqa: E501

        self._shape_id = shape_id

    @property
    def shape_type(self):
        """Gets the shape_type of this Shape.

        descriminator  # noqa: E501

        :return: The shape_type of this Shape.
        :rtype: str
        """
        return self._shape_type

    @shape_type.setter
    def shape_type(self, shape_type):
        """Sets the shape_type of this Shape.

        descriminator  # noqa: E501

        :param shape_type: The shape_type of this Shape.
        :type shape_type: str
        """
        if shape_type is None:
            raise ValueError("Invalid value for `shape_type`, must not be `None`")  # noqa: E501

        self._shape_type = shape_type