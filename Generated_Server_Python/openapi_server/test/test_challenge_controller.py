# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.archived_shard import ArchivedShard  # noqa: E501
from openapi_server.models.assign_users_request import AssignUsersRequest  # noqa: E501
from openapi_server.models.challenge import Challenge  # noqa: E501
from openapi_server.models.challenge_budget_request import ChallengeBudgetRequest  # noqa: E501
from openapi_server.models.challenge_budget_response import ChallengeBudgetResponse  # noqa: E501
from openapi_server.models.challenge_statistics import ChallengeStatistics  # noqa: E501
from openapi_server.models.patch_challenge import PatchChallenge  # noqa: E501
from openapi_server.models.tagged_media_item import TaggedMediaItem  # noqa: E501
from openapi_server.test import BaseTestCase


class TestChallengeController(BaseTestCase):
    """ChallengeController integration test stubs"""

    def test_archive_shard(self):
        """Test case for archive_shard

        Archive shard from challenges
        """
        query_string = [('force', True)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/challenge/{challenge_id}/archive/{shard}'.format(challenge_id='challenge_id_example', shard=56),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_archived_shard_list(self):
        """Test case for archived_shard_list

        Get archive list from challenges
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/challenge/{challenge_id}/archive/list'.format(challenge_id='challenge_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consummes. See https://github.com/zalando/connexion/pull/760")
    def test_assign_challenge(self):
        """Test case for assign_challenge

        Assign a private challenge.
        """
        assign_users_request = {
  "challengeId" : "challengeId",
  "avatarIds" : [ "avatarIds", "avatarIds" ]
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/challenge/assign',
            method='POST',
            headers=headers,
            data=json.dumps(assign_users_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_assign_tenant_to_challenge(self):
        """Test case for assign_tenant_to_challenge

        Star a public challenge.
        """
        headers = { 
        }
        response = self.client.open(
            '/challenge/{challenge_id}/assign-tenant/{tenant_id}'.format(challenge_id='challenge_id_example', tenant_id='tenant_id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consummes. See https://github.com/zalando/connexion/pull/760")
    def test_create_challenge(self):
        """Test case for create_challenge

        Create a new challenge.
        """
        challenge = {
  "completionPercentageForCollaborator" : 70,
  "dispatchPolicyId" : "DFK768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "supplierTenantId" : "Dogs",
  "edgeTaxonomy" : "is a, has a",
  "initialNumberOfShards" : 4,
  "demanderTenantId" : "Dogs",
  "description" : "Tag the cats",
  "resolution" : "Tag the cats",
  "nodeTaxonomy" : "consumer,overdue",
  "completionPercentages" : [ {
    "stages" : [ {
      "percentage" : 100,
      "stageNumber" : 1
    }, {
      "percentage" : 100,
      "stageNumber" : 1
    } ],
    "shard" : 1
  }, {
    "stages" : [ {
      "percentage" : 100,
      "stageNumber" : 1
    }, {
      "percentage" : 100,
      "stageNumber" : 1
    } ],
    "shard" : 1
  } ],
  "creationTimestamp" : "2000-01-23T04:56:07.000+00:00",
  "datasetId" : "DFK768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "budget" : 3.14,
  "challengeAccessToken" : "DFK768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "datasetMetadata" : {
    "mediaItems" : 1000,
    "numberOfShards" : 4,
    "name" : "Dogs"
  },
  "completionPercentage" : 70,
  "challengeId" : "DFK768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "name" : "Dogs",
  "expiration" : 4,
  "evaluationPolicyId" : "DFK768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "stared" : true,
  "estimatedTagsPerMediaItem" : 4
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/challenge',
            method='POST',
            headers=headers,
            data=json.dumps(challenge),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_download_challenge(self):
        """Test case for download_challenge

        Download tagged items from challenges
        """
        query_string = [('X-Auth-Credential', 'x_auth_credential_example')]
        headers = { 
        }
        response = self.client.open(
            '/challenge/{challenge_id}/download/{shard}'.format(challenge_id='challenge_id_example', shard=56),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_force_merge_tagged_media_item(self):
        """Test case for force_merge_tagged_media_item

        force merge
        """
        query_string = [('challengeName', 'challenge_name_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/challenge/{challenge_id}/force-merge'.format(challenge_id='challenge_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_challenge(self):
        """Test case for get_challenge

        Retrieve list of challenges
        """
        query_string = [('accessToken', 'access_token_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/challenge/{challenge_id}'.format(challenge_id='challenge_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consummes. See https://github.com/zalando/connexion/pull/760")
    def test_get_challenge_cost(self):
        """Test case for get_challenge_cost

        get estimated cost for challenge
        """
        challenge_budget_request = {
  "dispatchPolicyId" : "DFK768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "datasetId" : "XAFKE80768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "evaluationPolicyId" : "DFK768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "estimatedTagsPerMediaItem" : 4
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/challenge/cost',
            method='POST',
            headers=headers,
            data=json.dumps(challenge_budget_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_challenge_list_broker(self):
        """Test case for get_challenge_list_broker

        Retrieve list of challenges
        """
        query_string = [('challengeName', 'challenge_name_example'),
                        ('accessType', 'access_type_example'),
                        ('liked', True),
                        ('pageSize', 56),
                        ('pageNumber', 56)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/challenge/broker/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_challenge_list_collaborator(self):
        """Test case for get_challenge_list_collaborator

        Retrieve list of challenges
        """
        query_string = [('challengeName', 'challenge_name_example'),
                        ('accessType', 'access_type_example'),
                        ('liked', True),
                        ('pageSize', 56),
                        ('pageNumber', 56)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/challenge/collaborator/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_challenge_list_supervisor(self):
        """Test case for get_challenge_list_supervisor

        Retrieve list of challenges
        """
        query_string = [('challengeName', 'challenge_name_example'),
                        ('accessType', 'access_type_example'),
                        ('liked', True),
                        ('pageSize', 56),
                        ('pageNumber', 56)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/challenge/supervisor/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_tagged_items(self):
        """Test case for get_tagged_items

        Retrieve list tagged media items
        """
        query_string = [('pageSize', 56),
                        ('pageNumber', 56),
                        ('stage', 56),
                        ('accessToken', 'access_token_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/challenge/{challenge_id}/tagged-item/list'.format(challenge_id='challenge_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consummes. See https://github.com/zalando/connexion/pull/760")
    def test_patch_challenge(self):
        """Test case for patch_challenge

        Update challenge.
        """
        patch_challenge = {
  "dispatchPolicyId" : "DFK768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "name" : "Dogs",
  "description" : "Tag the cats",
  "evaluationPolicyId" : "DFK768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "budget" : 3.14
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/challenge/{challenge_id}'.format(challenge_id='challenge_id_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(patch_challenge),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reject_challenge(self):
        """Test case for reject_challenge

        Star a public challenge.
        """
        body = 'body_example'
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/challenge/{challenge_id}/reject'.format(challenge_id='challenge_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_star_challenge(self):
        """Test case for star_challenge

        Star a public challenge.
        """
        headers = { 
        }
        response = self.client.open(
            '/challenge/{challenge_id}/star'.format(challenge_id='challenge_id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_statistics_challenge(self):
        """Test case for statistics_challenge

        Get challenge statistics
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/challenge/{challenge_id}/statistics'.format(challenge_id='challenge_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
