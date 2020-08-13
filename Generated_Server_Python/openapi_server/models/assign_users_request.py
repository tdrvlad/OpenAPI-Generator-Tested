# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AssignUsersRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, challenge_id=None, avatar_ids=None):  # noqa: E501
        """AssignUsersRequest - a model defined in OpenAPI

        :param challenge_id: The challenge_id of this AssignUsersRequest.  # noqa: E501
        :type challenge_id: str
        :param avatar_ids: The avatar_ids of this AssignUsersRequest.  # noqa: E501
        :type avatar_ids: List[str]
        """
        self.openapi_types = {
            'challenge_id': str,
            'avatar_ids': List[str]
        }

        self.attribute_map = {
            'challenge_id': 'challengeId',
            'avatar_ids': 'avatarIds'
        }

        self._challenge_id = challenge_id
        self._avatar_ids = avatar_ids

    @classmethod
    def from_dict(cls, dikt) -> 'AssignUsersRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssignUsersRequest of this AssignUsersRequest.  # noqa: E501
        :rtype: AssignUsersRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def challenge_id(self):
        """Gets the challenge_id of this AssignUsersRequest.

        Unique ID of challenge  # noqa: E501

        :return: The challenge_id of this AssignUsersRequest.
        :rtype: str
        """
        return self._challenge_id

    @challenge_id.setter
    def challenge_id(self, challenge_id):
        """Sets the challenge_id of this AssignUsersRequest.

        Unique ID of challenge  # noqa: E501

        :param challenge_id: The challenge_id of this AssignUsersRequest.
        :type challenge_id: str
        """

        self._challenge_id = challenge_id

    @property
    def avatar_ids(self):
        """Gets the avatar_ids of this AssignUsersRequest.


        :return: The avatar_ids of this AssignUsersRequest.
        :rtype: List[str]
        """
        return self._avatar_ids

    @avatar_ids.setter
    def avatar_ids(self, avatar_ids):
        """Sets the avatar_ids of this AssignUsersRequest.


        :param avatar_ids: The avatar_ids of this AssignUsersRequest.
        :type avatar_ids: List[str]
        """

        self._avatar_ids = avatar_ids
