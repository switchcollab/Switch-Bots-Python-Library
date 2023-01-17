<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/models/auth_user.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.auth.models.auth_user`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/models/auth_user.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `AuthUser`




<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/models/auth_user.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    id: Optional[int] = None,
    user_name: Optional[str] = None,
    name: Optional[str] = None,
    creator_name: Optional[str] = None,
    verify_email: Optional[bool] = None,
    privacy: Optional[str] = None,
    is_bot: Optional[bool] = None,
    bot_privacy: Optional[str] = None,
    profile_colour: Optional[str] = None,
    otp: Optional[str] = None,
    otp_expiry: Optional[str] = None,
    bio: Optional[str] = None,
    imageurl: Optional[str] = None,
    private_imageurl: Optional[str] = None,
    gender: Optional[str] = None,
    date_of_birth: Optional[str] = None,
    media1: Optional[str] = None,
    media2: Optional[str] = None,
    media3: Optional[str] = None,
    media4: Optional[str] = None,
    media5: Optional[str] = None,
    more_about_this: Optional[str] = None,
    active: Optional[bool] = None,
    parent_id: Optional[int] = None,
    created_at: Optional[str] = None,
    updated_at: Optional[str] = None
)
```








---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/models/auth_user.py#L63"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `from_json`

```python
from_json(data: Optional[Dict[str, Any]]) → AuthUser
```





---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/auth/models/auth_user.py#L95"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `to_json`

```python
to_json() → Dict[str, Any]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
