# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.challenge_statistics_users_work_time import ChallengeStatisticsUsersWorkTime
from openapi_server import util

from openapi_server.models.challenge_statistics_users_work_time import ChallengeStatisticsUsersWorkTime  # noqa: E501

class ChallengeStatistics(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, average_rate=None, average_completion_time=None, average_validation_rate=None, payment_per_hour=None, completion_time_passed=None, completion_time_real=None, users_work_time=None):  # noqa: E501
        """ChallengeStatistics - a model defined in OpenAPI

        :param average_rate: The average_rate of this ChallengeStatistics.  # noqa: E501
        :type average_rate: float
        :param average_completion_time: The average_completion_time of this ChallengeStatistics.  # noqa: E501
        :type average_completion_time: float
        :param average_validation_rate: The average_validation_rate of this ChallengeStatistics.  # noqa: E501
        :type average_validation_rate: float
        :param payment_per_hour: The payment_per_hour of this ChallengeStatistics.  # noqa: E501
        :type payment_per_hour: float
        :param completion_time_passed: The completion_time_passed of this ChallengeStatistics.  # noqa: E501
        :type completion_time_passed: int
        :param completion_time_real: The completion_time_real of this ChallengeStatistics.  # noqa: E501
        :type completion_time_real: int
        :param users_work_time: The users_work_time of this ChallengeStatistics.  # noqa: E501
        :type users_work_time: List[ChallengeStatisticsUsersWorkTime]
        """
        self.openapi_types = {
            'average_rate': float,
            'average_completion_time': float,
            'average_validation_rate': float,
            'payment_per_hour': float,
            'completion_time_passed': int,
            'completion_time_real': int,
            'users_work_time': List[ChallengeStatisticsUsersWorkTime]
        }

        self.attribute_map = {
            'average_rate': 'averageRate',
            'average_completion_time': 'averageCompletionTime',
            'average_validation_rate': 'averageValidationRate',
            'payment_per_hour': 'paymentPerHour',
            'completion_time_passed': 'completionTimePassed',
            'completion_time_real': 'completionTimeReal',
            'users_work_time': 'usersWorkTime'
        }

        self._average_rate = average_rate
        self._average_completion_time = average_completion_time
        self._average_validation_rate = average_validation_rate
        self._payment_per_hour = payment_per_hour
        self._completion_time_passed = completion_time_passed
        self._completion_time_real = completion_time_real
        self._users_work_time = users_work_time

    @classmethod
    def from_dict(cls, dikt) -> 'ChallengeStatistics':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChallengeStatistics of this ChallengeStatistics.  # noqa: E501
        :rtype: ChallengeStatistics
        """
        return util.deserialize_model(dikt, cls)

    @property
    def average_rate(self):
        """Gets the average_rate of this ChallengeStatistics.

        average payment per challenge  # noqa: E501

        :return: The average_rate of this ChallengeStatistics.
        :rtype: float
        """
        return self._average_rate

    @average_rate.setter
    def average_rate(self, average_rate):
        """Sets the average_rate of this ChallengeStatistics.

        average payment per challenge  # noqa: E501

        :param average_rate: The average_rate of this ChallengeStatistics.
        :type average_rate: float
        """

        self._average_rate = average_rate

    @property
    def average_completion_time(self):
        """Gets the average_completion_time of this ChallengeStatistics.

        Average time to complete a task for a challenge  # noqa: E501

        :return: The average_completion_time of this ChallengeStatistics.
        :rtype: float
        """
        return self._average_completion_time

    @average_completion_time.setter
    def average_completion_time(self, average_completion_time):
        """Sets the average_completion_time of this ChallengeStatistics.

        Average time to complete a task for a challenge  # noqa: E501

        :param average_completion_time: The average_completion_time of this ChallengeStatistics.
        :type average_completion_time: float
        """

        self._average_completion_time = average_completion_time

    @property
    def average_validation_rate(self):
        """Gets the average_validation_rate of this ChallengeStatistics.

        Average valdation per challenge  # noqa: E501

        :return: The average_validation_rate of this ChallengeStatistics.
        :rtype: float
        """
        return self._average_validation_rate

    @average_validation_rate.setter
    def average_validation_rate(self, average_validation_rate):
        """Sets the average_validation_rate of this ChallengeStatistics.

        Average valdation per challenge  # noqa: E501

        :param average_validation_rate: The average_validation_rate of this ChallengeStatistics.
        :type average_validation_rate: float
        """

        self._average_validation_rate = average_validation_rate

    @property
    def payment_per_hour(self):
        """Gets the payment_per_hour of this ChallengeStatistics.

        Estimated payment per hour  # noqa: E501

        :return: The payment_per_hour of this ChallengeStatistics.
        :rtype: float
        """
        return self._payment_per_hour

    @payment_per_hour.setter
    def payment_per_hour(self, payment_per_hour):
        """Sets the payment_per_hour of this ChallengeStatistics.

        Estimated payment per hour  # noqa: E501

        :param payment_per_hour: The payment_per_hour of this ChallengeStatistics.
        :type payment_per_hour: float
        """

        self._payment_per_hour = payment_per_hour

    @property
    def completion_time_passed(self):
        """Gets the completion_time_passed of this ChallengeStatistics.

        completion time for all the task passed miliseconds  # noqa: E501

        :return: The completion_time_passed of this ChallengeStatistics.
        :rtype: int
        """
        return self._completion_time_passed

    @completion_time_passed.setter
    def completion_time_passed(self, completion_time_passed):
        """Sets the completion_time_passed of this ChallengeStatistics.

        completion time for all the task passed miliseconds  # noqa: E501

        :param completion_time_passed: The completion_time_passed of this ChallengeStatistics.
        :type completion_time_passed: int
        """

        self._completion_time_passed = completion_time_passed

    @property
    def completion_time_real(self):
        """Gets the completion_time_real of this ChallengeStatistics.

        completion time for all the tasks miliseconds  # noqa: E501

        :return: The completion_time_real of this ChallengeStatistics.
        :rtype: int
        """
        return self._completion_time_real

    @completion_time_real.setter
    def completion_time_real(self, completion_time_real):
        """Sets the completion_time_real of this ChallengeStatistics.

        completion time for all the tasks miliseconds  # noqa: E501

        :param completion_time_real: The completion_time_real of this ChallengeStatistics.
        :type completion_time_real: int
        """

        self._completion_time_real = completion_time_real

    @property
    def users_work_time(self):
        """Gets the users_work_time of this ChallengeStatistics.

        graphs  # noqa: E501

        :return: The users_work_time of this ChallengeStatistics.
        :rtype: List[ChallengeStatisticsUsersWorkTime]
        """
        return self._users_work_time

    @users_work_time.setter
    def users_work_time(self, users_work_time):
        """Sets the users_work_time of this ChallengeStatistics.

        graphs  # noqa: E501

        :param users_work_time: The users_work_time of this ChallengeStatistics.
        :type users_work_time: List[ChallengeStatisticsUsersWorkTime]
        """

        self._users_work_time = users_work_time
