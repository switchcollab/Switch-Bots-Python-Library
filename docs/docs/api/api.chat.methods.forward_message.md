<!-- markdownlint-disable -->

<a href="../../../src/switch/api/chat/methods/forward_message.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.methods.forward_message`






---

<a href="../../../src/switch/api/chat/methods/forward_message.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `ForwardMessage`







---

<a href="../../../src/switch/api/chat/methods/forward_message.py#L8"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `forward_message`

```python
forward_message(
    self: 'ApiClient',
    message: Message | int,
    group_channel: Group | Channel | str = None,
    receiver_id: str = None
) → Message
```

Forward a message 



**Parameters:**
 
 - <b>`message`</b> (``~switch.api.chat.models.Message`` | ``int``):  The message to forward 
 - <b>`group_channel`</b> (``~switch.api.community.models.Group`` | ``~switch.api.community.models.Channel`` | ``str``):  The group/channel to forward the message to 
 - <b>`receiver_id`</b> (``str``):  The receiver id to forward the message to 



**Returns:**
 
 - <b>```~switch.api.chat.models.Message```</b>:  The forwarded message 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be forwarded 

This functions does the same as :meth:`~switch.api.chat.controllers.MessageController.forward_message`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
