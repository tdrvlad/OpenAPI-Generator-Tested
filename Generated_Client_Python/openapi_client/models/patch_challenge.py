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


class PatchChallenge(object):
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
        'evaluation_policy_id': 'str',
        'dispatch_policy_id': 'str',
        'access_type': 'ChallengeAccessTypeEnum',
        'name': 'str',
        'description': 'str',
        'budget': 'float'
    }

    attribute_map = {
        'evaluation_policy_id': 'evaluationPolicyId',
        'dispatch_policy_id': 'dispatchPolicyId',
        'access_type': 'accessType',
        'name': 'name',
        'description': 'description',
        'budget': 'budget'
    }

    def __init__(self, evaluation_policy_id=None, dispatch_policy_id=None, access_type=None, name=None, description=None, budget=None, local_vars_configuration=None):  # noqa: E501
        """PatchChallenge - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._evaluation_policy_id = None
        self._dispatch_policy_id = None
        self._access_type = None
        self._name = None
        self._description = None
        self._budget = None
        self.discriminator = None

        if evaluation_policy_id is not None:
            self.evaluation_policy_id = evaluation_policy_id
        if dispatch_policy_id is not None:
            self.dispatch_policy_id = dispatch_policy_id
        if access_type is not None:
            self.access_type = access_type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if budget is not None:
            self.budget = budget

    @property
    def evaluation_policy_id(self):
        """Gets the evaluation_policy_id of this PatchChallenge.  # noqa: E501

        Alpha-numeric, unique id of evaluation policy  # noqa: E501

        :return: The evaluation_policy_id of this PatchChallenge.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_policy_id

    @evaluation_policy_id.setter
    def evaluation_policy_id(self, evaluation_policy_id):
        """Sets the evaluation_policy_id of this PatchChallenge.

        Alpha-numeric, unique id of evaluation policy  # noqa: E501

        :param evaluation_policy_id: The evaluation_policy_id of this PatchChallenge.  # noqa: E501
        :type: str
        """

        self._evaluation_policy_id = evaluation_policy_id

    @property
    def dispatch_policy_id(self):
        """Gets the dispatch_policy_id of this PatchChallenge.  # noqa: E501

        Alpha-numeric, unique id of dispatch policy  # noqa: E501

        :return: The dispatch_policy_id of this PatchChallenge.  # noqa: E501
        :rtype: str
        """
        return self._dispatch_policy_id

    @dispatch_policy_id.setter
    def dispatch_policy_id(self, dispatch_policy_id):
        """Sets the dispatch_policy_id of this PatchChallenge.

        Alpha-numeric, unique id of dispatch policy  # noqa: E501

        :param dispatch_policy_id: The dispatch_policy_id of this PatchChallenge.  # noqa: E501
        :type: str
        """

        self._dispatch_policy_id = dispatch_policy_id

    @property
    def access_type(self):
        """Gets the access_type of this PatchChallenge.  # noqa: E501


        :return: The access_type of this PatchChallenge.  # noqa: E501
        :rtype: ChallengeAccessTypeEnum
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this PatchChallenge.


        :param access_type: The access_type of this PatchChallenge.  # noqa: E501
        :type: ChallengeAccessTypeEnum
        """

        self._access_type = access_type

    @property
    def name(self):
        """Gets the name of this PatchChallenge.  # noqa: E501

        [TBD] Alpha-numeric, name of dataset  # noqa: E501

        :return: The name of this PatchChallenge.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchChallenge.

        [TBD] Alpha-numeric, name of dataset  # noqa: E501

        :param name: The name of this PatchChallenge.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this PatchChallenge.  # noqa: E501

        [TBD] Alpha-numeric, name of dataset  # noqa: E501

        :return: The description of this PatchChallenge.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PatchChallenge.

        [TBD] Alpha-numeric, name of dataset  # noqa: E501

        :param description: The description of this PatchChallenge.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def budget(self):
        """Gets the budget of this PatchChallenge.  # noqa: E501

        budget allocated for challenge  # noqa: E501

        :return: The budget of this PatchChallenge.  # noqa: E501
        :rtype: float
        """
        return self._budget

    @budget.setter
    def budget(self, budget):
        """Sets the budget of this PatchChallenge.

        budget allocated for challenge  # noqa: E501

        :param budget: The budget of this PatchChallenge.  # noqa: E501
        :type: float
        """

        self._budget = budget

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
        if not isinstance(other, PatchChallenge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchChallenge):
            return True

        return self.to_dict() != other.to_dict()
