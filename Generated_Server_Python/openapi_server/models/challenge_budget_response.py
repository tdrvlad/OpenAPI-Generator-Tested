# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ChallengeBudgetResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, estimated_budget=None):  # noqa: E501
        """ChallengeBudgetResponse - a model defined in OpenAPI

        :param estimated_budget: The estimated_budget of this ChallengeBudgetResponse.  # noqa: E501
        :type estimated_budget: float
        """
        self.openapi_types = {
            'estimated_budget': float
        }

        self.attribute_map = {
            'estimated_budget': 'estimatedBudget'
        }

        self._estimated_budget = estimated_budget

    @classmethod
    def from_dict(cls, dikt) -> 'ChallengeBudgetResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChallengeBudgetResponse of this ChallengeBudgetResponse.  # noqa: E501
        :rtype: ChallengeBudgetResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def estimated_budget(self):
        """Gets the estimated_budget of this ChallengeBudgetResponse.

        estimated budget for challenge  # noqa: E501

        :return: The estimated_budget of this ChallengeBudgetResponse.
        :rtype: float
        """
        return self._estimated_budget

    @estimated_budget.setter
    def estimated_budget(self, estimated_budget):
        """Sets the estimated_budget of this ChallengeBudgetResponse.

        estimated budget for challenge  # noqa: E501

        :param estimated_budget: The estimated_budget of this ChallengeBudgetResponse.
        :type estimated_budget: float
        """

        self._estimated_budget = estimated_budget
