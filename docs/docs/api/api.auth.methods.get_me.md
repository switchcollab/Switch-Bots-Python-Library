<!-- markdownlint-disable -->

<a href="../../../src/switch/api/auth/methods/get_me.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.auth.methods.get_me`






---

<a href="../../../src/switch/api/auth/methods/get_me.py#L8"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `GetMe`







---

<a href="../../../src/switch/api/auth/methods/get_me.py#L9"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_me`

```python
get_me(
    self: 'ApiClient',
    user_type: Type[~T] = <class 'switch.api.auth.models.auth_user.AuthUser'>
) → ~T
```

Get the current user 



**Parameters:**
 
 - <b>`user_type`</b> (``Type[T]``, *optional*):  The user type to return. Defaults to :obj:`~switch.api.auth.models.AuthUser`. 



**Returns:**
 
 - <b>```T```</b>:  The current user 

This functions does the same as :meth:`~switch.api.auth.controllers.UserController.me`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
