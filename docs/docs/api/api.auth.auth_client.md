<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/auth_client.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.auth.auth_client`




**Global Variables**
---------------
- **APP_CONFIG**


---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/auth_client.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `AuthClient`
Auth client 

This client is used to communicate with the auth service. 

Controllers: 
    - :attr:`users`: :obj:`~switch.api.auth.controllers.UserController` : The users controller 

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/auth_client.py#L15"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(base_url: str = 'http://51.159.11.53:9999/api')
```






---

#### <kbd>property</kbd> base_url





---

#### <kbd>property</kbd> token





---

#### <kbd>property</kbd> users

Get the users controller 



**Returns:**
 
 - <b>`:obj`</b>: `~switch.api.auth.controllers.UserController`: The users controller 



---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/auth_client.py#L31"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `prepare_request_headers`

```python
prepare_request_headers(headers: dict) → dict
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
