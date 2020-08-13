# openapi_client.DispatchPolicyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dispatch_policy**](DispatchPolicyApi.md#create_dispatch_policy) | **POST** /dispatch-policy | Create a new dispatchPolicy.
[**get_dispatch_policy_list**](DispatchPolicyApi.md#get_dispatch_policy_list) | **GET** /dispatch-policy/list | Retrieve list of dispatch policies


# **create_dispatch_policy**
> DispatchPolicy create_dispatch_policy(dispatch_policy)

Create a new dispatchPolicy.

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
    api_instance = openapi_client.DispatchPolicyApi(api_client)
    dispatch_policy = openapi_client.DispatchPolicy() # DispatchPolicy | The dispatchPolicy object to be created

    try:
        # Create a new dispatchPolicy.
        api_response = api_instance.create_dispatch_policy(dispatch_policy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DispatchPolicyApi->create_dispatch_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispatch_policy** | [**DispatchPolicy**](DispatchPolicy.md)| The dispatchPolicy object to be created | 

### Return type

[**DispatchPolicy**](DispatchPolicy.md)

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

# **get_dispatch_policy_list**
> list[DispatchPolicy] get_dispatch_policy_list()

Retrieve list of dispatch policies

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
    api_instance = openapi_client.DispatchPolicyApi(api_client)
    
    try:
        # Retrieve list of dispatch policies
        api_response = api_instance.get_dispatch_policy_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DispatchPolicyApi->get_dispatch_policy_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DispatchPolicy]**](DispatchPolicy.md)

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

