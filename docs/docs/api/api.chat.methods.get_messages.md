<!-- markdownlint-disable -->

<a href="../../../src/switch/api/chat/methods/get_messages.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.get_messages`






---

<a href="../../../src/switch/api/chat/methods/get_messages.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `GetMessages`







---

<a href="../../../src/switch/api/chat/methods/get_messages.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_messages`

```python
get_messages(self: 'ApiClient', user_id: int = None) → List[Message]
```

Get messages 



**Parameters:**
 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The messages 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the messages could not be retrieved 

This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_messages`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
