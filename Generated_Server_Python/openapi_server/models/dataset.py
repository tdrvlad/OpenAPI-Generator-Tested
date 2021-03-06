# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.dataset_type_enum import DatasetTypeEnum
from openapi_server.models.image import Image
from openapi_server import util

from openapi_server.models.dataset_type_enum import DatasetTypeEnum  # noqa: E501
from openapi_server.models.image import Image  # noqa: E501

class Dataset(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dataset_id=None, type=None, creation_timestamp=None, last_update_timestamp=None, owning_account_id=None, name=None, image=None, storage_cost=None):  # noqa: E501
        """Dataset - a model defined in OpenAPI

        :param dataset_id: The dataset_id of this Dataset.  # noqa: E501
        :type dataset_id: str
        :param type: The type of this Dataset.  # noqa: E501
        :type type: DatasetTypeEnum
        :param creation_timestamp: The creation_timestamp of this Dataset.  # noqa: E501
        :type creation_timestamp: datetime
        :param last_update_timestamp: The last_update_timestamp of this Dataset.  # noqa: E501
        :type last_update_timestamp: datetime
        :param owning_account_id: The owning_account_id of this Dataset.  # noqa: E501
        :type owning_account_id: str
        :param name: The name of this Dataset.  # noqa: E501
        :type name: str
        :param image: The image of this Dataset.  # noqa: E501
        :type image: Image
        :param storage_cost: The storage_cost of this Dataset.  # noqa: E501
        :type storage_cost: float
        """
        self.openapi_types = {
            'dataset_id': str,
            'type': DatasetTypeEnum,
            'creation_timestamp': datetime,
            'last_update_timestamp': datetime,
            'owning_account_id': str,
            'name': str,
            'image': Image,
            'storage_cost': float
        }

        self.attribute_map = {
            'dataset_id': 'datasetId',
            'type': 'type',
            'creation_timestamp': 'creationTimestamp',
            'last_update_timestamp': 'lastUpdateTimestamp',
            'owning_account_id': 'owningAccountId',
            'name': 'name',
            'image': 'image',
            'storage_cost': 'storageCost'
        }

        self._dataset_id = dataset_id
        self._type = type
        self._creation_timestamp = creation_timestamp
        self._last_update_timestamp = last_update_timestamp
        self._owning_account_id = owning_account_id
        self._name = name
        self._image = image
        self._storage_cost = storage_cost

    @classmethod
    def from_dict(cls, dikt) -> 'Dataset':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Dataset of this Dataset.  # noqa: E501
        :rtype: Dataset
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dataset_id(self):
        """Gets the dataset_id of this Dataset.

        [TBD] Alpha-numeric, unique id of dataset  # noqa: E501

        :return: The dataset_id of this Dataset.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this Dataset.

        [TBD] Alpha-numeric, unique id of dataset  # noqa: E501

        :param dataset_id: The dataset_id of this Dataset.
        :type dataset_id: str
        """

        self._dataset_id = dataset_id

    @property
    def type(self):
        """Gets the type of this Dataset.


        :return: The type of this Dataset.
        :rtype: DatasetTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Dataset.


        :param type: The type of this Dataset.
        :type type: DatasetTypeEnum
        """

        self._type = type

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this Dataset.

        Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00)  # noqa: E501

        :return: The creation_timestamp of this Dataset.
        :rtype: datetime
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this Dataset.

        Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00)  # noqa: E501

        :param creation_timestamp: The creation_timestamp of this Dataset.
        :type creation_timestamp: datetime
        """

        self._creation_timestamp = creation_timestamp

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this Dataset.

        Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00)  # noqa: E501

        :return: The last_update_timestamp of this Dataset.
        :rtype: datetime
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this Dataset.

        Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00)  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this Dataset.
        :type last_update_timestamp: datetime
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def owning_account_id(self):
        """Gets the owning_account_id of this Dataset.

        [TBD] Alpha-numeric, unique id of dataset  # noqa: E501

        :return: The owning_account_id of this Dataset.
        :rtype: str
        """
        return self._owning_account_id

    @owning_account_id.setter
    def owning_account_id(self, owning_account_id):
        """Sets the owning_account_id of this Dataset.

        [TBD] Alpha-numeric, unique id of dataset  # noqa: E501

        :param owning_account_id: The owning_account_id of this Dataset.
        :type owning_account_id: str
        """

        self._owning_account_id = owning_account_id

    @property
    def name(self):
        """Gets the name of this Dataset.

        [TBD] Alpha-numeric, name of dataset  # noqa: E501

        :return: The name of this Dataset.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dataset.

        [TBD] Alpha-numeric, name of dataset  # noqa: E501

        :param name: The name of this Dataset.
        :type name: str
        """

        self._name = name

    @property
    def image(self):
        """Gets the image of this Dataset.


        :return: The image of this Dataset.
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Dataset.


        :param image: The image of this Dataset.
        :type image: Image
        """

        self._image = image

    @property
    def storage_cost(self):
        """Gets the storage_cost of this Dataset.

        cost for storage in dollars per month  # noqa: E501

        :return: The storage_cost of this Dataset.
        :rtype: float
        """
        return self._storage_cost

    @storage_cost.setter
    def storage_cost(self, storage_cost):
        """Sets the storage_cost of this Dataset.

        cost for storage in dollars per month  # noqa: E501

        :param storage_cost: The storage_cost of this Dataset.
        :type storage_cost: float
        """

        self._storage_cost = storage_cost
