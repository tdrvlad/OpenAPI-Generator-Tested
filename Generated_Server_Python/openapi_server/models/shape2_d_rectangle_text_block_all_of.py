# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.style import Style
from openapi_server.models.transliteration import Transliteration
from openapi_server import util

from openapi_server.models.style import Style  # noqa: E501
from openapi_server.models.transliteration import Transliteration  # noqa: E501

class Shape2DRectangleTextBlockAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, transliteration=None, style=None):  # noqa: E501
        """Shape2DRectangleTextBlockAllOf - a model defined in OpenAPI

        :param transliteration: The transliteration of this Shape2DRectangleTextBlockAllOf.  # noqa: E501
        :type transliteration: Transliteration
        :param style: The style of this Shape2DRectangleTextBlockAllOf.  # noqa: E501
        :type style: Style
        """
        self.openapi_types = {
            'transliteration': Transliteration,
            'style': Style
        }

        self.attribute_map = {
            'transliteration': 'transliteration',
            'style': 'style'
        }

        self._transliteration = transliteration
        self._style = style

    @classmethod
    def from_dict(cls, dikt) -> 'Shape2DRectangleTextBlockAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Shape2DRectangleTextBlock_allOf of this Shape2DRectangleTextBlockAllOf.  # noqa: E501
        :rtype: Shape2DRectangleTextBlockAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transliteration(self):
        """Gets the transliteration of this Shape2DRectangleTextBlockAllOf.


        :return: The transliteration of this Shape2DRectangleTextBlockAllOf.
        :rtype: Transliteration
        """
        return self._transliteration

    @transliteration.setter
    def transliteration(self, transliteration):
        """Sets the transliteration of this Shape2DRectangleTextBlockAllOf.


        :param transliteration: The transliteration of this Shape2DRectangleTextBlockAllOf.
        :type transliteration: Transliteration
        """

        self._transliteration = transliteration

    @property
    def style(self):
        """Gets the style of this Shape2DRectangleTextBlockAllOf.


        :return: The style of this Shape2DRectangleTextBlockAllOf.
        :rtype: Style
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this Shape2DRectangleTextBlockAllOf.


        :param style: The style of this Shape2DRectangleTextBlockAllOf.
        :type style: Style
        """

        self._style = style
