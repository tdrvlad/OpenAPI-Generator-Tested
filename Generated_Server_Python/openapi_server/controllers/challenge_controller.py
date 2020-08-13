import connexion
import six

from openapi_server.models.archived_shard import ArchivedShard  # noqa: E501
from openapi_server.models.assign_users_request import AssignUsersRequest  # noqa: E501
from openapi_server.models.challenge import Challenge  # noqa: E501
from openapi_server.models.challenge_budget_request import ChallengeBudgetRequest  # noqa: E501
from openapi_server.models.challenge_budget_response import ChallengeBudgetResponse  # noqa: E501
from openapi_server.models.challenge_statistics import ChallengeStatistics  # noqa: E501
from openapi_server.models.patch_challenge import PatchChallenge  # noqa: E501
from openapi_server.models.tagged_media_item import TaggedMediaItem  # noqa: E501
from openapi_server import util


def archive_shard(challenge_id, shard, force=None):  # noqa: E501
    """Archive shard from challenges

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param challenge_id: The identifier of the challenge
    :type challenge_id: str
    :param shard: The identifier of the shard
    :type shard: int
    :param force: 
    :type force: bool

    :rtype: ArchivedShard
    """
    return 'do some magic!'


def archived_shard_list(challenge_id):  # noqa: E501
    """Get archive list from challenges

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param challenge_id: The identifier of the challenge
    :type challenge_id: str

    :rtype: List[ArchivedShard]
    """
    return 'do some magic!'


def assign_challenge(assign_users_request):  # noqa: E501
    """Assign a private challenge.

     # noqa: E501

    :param assign_users_request: The users to be assigned to a challenge
    :type assign_users_request: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        assign_users_request = AssignUsersRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def assign_tenant_to_challenge(challenge_id, tenant_id):  # noqa: E501
    """Star a public challenge.

     # noqa: E501

    :param challenge_id: 
    :type challenge_id: str
    :param tenant_id: 
    :type tenant_id: str

    :rtype: None
    """
    return 'do some magic!'


def create_challenge(challenge):  # noqa: E501
    """Create a new challenge.

     # noqa: E501

    :param challenge: The challenge object to be created
    :type challenge: dict | bytes

    :rtype: Challenge
    """
    if connexion.request.is_json:
        challenge = Challenge.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def download_challenge(challenge_id, shard, x_auth_credential=None):  # noqa: E501
    """Download tagged items from challenges

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param challenge_id: The identifier of the challenge
    :type challenge_id: str
    :param shard: The identifier of the shard
    :type shard: int
    :param x_auth_credential: 
    :type x_auth_credential: str

    :rtype: None
    """
    return 'do some magic!'


def force_merge_tagged_media_item(challenge_id, challenge_name=None):  # noqa: E501
    """force merge

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param challenge_id: The identifier of the dataset
    :type challenge_id: str
    :param challenge_name: The identifier of the tagged media item
    :type challenge_name: str

    :rtype: Challenge
    """
    return 'do some magic!'


def get_challenge(challenge_id, access_token=None):  # noqa: E501
    """Retrieve list of challenges

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param challenge_id: The identifier of the dataset
    :type challenge_id: str
    :param access_token: 
    :type access_token: str

    :rtype: Challenge
    """
    return 'do some magic!'


def get_challenge_cost(challenge_budget_request):  # noqa: E501
    """get estimated cost for challenge

    estimage challenge budget # noqa: E501

    :param challenge_budget_request: The challenge options
    :type challenge_budget_request: dict | bytes

    :rtype: ChallengeBudgetResponse
    """
    if connexion.request.is_json:
        challenge_budget_request = ChallengeBudgetRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_challenge_list_broker(challenge_name=None, access_type=None, liked=None, page_size=None, page_number=None):  # noqa: E501
    """Retrieve list of challenges

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param challenge_name: 
    :type challenge_name: str
    :param access_type: 
    :type access_type: str
    :param liked: 
    :type liked: bool
    :param page_size: 
    :type page_size: int
    :param page_number: 
    :type page_number: int

    :rtype: List[Challenge]
    """
    return 'do some magic!'


def get_challenge_list_collaborator(challenge_name=None, access_type=None, liked=None, page_size=None, page_number=None):  # noqa: E501
    """Retrieve list of challenges

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param challenge_name: 
    :type challenge_name: str
    :param access_type: 
    :type access_type: str
    :param liked: 
    :type liked: bool
    :param page_size: 
    :type page_size: int
    :param page_number: 
    :type page_number: int

    :rtype: List[Challenge]
    """
    return 'do some magic!'


def get_challenge_list_supervisor(challenge_name=None, access_type=None, liked=None, page_size=None, page_number=None):  # noqa: E501
    """Retrieve list of challenges

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param challenge_name: 
    :type challenge_name: str
    :param access_type: 
    :type access_type: str
    :param liked: 
    :type liked: bool
    :param page_size: 
    :type page_size: int
    :param page_number: 
    :type page_number: int

    :rtype: List[Challenge]
    """
    return 'do some magic!'


def get_tagged_items(challenge_id, page_size=None, page_number=None, stage=None, access_token=None):  # noqa: E501
    """Retrieve list tagged media items

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param challenge_id: The identifier of the dataset
    :type challenge_id: str
    :param page_size: 
    :type page_size: int
    :param page_number: 
    :type page_number: int
    :param stage: 
    :type stage: int
    :param access_token: 
    :type access_token: str

    :rtype: List[TaggedMediaItem]
    """
    return 'do some magic!'


def patch_challenge(challenge_id, patch_challenge):  # noqa: E501
    """Update challenge.

     # noqa: E501

    :param challenge_id: The identifier of the dataset
    :type challenge_id: str
    :param patch_challenge: The new challenge object
    :type patch_challenge: dict | bytes

    :rtype: Challenge
    """
    if connexion.request.is_json:
        patch_challenge = PatchChallenge.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def reject_challenge(challenge_id, body):  # noqa: E501
    """Star a public challenge.

     # noqa: E501

    :param challenge_id: 
    :type challenge_id: str
    :param body: The challenge object to be created
    :type body: str

    :rtype: None
    """
    return 'do some magic!'


def star_challenge(challenge_id):  # noqa: E501
    """Star a public challenge.

     # noqa: E501

    :param challenge_id: 
    :type challenge_id: str

    :rtype: None
    """
    return 'do some magic!'


def statistics_challenge(challenge_id):  # noqa: E501
    """Get challenge statistics

     # noqa: E501

    :param challenge_id: 
    :type challenge_id: str

    :rtype: ChallengeStatistics
    """
    return 'do some magic!'
