# coding: utf-8

"""
    DeepVISS TAG

    DeepVISS (Deep Vision Interoperability Specification Standard) allows several computer vision solutions to produce, consume and exchange events in the same format.  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: office@deepviss.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.dataset_api import DatasetApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDatasetApi(unittest.TestCase):
    """DatasetApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.dataset_api.DatasetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_media_item(self):
        """Test case for add_media_item

        add media items to dataset  # noqa: E501
        """
        pass

    def test_create_dataset(self):
        """Test case for create_dataset

        Retrieve list of datasets  # noqa: E501
        """
        pass

    def test_delete_dataset(self):
        """Test case for delete_dataset

        Delete dataset  # noqa: E501
        """
        pass

    def test_get_dataset(self):
        """Test case for get_dataset

        Retrieve dataset info  # noqa: E501
        """
        pass

    def test_get_dataset_list(self):
        """Test case for get_dataset_list

        Retrieve list of datasets  # noqa: E501
        """
        pass

    def test_get_dataset_static_images(self):
        """Test case for get_dataset_static_images

        Retrieve list of static images  # noqa: E501
        """
        pass

    def test_get_storage_cost(self):
        """Test case for get_storage_cost

        get estimated cost for storage  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
