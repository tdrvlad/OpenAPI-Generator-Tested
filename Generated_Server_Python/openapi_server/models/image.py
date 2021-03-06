# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Image(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, image_url=None, image_base64=None, image_content_type=None):  # noqa: E501
        """Image - a model defined in OpenAPI

        :param image_url: The image_url of this Image.  # noqa: E501
        :type image_url: str
        :param image_base64: The image_base64 of this Image.  # noqa: E501
        :type image_base64: str
        :param image_content_type: The image_content_type of this Image.  # noqa: E501
        :type image_content_type: str
        """
        self.openapi_types = {
            'image_url': str,
            'image_base64': str,
            'image_content_type': str
        }

        self.attribute_map = {
            'image_url': 'imageURL',
            'image_base64': 'imageBase64',
            'image_content_type': 'imageContentType'
        }

        self._image_url = image_url
        self._image_base64 = image_base64
        self._image_content_type = image_content_type

    @classmethod
    def from_dict(cls, dikt) -> 'Image':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Image of this Image.  # noqa: E501
        :rtype: Image
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image_url(self):
        """Gets the image_url of this Image.

        The URL where the image is stored.  # noqa: E501

        :return: The image_url of this Image.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Image.

        The URL where the image is stored.  # noqa: E501

        :param image_url: The image_url of this Image.
        :type image_url: str
        """

        self._image_url = image_url

    @property
    def image_base64(self):
        """Gets the image_base64 of this Image.

        Base64 encoded string of the image.  # noqa: E501

        :return: The image_base64 of this Image.
        :rtype: str
        """
        return self._image_base64

    @image_base64.setter
    def image_base64(self, image_base64):
        """Sets the image_base64 of this Image.

        Base64 encoded string of the image.  # noqa: E501

        :param image_base64: The image_base64 of this Image.
        :type image_base64: str
        """

        self._image_base64 = image_base64

    @property
    def image_content_type(self):
        """Gets the image_content_type of this Image.

        Image MIME-type, such as image/png or image/jpeg  # noqa: E501

        :return: The image_content_type of this Image.
        :rtype: str
        """
        return self._image_content_type

    @image_content_type.setter
    def image_content_type(self, image_content_type):
        """Sets the image_content_type of this Image.

        Image MIME-type, such as image/png or image/jpeg  # noqa: E501

        :param image_content_type: The image_content_type of this Image.
        :type image_content_type: str
        """

        self._image_content_type = image_content_type
