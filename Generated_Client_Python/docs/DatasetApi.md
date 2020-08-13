# openapi_client.DatasetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_media_item**](DatasetApi.md#add_media_item) | **POST** /dataset/media-item/{datasetId} | add media items to dataset
[**create_dataset**](DatasetApi.md#create_dataset) | **POST** /dataset | Retrieve list of datasets
[**delete_dataset**](DatasetApi.md#delete_dataset) | **DELETE** /dataset | Delete dataset
[**get_dataset**](DatasetApi.md#get_dataset) | **GET** /dataset/{datasetId} | Retrieve dataset info
[**get_dataset_list**](DatasetApi.md#get_dataset_list) | **GET** /dataset/list | Retrieve list of datasets
[**get_dataset_static_images**](DatasetApi.md#get_dataset_static_images) | **GET** /dataset/static-image/list | Retrieve list of static images
[**get_storage_cost**](DatasetApi.md#get_storage_cost) | **GET** /dataset/cost | get estimated cost for storage


# **add_media_item**
> add_media_item(dataset_id)

add media items to dataset

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
    api_instance = openapi_client.DatasetApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        # add media items to dataset
        api_instance.add_media_item(dataset_id)
    except ApiException as e:
        print("Exception when calling DatasetApi->add_media_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dataset**
> Dataset create_dataset(dataset_name=dataset_name, dataset_type=dataset_type, static_image=static_image)

Retrieve list of datasets

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
    api_instance = openapi_client.DatasetApi(api_client)
    dataset_name = 'dataset_name_example' # str |  (optional)
dataset_type = 'dataset_type_example' # str |  (optional)
static_image = 'static_image_example' # str |  (optional)

    try:
        # Retrieve list of datasets
        api_response = api_instance.create_dataset(dataset_name=dataset_name, dataset_type=dataset_type, static_image=static_image)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->create_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | [optional] 
 **dataset_type** | **str**|  | [optional] 
 **static_image** | **str**|  | [optional] 

### Return type

[**Dataset**](Dataset.md)

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

# **delete_dataset**
> delete_dataset(request_body)

Delete dataset

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
    api_instance = openapi_client.DatasetApi(api_client)
    request_body = ['request_body_example'] # list[str] | The challenge object to be created

    try:
        # Delete dataset
        api_instance.delete_dataset(request_body)
    except ApiException as e:
        print("Exception when calling DatasetApi->delete_dataset: %s\n" % e)
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

# **get_dataset**
> Dataset get_dataset(dataset_id)

Retrieve dataset info

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
    api_instance = openapi_client.DatasetApi(api_client)
    dataset_id = 'dataset_id_example' # str | The identifier of the dataset

    try:
        # Retrieve dataset info
        api_response = api_instance.get_dataset(dataset_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->get_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The identifier of the dataset | 

### Return type

[**Dataset**](Dataset.md)

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

# **get_dataset_list**
> list[Dataset] get_dataset_list()

Retrieve list of datasets

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
    api_instance = openapi_client.DatasetApi(api_client)
    
    try:
        # Retrieve list of datasets
        api_response = api_instance.get_dataset_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->get_dataset_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Dataset]**](Dataset.md)

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

# **get_dataset_static_images**
> list[str] get_dataset_static_images()

Retrieve list of static images

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
    api_instance = openapi_client.DatasetApi(api_client)
    
    try:
        # Retrieve list of static images
        api_response = api_instance.get_dataset_static_images()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->get_dataset_static_images: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

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

# **get_storage_cost**
> DatasetStorageCost get_storage_cost(dataset_id=dataset_id, size=size)

get estimated cost for storage

optional parameter datasetId for new shards

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
    api_instance = openapi_client.DatasetApi(api_client)
    dataset_id = 'dataset_id_example' # str |  (optional)
size = 3.14 # float |  (optional)

    try:
        # get estimated cost for storage
        api_response = api_instance.get_storage_cost(dataset_id=dataset_id, size=size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->get_storage_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | [optional] 
 **size** | **float**|  | [optional] 

### Return type

[**DatasetStorageCost**](DatasetStorageCost.md)

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

