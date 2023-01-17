<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/edit_message.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.edit_message`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/edit_message.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `EditMessage`







---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/edit_message.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `edit_message`

```python
edit_message(self: 'ApiClient', message: Message) → Message
```

Edit a message 



**Parameters:**
 
 - <b>`message`</b> (``~switch.api.chat.models.Message``):  The message to edit 



**Returns:**
 
 - <b>```~switch.api.chat.models.Message```</b>:  The message 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be edited 

This method does the same as :meth:`~switch.api.chat.controllers.MessageController.edit_message`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
