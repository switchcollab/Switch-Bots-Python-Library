<!-- markdownlint-disable -->

<a href="../../../src/switch/api/chat/methods/get_messages_between_users.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.get_messages_between_users`






---

<a href="../../../src/switch/api/chat/methods/get_messages_between_users.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `GetMessagesBetweenUsers`







---

<a href="../../../src/switch/api/chat/methods/get_messages_between_users.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_messages_between_users`

```python
get_messages_between_users(
    self: 'ApiClient',
    user_id: int,
    other_user_id: int,
    limit: int = 100,
    offset: int = 0
) → List[Message]
```

Get messages between users 



**Parameters:**
 
 - <b>`user_id`</b> (``int``):  The user id 
 - <b>`other_user_id`</b> (``int``):  The other user id 
 - <b>`limit`</b> (``int``, *optional*):  The maximum number of messages to retrieve. Defaults to 100. 
 - <b>`offset`</b> (``int``, *optional*):  The offset. Defaults to 0. 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The messages 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the messages could not be retrieved 

This function does the same as :meth:`~switch.api.chat.controllers.MessageController.get_messages_between_users`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
