# swagger_client.UsersApi

All URIs are relative to *http://0.0.0.0:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users/register | Registration end point for a user account
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{id} | Delete user (only allowed by the user themselves)
[**generate**](UsersApi.md#generate) | **POST** /users/authorize | Post auth for token response
[**get_subs**](UsersApi.md#get_subs) | **GET** /users/{id}/submissions | Get all submissions for a user (or those matching an ID)
[**get_user**](UsersApi.md#get_user) | **GET** /users/{id} | Get all users (or those matching an ID)
[**get_users**](UsersApi.md#get_users) | **GET** /users | 
[**login**](UsersApi.md#login) | **POST** /users/login | Allow a user to login
[**reset**](UsersApi.md#reset) | **GET** /users/reset | Reset user password
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{id} | Update user details (change password, add details etc)
[**validate**](UsersApi.md#validate) | **GET** /users/validate | OAuth2 token info
[**verify_reset**](UsersApi.md#verify_reset) | **POST** /users/reset | Verify password reset token


# **create_user**
> create_user(user=user)

Registration end point for a user account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user = swagger_client.null() #  |  (optional)

try:
    # Registration end point for a user account
    api_instance.create_user(user=user)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [****](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(id)

Delete user (only allowed by the user themselves)

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)

try:
    # Delete user (only allowed by the user themselves)
    api_instance.delete_user(id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 

### Return type

void (empty response body)

### Authorization

[anonUser](../README.md#anonUser), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate**
> generate(token=token)

Post auth for token response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
token = swagger_client.null() #  |  (optional)

try:
    # Post auth for token response
    api_instance.generate(token=token)
except ApiException as e:
    print("Exception when calling UsersApi->generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [****](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subs**
> list[InlineResponse2004] get_subs(id)

Get all submissions for a user (or those matching an ID)

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)

try:
    # Get all submissions for a user (or those matching an ID)
    api_response = api_instance.get_subs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_subs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 

### Return type

[**list[InlineResponse2004]**](InlineResponse2004.md)

### Authorization

[anonUser](../README.md#anonUser), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> object get_user(id)

Get all users (or those matching an ID)

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)

try:
    # Get all users (or those matching an ID)
    api_response = api_instance.get_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 

### Return type

**object**

### Authorization

[anonUser](../README.md#anonUser), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[object] get_users(search_term=search_term, limit=limit)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
search_term = 'search_term_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.get_users(search_term=search_term, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

**list[object]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> login(user)

Allow a user to login

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user = swagger_client.null() #  | 

try:
    # Allow a user to login
    api_instance.login(user)
except ApiException as e:
    print("Exception when calling UsersApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [****](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset**
> reset(email)

Reset user password

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
email = 'email_example' # str | 

try:
    # Reset user password
    api_instance.reset(email)
except ApiException as e:
    print("Exception when calling UsersApi->reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> object update_user(id, user=user)

Update user details (change password, add details etc)

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifer for an Object (i.e. User, Task, Project, Submission etc)
user = swagger_client.null() #  |  (optional)

try:
    # Update user details (change password, add details etc)
    api_response = api_instance.update_user(id, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifer for an Object (i.e. User, Task, Project, Submission etc) | 
 **user** | [****](.md)|  | [optional] 

### Return type

**object**

### Authorization

[anonUser](../README.md#anonUser), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate**
> object validate(key=key)

OAuth2 token info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
key = 'key_example' # str |  (optional)

try:
    # OAuth2 token info
    api_response = api_instance.validate(key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_reset**
> verify_reset(reset=reset)

Verify password reset token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
reset = swagger_client.Reset() # Reset |  (optional)

try:
    # Verify password reset token
    api_instance.verify_reset(reset=reset)
except ApiException as e:
    print("Exception when calling UsersApi->verify_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset** | [**Reset**](Reset.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

