import connexion
import six

from openapi_server.models.dispatch_policy import DispatchPolicy  # noqa: E501
from openapi_server import util


def create_dispatch_policy(dispatch_policy):  # noqa: E501
    """Create a new dispatchPolicy.

     # noqa: E501

    :param dispatch_policy: The dispatchPolicy object to be created
    :type dispatch_policy: dict | bytes

    :rtype: DispatchPolicy
    """
    if connexion.request.is_json:
        dispatch_policy = DispatchPolicy.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_dispatch_policy_list():  # noqa: E501
    """Retrieve list of dispatch policies

    Multiple status values can be provided with comma separated strings # noqa: E501


    :rtype: List[DispatchPolicy]
    """
    return 'do some magic!'
