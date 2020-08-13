import connexion
import six

from openapi_server.models.evaluation_policy import EvaluationPolicy  # noqa: E501
from openapi_server import util


def create_evaluation_policy(evaluation_policy):  # noqa: E501
    """Create a new evaluationPolicy.

     # noqa: E501

    :param evaluation_policy: The evaluationPolicy object to be created
    :type evaluation_policy: dict | bytes

    :rtype: EvaluationPolicy
    """
    if connexion.request.is_json:
        evaluation_policy = EvaluationPolicy.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_evaluation_policy_list():  # noqa: E501
    """Retrieve list of evaluation policies

    Multiple status values can be provided with comma separated strings # noqa: E501


    :rtype: List[EvaluationPolicy]
    """
    return 'do some magic!'
