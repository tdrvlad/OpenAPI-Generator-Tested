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
from openapi_client.api.challenge_api import ChallengeApi  # noqa: E501
from openapi_client.rest import ApiException


class TestChallengeApi(unittest.TestCase):
    """ChallengeApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.challenge_api.ChallengeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_archive_shard(self):
        """Test case for archive_shard

        Archive shard from challenges  # noqa: E501
        """
        pass

    def test_archived_shard_list(self):
        """Test case for archived_shard_list

        Get archive list from challenges  # noqa: E501
        """
        pass

    def test_assign_challenge(self):
        """Test case for assign_challenge

        Assign a private challenge.  # noqa: E501
        """
        pass

    def test_assign_tenant_to_challenge(self):
        """Test case for assign_tenant_to_challenge

        Star a public challenge.  # noqa: E501
        """
        pass

    def test_create_challenge(self):
        """Test case for create_challenge

        Create a new challenge.  # noqa: E501
        """
        pass

    def test_download_challenge(self):
        """Test case for download_challenge

        Download tagged items from challenges  # noqa: E501
        """
        pass

    def test_force_merge_tagged_media_item(self):
        """Test case for force_merge_tagged_media_item

        force merge  # noqa: E501
        """
        pass

    def test_get_challenge(self):
        """Test case for get_challenge

        Retrieve list of challenges  # noqa: E501
        """
        pass

    def test_get_challenge_cost(self):
        """Test case for get_challenge_cost

        get estimated cost for challenge  # noqa: E501
        """
        pass

    def test_get_challenge_list_broker(self):
        """Test case for get_challenge_list_broker

        Retrieve list of challenges  # noqa: E501
        """
        pass

    def test_get_challenge_list_collaborator(self):
        """Test case for get_challenge_list_collaborator

        Retrieve list of challenges  # noqa: E501
        """
        pass

    def test_get_challenge_list_supervisor(self):
        """Test case for get_challenge_list_supervisor

        Retrieve list of challenges  # noqa: E501
        """
        pass

    def test_get_tagged_items(self):
        """Test case for get_tagged_items

        Retrieve list tagged media items  # noqa: E501
        """
        pass

    def test_patch_challenge(self):
        """Test case for patch_challenge

        Update challenge.  # noqa: E501
        """
        pass

    def test_reject_challenge(self):
        """Test case for reject_challenge

        Star a public challenge.  # noqa: E501
        """
        pass

    def test_star_challenge(self):
        """Test case for star_challenge

        Star a public challenge.  # noqa: E501
        """
        pass

    def test_statistics_challenge(self):
        """Test case for statistics_challenge

        Get challenge statistics  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()