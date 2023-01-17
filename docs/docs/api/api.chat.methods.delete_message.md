<!-- markdownlint-disable -->

<a href="../../../src/switch/api/chat/methods/delete_message.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.delete_message`






---

<a href="../../../src/switch/api/chat/methods/delete_message.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `DeleteMessage`







---

<a href="../../../src/switch/api/chat/methods/delete_message.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `delete_message`

```python
delete_message(self: 'ApiClient', message: int | Message) → bool
```

Delete a message 



**Parameters:**
 
 - <b>`message`</b> (``int`` | ``~switch.api.chat.models.Message``):  The message to delete 



**Returns:**
 
 - <b>```bool```</b>:  Whether the message was deleted 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be deleted 

This method does the same as :meth:`~switch.api.chat.controllers.MessageController.delete_message`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
