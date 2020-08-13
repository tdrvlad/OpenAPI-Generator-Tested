# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.dispatch_policy import DispatchPolicy  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDispatchPolicyController(BaseTestCase):
    """DispatchPolicyController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consummes. See https://github.com/zalando/connexion/pull/760")
    def test_create_dispatch_policy(self):
        """Test case for create_dispatch_policy

        Create a new dispatchPolicy.
        """
        dispatch_policy = {
  "dispatchPolicyId" : "dispatchPolicyId",
  "mediaItemLockTimeout" : 10,
  "numberOfUsers" : 3,
  "name" : "Fast"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/dispatch-policy',
            method='POST',
            headers=headers,
            data=json.dumps(dispatch_policy),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dispatch_policy_list(self):
        """Test case for get_dispatch_policy_list

        Retrieve list of dispatch policies
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/dispatch-policy/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
