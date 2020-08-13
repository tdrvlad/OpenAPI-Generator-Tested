import connexion
import six

from openapi_server.models.dataset import Dataset  # noqa: E501
from openapi_server.models.dataset_storage_cost import DatasetStorageCost  # noqa: E501
from openapi_server import util


def add_media_item(dataset_id):  # noqa: E501
    """add media items to dataset

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param dataset_id: 
    :type dataset_id: str

    :rtype: None
    """
    return 'do some magic!'


def create_dataset(dataset_name=None, dataset_type=None, static_image=None):  # noqa: E501
    """Retrieve list of datasets

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param dataset_name: 
    :type dataset_name: str
    :param dataset_type: 
    :type dataset_type: str
    :param static_image: 
    :type static_image: str

    :rtype: Dataset
    """
    return 'do some magic!'


def delete_dataset(request_body):  # noqa: E501
    """Delete dataset

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param request_body: The challenge object to be created
    :type request_body: List[str]

    :rtype: None
    """
    return 'do some magic!'


def get_dataset(dataset_id):  # noqa: E501
    """Retrieve dataset info

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param dataset_id: The identifier of the dataset
    :type dataset_id: str

    :rtype: Dataset
    """
    return 'do some magic!'


def get_dataset_list():  # noqa: E501
    """Retrieve list of datasets

    Multiple status values can be provided with comma separated strings # noqa: E501


    :rtype: List[Dataset]
    """
    return 'do some magic!'


def get_dataset_static_images():  # noqa: E501
    """Retrieve list of static images

    Multiple status values can be provided with comma separated strings # noqa: E501


    :rtype: List[str]
    """
    return 'do some magic!'


def get_storage_cost(dataset_id=None, size=None):  # noqa: E501
    """get estimated cost for storage

    optional parameter datasetId for new shards # noqa: E501

    :param dataset_id: 
    :type dataset_id: str
    :param size: 
    :type size: float

    :rtype: DatasetStorageCost
    """
    return 'do some magic!'
