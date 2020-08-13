# openapi_client.TaskApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task**](TaskApi.md#get_task) | **GET** /task/{challengeId} | Get new task
[**submit_task**](TaskApi.md#submit_task) | **POST** /task/{taskId}/submit | Submit  task


# **get_task**
> GetTaskResponse get_task(challenge_id)

Get new task

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
    api_instance = openapi_client.TaskApi(api_client)
    challenge_id = 'challenge_id_example' # str | The identifier of the challenge

    try:
        # Get new task
        api_response = api_instance.get_task(challenge_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**| The identifier of the challenge | 

### Return type

[**GetTaskResponse**](GetTaskResponse.md)

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

# **submit_task**
> Task submit_task(task_id, task)

Submit  task

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
    api_instance = openapi_client.TaskApi(api_client)
    task_id = 'task_id_example' # str | The identifier of the challenge
task = openapi_client.Task() # Task | task object

    try:
        # Submit  task
        api_response = api_instance.submit_task(task_id, task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->submit_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of the challenge | 
 **task** | [**Task**](Task.md)| task object | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

