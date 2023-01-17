<!-- markdownlint-disable -->

<a href="../../../src/switch/api/common/models/user.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.common.models.user`






---

<a href="../../../src/switch/api/common/models/user.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `User`




<a href="../../../src/switch/api/common/models/user.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    id: Optional[str] = None,
    name: Optional[str] = None,
    username: Optional[str] = None,
    image_url: Optional[str] = None,
    active: Optional[bool] = None,
    deleted: Optional[bool] = None,
    role_info: Optional[str] = None,
    admin: Optional[bool] = None,
    is_bot: Optional[bool] = None
)
```








---

<a href="../../../src/switch/api/common/models/user.py#L42"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `from_json`

```python
from_json(data: Optional[Dict[str, Any]] = None) → User
```





---

<a href="../../../src/switch/api/common/models/user.py#L29"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `to_json`

```python
to_json() → Dict[str, Any]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
