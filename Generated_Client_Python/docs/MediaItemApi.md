# openapi_client.MediaItemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_media_items**](MediaItemApi.md#delete_media_items) | **DELETE** /media-item | Delete mediaItem
[**get_media_item**](MediaItemApi.md#get_media_item) | **GET** /media-item/{bucketName}/{mediaItem} | Retrieve media item
[**get_media_item_list**](MediaItemApi.md#get_media_item_list) | **GET** /media-item/{datasetId}/list | Retrieve list of mediaItems


# **delete_media_items**
> delete_media_items(request_body)

Delete mediaItem

Multiple status values can be provided with comma separated strings

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MediaItemApi(api_client)
    request_body = ['request_body_example'] # list[str] | The challenge object to be created

    try:
        # Delete mediaItem
        api_instance.delete_media_items(request_body)
    except ApiException as e:
        print("Exception when calling MediaItemApi->delete_media_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](str.md)| The challenge object to be created | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_item**
> str get_media_item(bucket_name, media_item)

Retrieve media item

Multiple status values can be provided with comma separated strings

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MediaItemApi(api_client)
    bucket_name = 'bucket_name_example' # str | bucket name
media_item = 'media_item_example' # str | media item

    try:
        # Retrieve media item
        api_response = api_instance.get_media_item(bucket_name, media_item)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaItemApi->get_media_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**| bucket name | 
 **media_item** | **str**| media item | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_item_list**
> list[MediaItem] get_media_item_list(dataset_id, page_size=page_size, page_number=page_number)

Retrieve list of mediaItems

Multiple status values can be provided with comma separated strings

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MediaItemApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
page_size = 56 # int |  (optional)
page_number = 56 # int |  (optional)

    try:
        # Retrieve list of mediaItems
        api_response = api_instance.get_media_item_list(dataset_id, page_size=page_size, page_number=page_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaItemApi->get_media_item_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **page_size** | **int**|  | [optional] 
 **page_number** | **int**|  | [optional] 

### Return type

[**list[MediaItem]**](MediaItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

