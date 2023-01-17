<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/controllers/user_controller.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.auth.controllers.user_controller`




**Global Variables**
---------------
- **TYPE_CHECKING**
- **BASE_PATH**


---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/controllers/user_controller.py#L15"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `UserController`
User controller 

This controller is used to communicate with the user endpoints. 

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/controllers/user_controller.py#L22"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(client: 'AuthClient')
```








---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/controllers/user_controller.py#L25"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `me`

```python
me(user_type: Type[~T] = <class 'api.auth.models.auth_user.AuthUser'>) → ~T
```

Get the current user 



**Parameters:**
 
 - <b>`user_type`</b> (``Type[T]``, *optional*):  The user type to return. Defaults to :obj:`~switch.api.auth.models.AuthUser`. 



**Returns:**
 
 - <b>```T```</b>:  The current user 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
