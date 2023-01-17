<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/community/models/channel.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.community.models.channel`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/community/models/channel.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `Channel`




<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/community/models/channel.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    id: Optional[str] = None,
    name: Optional[str] = None,
    community_id: Optional[str] = None,
    enabled_free: Optional[bool] = None,
    enabled_public: Optional[bool] = None,
    default_channel: Optional[bool] = None,
    is_public: Optional[bool] = None,
    created_by: Optional[str] = None,
    icon: Optional[str] = None,
    channel_logo_url: Optional[str] = None,
    allowed_content: Optional[str] = None,
    created_at: Optional[str] = None,
    updated_at: Optional[str] = None
)
```








---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/community/models/channel.py#L54"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `from_json`

```python
from_json(data: Dict[str, Any]) → Channel
```





---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/community/models/channel.py#L37"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `to_json`

```python
to_json() → Dict[str, Any]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
