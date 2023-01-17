<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/clear_conversation.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.clear_conversation`






---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/clear_conversation.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `ClearConversation`







---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/methods/clear_conversation.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `clear_conversation`

```python
clear_conversation(self: 'ApiClient', receiver_id: int) → bool
```

Clear a conversation 



**Parameters:**
 
 - <b>`receiver_id`</b> (``int``):  The receiver id 



**Returns:**
 
 - <b>```bool```</b>:  True if the conversation was cleared 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the conversation could not be cleared 

This method does the same as :meth:`~switch.api.chat.controllers.MessageController.clear_conversation`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
