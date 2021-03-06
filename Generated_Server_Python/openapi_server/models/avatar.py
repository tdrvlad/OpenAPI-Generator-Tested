# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.challenge import Challenge
from openapi_server.models.life_form_enum import LifeFormEnum
from openapi_server import util

from openapi_server.models.challenge import Challenge  # noqa: E501
from openapi_server.models.life_form_enum import LifeFormEnum  # noqa: E501

class Avatar(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, avatar_id=None, life_form=None, assigned_challenges=None):  # noqa: E501
        """Avatar - a model defined in OpenAPI

        :param avatar_id: The avatar_id of this Avatar.  # noqa: E501
        :type avatar_id: str
        :param life_form: The life_form of this Avatar.  # noqa: E501
        :type life_form: LifeFormEnum
        :param assigned_challenges: The assigned_challenges of this Avatar.  # noqa: E501
        :type assigned_challenges: List[Challenge]
        """
        self.openapi_types = {
            'avatar_id': str,
            'life_form': LifeFormEnum,
            'assigned_challenges': List[Challenge]
        }

        self.attribute_map = {
            'avatar_id': 'avatarId',
            'life_form': 'lifeForm',
            'assigned_challenges': 'assignedChallenges'
        }

        self._avatar_id = avatar_id
        self._life_form = life_form
        self._assigned_challenges = assigned_challenges

    @classmethod
    def from_dict(cls, dikt) -> 'Avatar':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Avatar of this Avatar.  # noqa: E501
        :rtype: Avatar
        """
        return util.deserialize_model(dikt, cls)

    @property
    def avatar_id(self):
        """Gets the avatar_id of this Avatar.

        [TBD] Alpha-numeric, unique id of avatar  # noqa: E501

        :return: The avatar_id of this Avatar.
        :rtype: str
        """
        return self._avatar_id

    @avatar_id.setter
    def avatar_id(self, avatar_id):
        """Sets the avatar_id of this Avatar.

        [TBD] Alpha-numeric, unique id of avatar  # noqa: E501

        :param avatar_id: The avatar_id of this Avatar.
        :type avatar_id: str
        """

        self._avatar_id = avatar_id

    @property
    def life_form(self):
        """Gets the life_form of this Avatar.


        :return: The life_form of this Avatar.
        :rtype: LifeFormEnum
        """
        return self._life_form

    @life_form.setter
    def life_form(self, life_form):
        """Sets the life_form of this Avatar.


        :param life_form: The life_form of this Avatar.
        :type life_form: LifeFormEnum
        """

        self._life_form = life_form

    @property
    def assigned_challenges(self):
        """Gets the assigned_challenges of this Avatar.

        assignedChallenges  # noqa: E501

        :return: The assigned_challenges of this Avatar.
        :rtype: List[Challenge]
        """
        return self._assigned_challenges

    @assigned_challenges.setter
    def assigned_challenges(self, assigned_challenges):
        """Sets the assigned_challenges of this Avatar.

        assignedChallenges  # noqa: E501

        :param assigned_challenges: The assigned_challenges of this Avatar.
        :type assigned_challenges: List[Challenge]
        """

        self._assigned_challenges = assigned_challenges
