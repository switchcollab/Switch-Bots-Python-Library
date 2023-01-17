<!-- markdownlint-disable -->

<a href="../../../src/switch/api/chat/methods/flag_message.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.flag_message`






---

<a href="../../../src/switch/api/chat/methods/flag_message.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `FlagMessage`







---

<a href="../../../src/switch/api/chat/methods/flag_message.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `flag_message`

```python
flag_message(self: 'ApiClient', message: Message | int) → bool
```

Flag a message 



**Parameters:**
 
 - <b>`message`</b> (``~switch.api.chat.models.Message`` | ``int``):  The message to flag 



**Returns:**
 
 - <b>```bool```</b>:  True if the message was flagged 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be flagged 

This method does the same as :meth:`~switch.api.chat.controllers.MessageController.flag_message`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
