<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/events/command_event.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.events.command_event`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/events/command_event.py#L13"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `CommandEvent`
Message event 

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/events/command_event.py#L16"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

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
    command: Optional[str] = None,
    params: Optional[str] = None
)
```








---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/events/command_event.py#L52"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `from_json`

```python
from_json(data: Dict[str, Any]) → CommandEvent
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
