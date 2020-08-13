# openapi_client.ChallengeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_shard**](ChallengeApi.md#archive_shard) | **GET** /challenge/{challengeId}/archive/{shard} | Archive shard from challenges
[**archived_shard_list**](ChallengeApi.md#archived_shard_list) | **GET** /challenge/{challengeId}/archive/list | Get archive list from challenges
[**assign_challenge**](ChallengeApi.md#assign_challenge) | **POST** /challenge/assign | Assign a private challenge.
[**assign_tenant_to_challenge**](ChallengeApi.md#assign_tenant_to_challenge) | **POST** /challenge/{challengeId}/assign-tenant/{tenantId} | Star a public challenge.
[**create_challenge**](ChallengeApi.md#create_challenge) | **POST** /challenge | Create a new challenge.
[**download_challenge**](ChallengeApi.md#download_challenge) | **GET** /challenge/{challengeId}/download/{shard} | Download tagged items from challenges
[**force_merge_tagged_media_item**](ChallengeApi.md#force_merge_tagged_media_item) | **GET** /challenge/{challengeId}/force-merge | force merge
[**get_challenge**](ChallengeApi.md#get_challenge) | **GET** /challenge/{challengeId} | Retrieve list of challenges
[**get_challenge_cost**](ChallengeApi.md#get_challenge_cost) | **POST** /challenge/cost | get estimated cost for challenge
[**get_challenge_list_broker**](ChallengeApi.md#get_challenge_list_broker) | **GET** /challenge/broker/list | Retrieve list of challenges
[**get_challenge_list_collaborator**](ChallengeApi.md#get_challenge_list_collaborator) | **GET** /challenge/collaborator/list | Retrieve list of challenges
[**get_challenge_list_supervisor**](ChallengeApi.md#get_challenge_list_supervisor) | **GET** /challenge/supervisor/list | Retrieve list of challenges
[**get_tagged_items**](ChallengeApi.md#get_tagged_items) | **GET** /challenge/{challengeId}/tagged-item/list | Retrieve list tagged media items
[**patch_challenge**](ChallengeApi.md#patch_challenge) | **PATCH** /challenge/{challengeId} | Update challenge.
[**reject_challenge**](ChallengeApi.md#reject_challenge) | **POST** /challenge/{challengeId}/reject | Star a public challenge.
[**star_challenge**](ChallengeApi.md#star_challenge) | **POST** /challenge/{challengeId}/star | Star a public challenge.
[**statistics_challenge**](ChallengeApi.md#statistics_challenge) | **GET** /challenge/{challengeId}/statistics | Get challenge statistics


# **archive_shard**
> ArchivedShard archive_shard(challenge_id, shard, force=force)

Archive shard from challenges

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | The identifier of the challenge
shard = 56 # int | The identifier of the shard
force = True # bool |  (optional)

    try:
        # Archive shard from challenges
        api_response = api_instance.archive_shard(challenge_id, shard, force=force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->archive_shard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**| The identifier of the challenge | 
 **shard** | **int**| The identifier of the shard | 
 **force** | **bool**|  | [optional] 

### Return type

[**ArchivedShard**](ArchivedShard.md)

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

# **archived_shard_list**
> list[ArchivedShard] archived_shard_list(challenge_id)

Get archive list from challenges

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | The identifier of the challenge

    try:
        # Get archive list from challenges
        api_response = api_instance.archived_shard_list(challenge_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->archived_shard_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**| The identifier of the challenge | 

### Return type

[**list[ArchivedShard]**](ArchivedShard.md)

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

# **assign_challenge**
> assign_challenge(assign_users_request)

Assign a private challenge.

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
    api_instance = openapi_client.ChallengeApi(api_client)
    assign_users_request = openapi_client.AssignUsersRequest() # AssignUsersRequest | The users to be assigned to a challenge

    try:
        # Assign a private challenge.
        api_instance.assign_challenge(assign_users_request)
    except ApiException as e:
        print("Exception when calling ChallengeApi->assign_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_users_request** | [**AssignUsersRequest**](AssignUsersRequest.md)| The users to be assigned to a challenge | 

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
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_tenant_to_challenge**
> assign_tenant_to_challenge(challenge_id, tenant_id)

Star a public challenge.

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | 
tenant_id = 'tenant_id_example' # str | 

    try:
        # Star a public challenge.
        api_instance.assign_tenant_to_challenge(challenge_id, tenant_id)
    except ApiException as e:
        print("Exception when calling ChallengeApi->assign_tenant_to_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**|  | 
 **tenant_id** | **str**|  | 

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
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_challenge**
> Challenge create_challenge(challenge)

Create a new challenge.

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge = openapi_client.Challenge() # Challenge | The challenge object to be created

    try:
        # Create a new challenge.
        api_response = api_instance.create_challenge(challenge)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->create_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge** | [**Challenge**](Challenge.md)| The challenge object to be created | 

### Return type

[**Challenge**](Challenge.md)

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

# **download_challenge**
> download_challenge(challenge_id, shard, x_auth_credential=x_auth_credential)

Download tagged items from challenges

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | The identifier of the challenge
shard = 56 # int | The identifier of the shard
x_auth_credential = 'x_auth_credential_example' # str |  (optional)

    try:
        # Download tagged items from challenges
        api_instance.download_challenge(challenge_id, shard, x_auth_credential=x_auth_credential)
    except ApiException as e:
        print("Exception when calling ChallengeApi->download_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**| The identifier of the challenge | 
 **shard** | **int**| The identifier of the shard | 
 **x_auth_credential** | **str**|  | [optional] 

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
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_merge_tagged_media_item**
> Challenge force_merge_tagged_media_item(challenge_id, challenge_name=challenge_name)

force merge

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | The identifier of the dataset
challenge_name = 'challenge_name_example' # str | The identifier of the tagged media item (optional)

    try:
        # force merge
        api_response = api_instance.force_merge_tagged_media_item(challenge_id, challenge_name=challenge_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->force_merge_tagged_media_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**| The identifier of the dataset | 
 **challenge_name** | **str**| The identifier of the tagged media item | [optional] 

### Return type

[**Challenge**](Challenge.md)

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

# **get_challenge**
> Challenge get_challenge(challenge_id, access_token=access_token)

Retrieve list of challenges

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | The identifier of the dataset
access_token = 'access_token_example' # str |  (optional)

    try:
        # Retrieve list of challenges
        api_response = api_instance.get_challenge(challenge_id, access_token=access_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->get_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**| The identifier of the dataset | 
 **access_token** | **str**|  | [optional] 

### Return type

[**Challenge**](Challenge.md)

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

# **get_challenge_cost**
> ChallengeBudgetResponse get_challenge_cost(challenge_budget_request)

get estimated cost for challenge

estimage challenge budget

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_budget_request = openapi_client.ChallengeBudgetRequest() # ChallengeBudgetRequest | The challenge options

    try:
        # get estimated cost for challenge
        api_response = api_instance.get_challenge_cost(challenge_budget_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->get_challenge_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_budget_request** | [**ChallengeBudgetRequest**](ChallengeBudgetRequest.md)| The challenge options | 

### Return type

[**ChallengeBudgetResponse**](ChallengeBudgetResponse.md)

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

# **get_challenge_list_broker**
> list[Challenge] get_challenge_list_broker(challenge_name=challenge_name, access_type=access_type, liked=liked, page_size=page_size, page_number=page_number)

Retrieve list of challenges

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_name = 'challenge_name_example' # str |  (optional)
access_type = 'access_type_example' # str |  (optional)
liked = True # bool |  (optional)
page_size = 56 # int |  (optional)
page_number = 56 # int |  (optional)

    try:
        # Retrieve list of challenges
        api_response = api_instance.get_challenge_list_broker(challenge_name=challenge_name, access_type=access_type, liked=liked, page_size=page_size, page_number=page_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->get_challenge_list_broker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_name** | **str**|  | [optional] 
 **access_type** | **str**|  | [optional] 
 **liked** | **bool**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_number** | **int**|  | [optional] 

### Return type

[**list[Challenge]**](Challenge.md)

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

# **get_challenge_list_collaborator**
> list[Challenge] get_challenge_list_collaborator(challenge_name=challenge_name, access_type=access_type, liked=liked, page_size=page_size, page_number=page_number)

Retrieve list of challenges

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_name = 'challenge_name_example' # str |  (optional)
access_type = 'access_type_example' # str |  (optional)
liked = True # bool |  (optional)
page_size = 56 # int |  (optional)
page_number = 56 # int |  (optional)

    try:
        # Retrieve list of challenges
        api_response = api_instance.get_challenge_list_collaborator(challenge_name=challenge_name, access_type=access_type, liked=liked, page_size=page_size, page_number=page_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->get_challenge_list_collaborator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_name** | **str**|  | [optional] 
 **access_type** | **str**|  | [optional] 
 **liked** | **bool**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_number** | **int**|  | [optional] 

### Return type

[**list[Challenge]**](Challenge.md)

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

# **get_challenge_list_supervisor**
> list[Challenge] get_challenge_list_supervisor(challenge_name=challenge_name, access_type=access_type, liked=liked, page_size=page_size, page_number=page_number)

Retrieve list of challenges

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_name = 'challenge_name_example' # str |  (optional)
access_type = 'access_type_example' # str |  (optional)
liked = True # bool |  (optional)
page_size = 56 # int |  (optional)
page_number = 56 # int |  (optional)

    try:
        # Retrieve list of challenges
        api_response = api_instance.get_challenge_list_supervisor(challenge_name=challenge_name, access_type=access_type, liked=liked, page_size=page_size, page_number=page_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->get_challenge_list_supervisor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_name** | **str**|  | [optional] 
 **access_type** | **str**|  | [optional] 
 **liked** | **bool**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_number** | **int**|  | [optional] 

### Return type

[**list[Challenge]**](Challenge.md)

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

# **get_tagged_items**
> list[TaggedMediaItem] get_tagged_items(challenge_id, page_size=page_size, page_number=page_number, stage=stage, access_token=access_token)

Retrieve list tagged media items

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | The identifier of the dataset
page_size = 56 # int |  (optional)
page_number = 56 # int |  (optional)
stage = 56 # int |  (optional)
access_token = 'access_token_example' # str |  (optional)

    try:
        # Retrieve list tagged media items
        api_response = api_instance.get_tagged_items(challenge_id, page_size=page_size, page_number=page_number, stage=stage, access_token=access_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->get_tagged_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**| The identifier of the dataset | 
 **page_size** | **int**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **stage** | **int**|  | [optional] 
 **access_token** | **str**|  | [optional] 

### Return type

[**list[TaggedMediaItem]**](TaggedMediaItem.md)

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

# **patch_challenge**
> Challenge patch_challenge(challenge_id, patch_challenge)

Update challenge.

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | The identifier of the dataset
patch_challenge = openapi_client.PatchChallenge() # PatchChallenge | The new challenge object

    try:
        # Update challenge.
        api_response = api_instance.patch_challenge(challenge_id, patch_challenge)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->patch_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**| The identifier of the dataset | 
 **patch_challenge** | [**PatchChallenge**](PatchChallenge.md)| The new challenge object | 

### Return type

[**Challenge**](Challenge.md)

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

# **reject_challenge**
> reject_challenge(challenge_id, body)

Star a public challenge.

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | 
body = 'body_example' # str | The challenge object to be created

    try:
        # Star a public challenge.
        api_instance.reject_challenge(challenge_id, body)
    except ApiException as e:
        print("Exception when calling ChallengeApi->reject_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**|  | 
 **body** | **str**| The challenge object to be created | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **star_challenge**
> star_challenge(challenge_id)

Star a public challenge.

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | 

    try:
        # Star a public challenge.
        api_instance.star_challenge(challenge_id)
    except ApiException as e:
        print("Exception when calling ChallengeApi->star_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**|  | 

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
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_challenge**
> ChallengeStatistics statistics_challenge(challenge_id)

Get challenge statistics

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
    api_instance = openapi_client.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | 

    try:
        # Get challenge statistics
        api_response = api_instance.statistics_challenge(challenge_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->statistics_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**|  | 

### Return type

[**ChallengeStatistics**](ChallengeStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

