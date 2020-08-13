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


class AssignUsersRequest(object):
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
        'challenge_id': 'str',
        'avatar_ids': 'list[str]'
    }

    attribute_map = {
        'challenge_id': 'challengeId',
        'avatar_ids': 'avatarIds'
    }

    def __init__(self, challenge_id=None, avatar_ids=None, local_vars_configuration=None):  # noqa: E501
        """AssignUsersRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._challenge_id = None
        self._avatar_ids = None
        self.discriminator = None

        if challenge_id is not None:
            self.challenge_id = challenge_id
        if avatar_ids is not None:
            self.avatar_ids = avatar_ids

    @property
    def challenge_id(self):
        """Gets the challenge_id of this AssignUsersRequest.  # noqa: E501

        Unique ID of challenge  # noqa: E501

        :return: The challenge_id of this AssignUsersRequest.  # noqa: E501
        :rtype: str
        """
        return self._challenge_id

    @challenge_id.setter
    def challenge_id(self, challenge_id):
        """Sets the challenge_id of this AssignUsersRequest.

        Unique ID of challenge  # noqa: E501

        :param challenge_id: The challenge_id of this AssignUsersRequest.  # noqa: E501
        :type: str
        """

        self._challenge_id = challenge_id

    @property
    def avatar_ids(self):
        """Gets the avatar_ids of this AssignUsersRequest.  # noqa: E501


        :return: The avatar_ids of this AssignUsersRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._avatar_ids

    @avatar_ids.setter
    def avatar_ids(self, avatar_ids):
        """Sets the avatar_ids of this AssignUsersRequest.


        :param avatar_ids: The avatar_ids of this AssignUsersRequest.  # noqa: E501
        :type: list[str]
        """

        self._avatar_ids = avatar_ids

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
        if not isinstance(other, AssignUsersRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssignUsersRequest):
            return True

        return self.to_dict() != other.to_dict()
