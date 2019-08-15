# swagger_client.CommentsApi

All URIs are relative to *http://0.0.0.0:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comment**](CommentsApi.md#create_comment) | **POST** /comments | Post a comment
[**delete_comment**](CommentsApi.md#delete_comment) | **DELETE** /comments/{id} | Remove a Comment
[**get_comment**](CommentsApi.md#get_comment) | **GET** /comments/{id} | Get a single comment
[**get_comments**](CommentsApi.md#get_comments) | **GET** /comments | Get a single comment
[**update_comment**](CommentsApi.md#update_comment) | **PUT** /comments/{id} | Modify/Create a Comment


# **create_comment**
> InlineResponse2001 create_comment(comment=comment)

Post a comment

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
api_instance = swagger_client.CommentsApi(swagger_client.ApiClient(configuration))
comment = swagger_client.null() #  |  (optional)

try:
    # Post a comment
    api_response = api_instance.create_comment(comment=comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->create_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment** | [****](.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[anonUser](../README.md#anonUser), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> delete_comment(id)

Remove a Comment

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
api_instance = swagger_client.CommentsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)

try:
    # Remove a Comment
    api_instance.delete_comment(id)
except ApiException as e:
    print("Exception when calling CommentsApi->delete_comment: %s\n" % e)
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

# **get_comment**
> InlineResponse2001 get_comment(id)

Get a single comment

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
api_instance = swagger_client.CommentsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)

try:
    # Get a single comment
    api_response = api_instance.get_comment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> list[InlineResponse2001] get_comments(search_term=search_term, limit=limit)

Get a single comment

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
api_instance = swagger_client.CommentsApi(swagger_client.ApiClient(configuration))
search_term = 'search_term_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    # Get a single comment
    api_response = api_instance.get_comments(search_term=search_term, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> update_comment(id, submission=submission)

Modify/Create a Comment

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
api_instance = swagger_client.CommentsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)
submission = swagger_client.null() #  |  (optional)

try:
    # Modify/Create a Comment
    api_instance.update_comment(id, submission=submission)
except ApiException as e:
    print("Exception when calling CommentsApi->update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 
 **submission** | [****](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

