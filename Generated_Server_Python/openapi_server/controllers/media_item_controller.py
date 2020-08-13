import connexion
import six

from openapi_server.models.media_item import MediaItem  # noqa: E501
from openapi_server import util


def delete_media_items(request_body):  # noqa: E501
    """Delete mediaItem

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param request_body: The challenge object to be created
    :type request_body: List[str]

    :rtype: None
    """
    return 'do some magic!'


def get_media_item(bucket_name, media_item):  # noqa: E501
    """Retrieve media item

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param bucket_name: bucket name
    :type bucket_name: str
    :param media_item: media item
    :type media_item: str

    :rtype: bytearray
    """
    return 'do some magic!'


def get_media_item_list(dataset_id, page_size=None, page_number=None):  # noqa: E501
    """Retrieve list of mediaItems

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param dataset_id: 
    :type dataset_id: str
    :param page_size: 
    :type page_size: int
    :param page_number: 
    :type page_number: int

    :rtype: List[MediaItem]
    """
    return 'do some magic!'
