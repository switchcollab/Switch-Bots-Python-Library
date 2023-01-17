<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_flag_messages.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.get_flag_messages`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_flag_messages.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `GetFlagMessages`







---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_flag_messages.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_flag_messages`

```python
get_flag_messages(self: 'ApiClient', user_id: int = None) → List[Message]
```

Get flagged messages 



**Parameters:**
 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The flagged messages 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the flagged messages could not be retrieved 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
