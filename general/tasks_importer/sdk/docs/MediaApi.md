# swagger_client.MediaApi

All URIs are relative to *http://0.0.0.0:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_medium**](MediaApi.md#create_medium) | **POST** /media | 
[**delete_medium**](MediaApi.md#delete_medium) | **DELETE** /media/source/{id} | Delete all media files related to  source
[**get_for_source**](MediaApi.md#get_for_source) | **GET** /media/source/{id} | Query media for a specific task or project
[**get_media**](MediaApi.md#get_media) | **GET** /media | 
[**get_medium**](MediaApi.md#get_medium) | **GET** /media/{id} | Get a single file
[**update_medium**](MediaApi.md#update_medium) | **PUT** /media/{id} | Put a single file
[**upload**](MediaApi.md#upload) | **POST** /media/upload | 


# **create_medium**
> create_medium(media=media)



The media details (for files already on the server or remotely hosted)

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
api_instance = swagger_client.MediaApi(swagger_client.ApiClient(configuration))
media = swagger_client.null() #  |  (optional)

try:
    api_instance.create_medium(media=media)
except ApiException as e:
    print("Exception when calling MediaApi->create_medium: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media** | [****](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_medium**
> delete_medium(id)

Delete all media files related to  source

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
api_instance = swagger_client.MediaApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)

try:
    # Delete all media files related to  source
    api_instance.delete_medium(id)
except ApiException as e:
    print("Exception when calling MediaApi->delete_medium: %s\n" % e)
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

# **get_for_source**
> list[InlineResponse2002] get_for_source(id)

Query media for a specific task or project

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
api_instance = swagger_client.MediaApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)

try:
    # Query media for a specific task or project
    api_response = api_instance.get_for_source(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_for_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

[anonUser](../README.md#anonUser), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> list[InlineResponse2002] get_media(search_term=search_term, limit=limit)



Get a list of media

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
api_instance = swagger_client.MediaApi(swagger_client.ApiClient(configuration))
search_term = 'search_term_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.get_media(search_term=search_term, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

[anonUser](../README.md#anonUser), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_medium**
> file get_medium(id)

Get a single file

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
api_instance = swagger_client.MediaApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)

try:
    # Get a single file
    api_response = api_instance.get_medium(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_medium: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 

### Return type

[**file**](file.md)

### Authorization

[anonUser](../README.md#anonUser), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_medium**
> InlineResponse2002 update_medium(id, media=media)

Put a single file

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
api_instance = swagger_client.MediaApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)
media = swagger_client.null() #  |  (optional)

try:
    # Put a single file
    api_response = api_instance.update_medium(id, media=media)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->update_medium: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 
 **media** | [****](.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> upload(attachment, id=id)



Add a new media attachment

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
api_instance = swagger_client.MediaApi(swagger_client.ApiClient(configuration))
attachment = '/path/to/file.txt' # file | The file to be uploaded
id = 'id_example' # str |  (optional)

try:
    api_instance.upload(attachment, id=id)
except ApiException as e:
    print("Exception when calling MediaApi->upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment** | **file**| The file to be uploaded | 
 **id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

