import connexion
import six

from openapi_server.models.get_task_response import GetTaskResponse  # noqa: E501
from openapi_server.models.task import Task  # noqa: E501
from openapi_server import util


def get_task(challenge_id):  # noqa: E501
    """Get new task

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param challenge_id: The identifier of the challenge
    :type challenge_id: str

    :rtype: GetTaskResponse
    """
    return 'do some magic!'


def submit_task(task_id, task):  # noqa: E501
    """Submit  task

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param task_id: The identifier of the challenge
    :type task_id: str
    :param task: task object
    :type task: dict | bytes

    :rtype: Task
    """
    if connexion.request.is_json:
        task = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
