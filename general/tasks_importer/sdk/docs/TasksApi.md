# swagger_client.TasksApi

All URIs are relative to *http://0.0.0.0:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tasks**](TasksApi.md#create_tasks) | **POST** /tasks | Post an array of tasks
[**delete_task**](TasksApi.md#delete_task) | **DELETE** /tasks/{id} | Delete a single tasks
[**delete_tasks**](TasksApi.md#delete_tasks) | **DELETE** /tasks | Delete an array of tasks
[**get_task**](TasksApi.md#get_task) | **GET** /tasks/{id} | Get a single task
[**get_task_count**](TasksApi.md#get_task_count) | **GET** /tasks/count | Get row count of query
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /tasks | Get a list of tasks
[**update_task**](TasksApi.md#update_task) | **PUT** /tasks/{id} | Modify/Create a task


# **create_tasks**
> InlineResponse2005 create_tasks(tasks=tasks)

Post an array of tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
tasks = [swagger_client.InlineResponse2005()] # list[InlineResponse2005] |  (optional)

try:
    # Post an array of tasks
    api_response = api_instance.create_tasks(tasks=tasks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tasks** | [**list[InlineResponse2005]**](InlineResponse2005.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> delete_task(id)

Delete a single tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)

try:
    # Delete a single tasks
    api_instance.delete_task(id)
except ApiException as e:
    print("Exception when calling TasksApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tasks**
> delete_tasks(tasks=tasks)

Delete an array of tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
tasks = [swagger_client.list[str]()] # list[str] |  (optional)

try:
    # Delete an array of tasks
    api_instance.delete_tasks(tasks=tasks)
except ApiException as e:
    print("Exception when calling TasksApi->delete_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tasks** | **list[str]**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> InlineResponse2005 get_task(id)

Get a single task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: anonUser
configuration = swagger_client.Configuration()
configuration.api_key['X-ANON'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-ANON'] = 'Bearer'
# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)

try:
    # Get a single task
    api_response = api_instance.get_task(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[anonUser](../README.md#anonUser), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_count**
> get_task_count(search_term=search_term)

Get row count of query

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
search_term = 'search_term_example' # str |  (optional)

try:
    # Get row count of query
    api_instance.get_task_count(search_term=search_term)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> list[InlineResponse2005] get_tasks(offset=offset, search_term=search_term, limit=limit)

Get a list of tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: anonUser
configuration = swagger_client.Configuration()
configuration.api_key['X-ANON'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-ANON'] = 'Bearer'
# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
offset = 0 # float |  (optional) (default to 0)
search_term = 'search_term_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    # Get a list of tasks
    api_response = api_instance.get_tasks(offset=offset, search_term=search_term, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**|  | [optional] [default to 0]
 **search_term** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**list[InlineResponse2005]**](InlineResponse2005.md)

### Authorization

[anonUser](../README.md#anonUser), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> update_task(id, task=task)

Modify/Create a task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)
task = swagger_client.null() #  |  (optional)

try:
    # Modify/Create a task
    api_instance.update_task(id, task=task)
except ApiException as e:
    print("Exception when calling TasksApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 
 **task** | [****](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

