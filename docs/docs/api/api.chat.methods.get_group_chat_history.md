<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_group_chat_history.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.get_group_chat_history`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_group_chat_history.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `GetGroupChatHistory`







---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_group_chat_history.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_group_chat_history`

```python
get_group_chat_history(
    self: 'ApiClient',
    group_id: str,
    community_id: str,
    user_id: int = None,
    page_limit: int = 100,
    page_offset=0
) → GroupChatHistory
```

Get group chat history 



**Parameters:**
 
 - <b>`group_id`</b> (``int``):  The group id 
 - <b>`limit`</b> (``int``, *optional*):  The maximum number of messages to return. Defaults to 100. 
 - <b>`offset`</b> (``int``, *optional*):  The offset. Defaults to 0. 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The messages 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the messages could not be retrieved 

This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_group_chat_history`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
