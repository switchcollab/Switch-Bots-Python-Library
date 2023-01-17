<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/models/message.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.models.message`




**Global Variables**
---------------
- **TYPE_CHECKING**


---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/models/message.py#L8"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `Message`




<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/models/message.py#L9"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    id: int = None,
    user_id: int = None,
    receiver_id: int = None,
    message: str = None,
    sent_date: int = None,
    status: int = None,
    request_id: int = None,
    button_name: str = None,
    button_pressed_id: int = None,
    callback_data: str = None,
    channel_chat: bool = None,
    channel_id: int = None,
    command_name: str = None,
    community_id: int = None,
    edit: bool = None,
    flag: int = None,
    forward: bool = None,
    group_chat: bool = None,
    group_id: int = None,
    information: str = None,
    inline_markup: 'InlineMarkup' = None,
    is_read: bool = None,
    media_link: str = None,
    mentioned_ids: List[int] = None,
    personal_chat: bool = None,
    pinned: bool = None,
    reactions: List[str] = None,
    replied_message: str = None,
    replied_to: int = None,
    replies: List[ForwardRef('Message')] = None,
    reply_count: int = None,
    **kwargs
)
```








---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/models/message.py#L123"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `from_json`

```python
from_json(data: Optional[Dict[str, Any]]) → Message
```





---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/models/message.py#L88"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `to_json`

```python
to_json() → Dict[str, Any]
```





---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/models/message.py#L77"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `to_json_request`

```python
to_json_request() → Dict[str, Any]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
