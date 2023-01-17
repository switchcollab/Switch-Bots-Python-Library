<!-- markdownlint-disable -->

<a href="../../../src/switch/api/community/events/community_event.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.community.events.community_event`






---

<a href="../../../src/switch/api/community/events/community_event.py#L13"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `CommunityEvent`




<a href="../../../src/switch/api/community/events/community_event.py#L14"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    type: Optional[EventType] = None,
    community_id: Optional[str] = None,
    community: Optional[Community] = None,
    group_id: Optional[str] = None,
    group: Optional[Group] = None,
    channel_id: Optional[str] = None,
    channel: Optional[Channel] = None,
    action_by_id: Optional[str] = None,
    action_by: Optional[User] = None,
    data: Optional[dict] = None,
    user_id: Optional[str] = None,
    user: Optional[User] = None
)
```








---

<a href="../../../src/switch/api/community/events/community_event.py#L59"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `from_json`

```python
from_json(data: Dict[str, Any]) → ~T
```





---

<a href="../../../src/switch/api/community/events/community_event.py#L42"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `to_json`

```python
to_json() → Dict[str, Any]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
