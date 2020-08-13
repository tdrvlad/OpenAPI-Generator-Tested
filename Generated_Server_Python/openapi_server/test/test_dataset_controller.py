# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.dataset import Dataset  # noqa: E501
from openapi_server.models.dataset_storage_cost import DatasetStorageCost  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDatasetController(BaseTestCase):
    """DatasetController integration test stubs"""

    def test_add_media_item(self):
        """Test case for add_media_item

        add media items to dataset
        """
        headers = { 
        }
        response = self.client.open(
            '/dataset/media-item/{dataset_id}'.format(dataset_id='dataset_id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_dataset(self):
        """Test case for create_dataset

        Retrieve list of datasets
        """
        query_string = [('datasetName', 'dataset_name_example'),
                        ('datasetType', 'dataset_type_example'),
                        ('staticImage', 'static_image_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/dataset',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consummes. See https://github.com/zalando/connexion/pull/760")
    def test_delete_dataset(self):
        """Test case for delete_dataset

        Delete dataset
        """
        request_body = ['request_body_example']
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/dataset',
            method='DELETE',
            headers=headers,
            data=json.dumps(request_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dataset(self):
        """Test case for get_dataset

        Retrieve dataset info
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/dataset/{dataset_id}'.format(dataset_id='dataset_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dataset_list(self):
        """Test case for get_dataset_list

        Retrieve list of datasets
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/dataset/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dataset_static_images(self):
        """Test case for get_dataset_static_images

        Retrieve list of static images
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/dataset/static-image/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_storage_cost(self):
        """Test case for get_storage_cost

        get estimated cost for storage
        """
        query_string = [('datasetId', 'dataset_id_example'),
                        ('size', 3.14)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/dataset/cost',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
