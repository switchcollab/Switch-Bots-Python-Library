<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_message.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.get_message`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_message.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `GetMessage`







---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/get_message.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_message`

```python
get_message(self: 'ApiClient', message_id: int) → Message
```

Get a message 



**Parameters:**
 
 - <b>`message_id`</b> (``int``):  The message id 



**Returns:**
 
 - <b>```~switch.api.chat.models.Message```</b>:  The message 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be retrieved 

This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_message`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
