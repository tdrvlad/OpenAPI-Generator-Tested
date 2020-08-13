# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.media_item import MediaItem  # noqa: E501
from openapi_server.test import BaseTestCase


class TestMediaItemController(BaseTestCase):
    """MediaItemController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consummes. See https://github.com/zalando/connexion/pull/760")
    def test_delete_media_items(self):
        """Test case for delete_media_items

        Delete mediaItem
        """
        request_body = ['request_body_example']
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/media-item',
            method='DELETE',
            headers=headers,
            data=json.dumps(request_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_media_item(self):
        """Test case for get_media_item

        Retrieve media item
        """
        headers = { 
            'Accept': 'image/png',
        }
        response = self.client.open(
            '/media-item/{bucket_name}/{media_item}'.format(bucket_name='bucket_name_example', media_item='media_item_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_media_item_list(self):
        """Test case for get_media_item_list

        Retrieve list of mediaItems
        """
        query_string = [('pageSize', 56),
                        ('pageNumber', 56)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/media-item/{dataset_id}/list'.format(dataset_id='dataset_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
