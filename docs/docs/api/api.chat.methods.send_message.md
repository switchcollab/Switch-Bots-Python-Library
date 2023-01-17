<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/send_message.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.send_message`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/send_message.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `SendMessage`







---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/send_message.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `send_message`

```python
send_message(self: 'ApiClient', message: Message) → Message
```

Send a message 



**Parameters:**
 
 - <b>`message`</b> (``~switch.api.chat.models.Message``):  The message to send 



**Returns:**
 
 - <b>```~switch.api.chat.models.Message```</b>:  The message 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be sent 

This functions does the same as :meth:`~switch.api.chat.controllers.MessageController.send_message`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
