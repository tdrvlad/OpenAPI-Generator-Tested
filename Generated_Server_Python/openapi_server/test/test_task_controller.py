# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.get_task_response import GetTaskResponse  # noqa: E501
from openapi_server.models.task import Task  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTaskController(BaseTestCase):
    """TaskController integration test stubs"""

    def test_get_task(self):
        """Test case for get_task

        Get new task
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/task/{challenge_id}'.format(challenge_id='challenge_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consummes. See https://github.com/zalando/connexion/pull/760")
    def test_submit_task(self):
        """Test case for submit_task

        Submit  task
        """
        task = {
  "image" : {
    "imageBase64" : "imageBase64",
    "imageURL" : "imageURL",
    "imageContentType" : "imageContentType"
  },
  "edges" : [ {
    "destinationTagID" : "7300124455B07E91CB289F87791D78064ECC93754F19B13D419489F1",
    "destinationTextBoxId" : "1",
    "elasticity" : 5.962133916683182,
    "edgeType" : "has-greater-area",
    "slack" : 0.0,
    "sourceTagId" : "87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
    "sourceTextBoxId" : "1",
    "internalSubjectiveOpinion" : {
      "baseRateNumerator" : 1,
      "commonDenominator" : 1,
      "unattributedUncertaintyNumerator" : 1,
      "opinionEmitterId" : "ocr",
      "attributedBeliefNumerator" : 5,
      "opinionReasonId" : "unreadable",
      "attributedDisbeliefNumerator" : 2
    }
  }, {
    "destinationTagID" : "7300124455B07E91CB289F87791D78064ECC93754F19B13D419489F1",
    "destinationTextBoxId" : "1",
    "elasticity" : 5.962133916683182,
    "edgeType" : "has-greater-area",
    "slack" : 0.0,
    "sourceTagId" : "87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
    "sourceTextBoxId" : "1",
    "internalSubjectiveOpinion" : {
      "baseRateNumerator" : 1,
      "commonDenominator" : 1,
      "unattributedUncertaintyNumerator" : 1,
      "opinionEmitterId" : "ocr",
      "attributedBeliefNumerator" : 5,
      "opinionReasonId" : "unreadable",
      "attributedDisbeliefNumerator" : 2
    }
  } ],
  "challengeDescription" : "Tag the cats",
  "generationTimestamp" : "2000-01-23T04:56:07.000+00:00",
  "resolution" : {
    "description" : "Reported for ..."
  },
  "submissionTimestamp" : "2000-01-23T04:56:07.000+00:00",
  "tags" : [ {
    "tagId" : "B07E91CB289F87791D78064ECC93754F19B13D419489F162",
    "geometry" : [ {
      "shapeType" : "Shape2DReactangle",
      "shapeId" : "791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E"
    }, {
      "shapeType" : "Shape2DReactangle",
      "shapeId" : "791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E"
    } ],
    "nodeType" : "vehicle",
    "taskId" : "1CB289F87791D78064ECC93754F19B13D419489F162A",
    "internalSubjectiveOpinion" : {
      "baseRateNumerator" : 1,
      "commonDenominator" : 1,
      "unattributedUncertaintyNumerator" : 1,
      "opinionEmitterId" : "ocr",
      "attributedBeliefNumerator" : 5,
      "opinionReasonId" : "unreadable",
      "attributedDisbeliefNumerator" : 2
    },
    "submissionTimestamp" : "2000-01-23T04:56:07.000+00:00"
  }, {
    "tagId" : "B07E91CB289F87791D78064ECC93754F19B13D419489F162",
    "geometry" : [ {
      "shapeType" : "Shape2DReactangle",
      "shapeId" : "791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E"
    }, {
      "shapeType" : "Shape2DReactangle",
      "shapeId" : "791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E"
    } ],
    "nodeType" : "vehicle",
    "taskId" : "1CB289F87791D78064ECC93754F19B13D419489F162A",
    "internalSubjectiveOpinion" : {
      "baseRateNumerator" : 1,
      "commonDenominator" : 1,
      "unattributedUncertaintyNumerator" : 1,
      "opinionEmitterId" : "ocr",
      "attributedBeliefNumerator" : 5,
      "opinionReasonId" : "unreadable",
      "attributedDisbeliefNumerator" : 2
    },
    "submissionTimestamp" : "2000-01-23T04:56:07.000+00:00"
  } ],
  "challengeId" : "7E43358680768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "avatarId" : "7E43358680768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E",
  "attemptSequenceNumber" : 2,
  "challengeName" : "Tag Cats",
  "evaluationStatus" : "unallocated",
  "taskId" : "7E43358680768EF053898993DD196397EDFDDFBC81751818B7FD1300124455B07E91CB289F87791D78064ECC93754F19B13D419489F162A150A22DD814CKAF0E"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/task/{task_id}/submit'.format(task_id='task_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(task),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
