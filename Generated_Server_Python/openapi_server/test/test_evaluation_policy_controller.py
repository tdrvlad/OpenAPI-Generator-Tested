# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.evaluation_policy import EvaluationPolicy  # noqa: E501
from openapi_server.test import BaseTestCase


class TestEvaluationPolicyController(BaseTestCase):
    """EvaluationPolicyController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consummes. See https://github.com/zalando/connexion/pull/760")
    def test_create_evaluation_policy(self):
        """Test case for create_evaluation_policy

        Create a new evaluationPolicy.
        """
        evaluation_policy = {
  "rankOfMean" : 1.0,
  "name" : "Lightwight",
  "harshness" : 0.5,
  "evaluationPolicyId" : "evaluationPolicyId",
  "summationType" : "algebraic",
  "spatialOverlapThreshold" : 0.5
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/evaluation-policy',
            method='POST',
            headers=headers,
            data=json.dumps(evaluation_policy),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_evaluation_policy_list(self):
        """Test case for get_evaluation_policy_list

        Retrieve list of evaluation policies
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/evaluation-policy/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
