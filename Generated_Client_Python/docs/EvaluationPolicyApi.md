# openapi_client.EvaluationPolicyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_evaluation_policy**](EvaluationPolicyApi.md#create_evaluation_policy) | **POST** /evaluation-policy | Create a new evaluationPolicy.
[**get_evaluation_policy_list**](EvaluationPolicyApi.md#get_evaluation_policy_list) | **GET** /evaluation-policy/list | Retrieve list of evaluation policies


# **create_evaluation_policy**
> EvaluationPolicy create_evaluation_policy(evaluation_policy)

Create a new evaluationPolicy.

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
    api_instance = openapi_client.EvaluationPolicyApi(api_client)
    evaluation_policy = openapi_client.EvaluationPolicy() # EvaluationPolicy | The evaluationPolicy object to be created

    try:
        # Create a new evaluationPolicy.
        api_response = api_instance.create_evaluation_policy(evaluation_policy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EvaluationPolicyApi->create_evaluation_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluation_policy** | [**EvaluationPolicy**](EvaluationPolicy.md)| The evaluationPolicy object to be created | 

### Return type

[**EvaluationPolicy**](EvaluationPolicy.md)

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

# **get_evaluation_policy_list**
> list[EvaluationPolicy] get_evaluation_policy_list()

Retrieve list of evaluation policies

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
    api_instance = openapi_client.EvaluationPolicyApi(api_client)
    
    try:
        # Retrieve list of evaluation policies
        api_response = api_instance.get_evaluation_policy_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EvaluationPolicyApi->get_evaluation_policy_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EvaluationPolicy]**](EvaluationPolicy.md)

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

