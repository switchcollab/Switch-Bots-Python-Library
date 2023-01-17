<!-- markdownlint-disable -->

<a href="../../../src/switch/api/chat/methods/delete_messages_from_user.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.delete_messages_from_user`






---

<a href="../../../src/switch/api/chat/methods/delete_messages_from_user.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `DeleteMessagesFromUser`







---

<a href="../../../src/switch/api/chat/methods/delete_messages_from_user.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `delete_messages_from_user`

```python
delete_messages_from_user(self: 'ApiClient', user_id: int) → bool
```

Delete all messages from a user 



**Parameters:**
 
 - <b>`user_id`</b> (``int``):  The user id 



**Returns:**
 
 - <b>```bool```</b>:  Whether the messages were deleted 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the messages could not be deleted 

This method does the same as :meth:`~switch.api.chat.controllers.MessageController.delete_messages_from_user`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
