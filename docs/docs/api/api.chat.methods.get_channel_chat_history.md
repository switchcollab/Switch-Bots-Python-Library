<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_channel_chat_history.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.get_channel_chat_history`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_channel_chat_history.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `GetChannelChatHistory`







---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_channel_chat_history.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_channel_chat_history`

```python
get_channel_chat_history(
    self: 'ApiClient',
    channel_id: str,
    community_id: str,
    user_id: int = None,
    page_limit: int = 100,
    page_offset=0
) → GroupChatHistory
```

Get channel chat history 





**Parameters:**
 
 - <b>`channel_id`</b> (``int``):  The channel id 
 - <b>`limit`</b> (``int``, *optional*):  The maximum number of messages to return. Defaults to 100. 
 - <b>`offset`</b> (``int``, *optional*):  The offset. Defaults to 0. 
 - <b>`community_id`</b> (``int``):  The community id 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.GroupChatHistory]```</b>:  The messages 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the messages could not be retrieved 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
