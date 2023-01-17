<!-- markdownlint-disable -->

<a href="../../../src/switch/api/chat/events/chat_event.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.events.chat_event`






---

<a href="../../../src/switch/api/chat/events/chat_event.py#L12"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `ChatEvent`




<a href="../../../src/switch/api/chat/events/chat_event.py#L13"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

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
    user: Optional[User] = None,
    message: Optional[Message] = None,
    message_id: Optional[str] = None
)
```








---

<a href="../../../src/switch/api/chat/events/chat_event.py#L58"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `from_json`

```python
from_json(data: Dict[str, Any]) → ChatEvent
```





---

<a href="../../../src/switch/api/chat/events/chat_event.py#L47"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `to_json`

```python
to_json() → Dict[str, Any]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
