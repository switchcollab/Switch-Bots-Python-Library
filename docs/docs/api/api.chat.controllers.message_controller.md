<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.controllers.message_controller`




**Global Variables**
---------------
- **TYPE_CHECKING**
- **BASE_PATH**


---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L17"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `MessageController`
Message controller 

This controller is used to communicate with the message endpoints. 

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L24"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(client: 'ChatClient')
```








---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L354"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `clear_conversation`

```python
clear_conversation(receiver_id: int) → bool
```

Clear a conversation 



**Parameters:**
 
 - <b>`receiver_id`</b> (``int``):  The receiver id 



**Returns:**
 
 - <b>```bool```</b>:  True if the conversation was cleared 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the conversation could not be cleared 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L79"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `delete_message`

```python
delete_message(message: int | Message) → bool
```

Delete a message 



**Parameters:**
 
 - <b>`message`</b> (``int`` | ``~switch.api.chat.models.Message``):  The message id or message to delete 



**Returns:**
 
 - <b>```bool```</b>:  True if the message was deleted 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be deleted 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L99"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `delete_messages_from_user`

```python
delete_messages_from_user(recipient_id: int, user_id: int = None) → bool
```

Delete messages from a user 



**Parameters:**
 
 - <b>`recipient_id`</b> (``int``):  The recipient id 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 



**Returns:**
 
 - <b>```bool```</b>:  True if the messages were deleted 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the messages could not be deleted 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L62"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `edit_message`

```python
edit_message(message: Message) → Message
```

Edit a message 



**Parameters:**
 
 - <b>`message`</b> (``~switch.api.chat.models.Message``):  The message to edit 



**Returns:**
 
 - <b>```~switch.api.chat.models.Message```</b>:  The message 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be edited 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L389"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `flag_message`

```python
flag_message(message: Message | int) → bool
```

Flag a message 



**Parameters:**
 
 - <b>`message`</b> (``~switch.api.chat.models.Message`` | ``int``):  The message to flag 



**Returns:**
 
 - <b>```bool```</b>:  True if the message was flagged 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be flagged 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L152"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `forward_message`

```python
forward_message(
    message: Message | int,
    group_channel: Group | Channel | str = None,
    receiver_id: str = None
) → Message
```

Forward a message to a group or user 



**Parameters:**
 
 - <b>`message`</b> (``~switch.api.chat.models.Message`` | ``int``):  The message to forward 
 - <b>`group_channel`</b> (``~switch.api.chat.models.Group`` | ``~switch.api.chat.models.Channel`` | ``str``, *optional*):  The group or channel to forward to. Defaults to None. 
 - <b>`receiver_id`</b> (``str``, *optional*):  The user id to forward to. Defaults to None. 



**Returns:**
 
 - <b>```~switch.api.chat.models.Message```</b>:  The message 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be forwarded 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L256"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_channel_chat_history`

```python
get_channel_chat_history(
    channel_id: str,
    community_id: str,
    user_id: int = None,
    page_limit: int = 100,
    page_offset=0
) → GroupChatHistory
```

Get channel chat history 



**Parameters:**
 
 - <b>`channel_id`</b> (``str``):  The channel id 
 - <b>`community_id`</b> (``str``):  The community id 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 
 - <b>`page_limit`</b> (``int``, *optional*):  The page limit. Defaults to 100. 
 - <b>`page_offset`</b> (``int``, *optional*):  The page offset. Defaults to 0. 



**Returns:**
 
 - <b>```~switch.api.chat.models.ChannelChatHistory```</b>:  The channel chat history 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the channel chat history could not be retrieved 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L297"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_community_media_files`

```python
get_community_media_files(community_id: str) → List[Message]
```

Get community media files 



**Parameters:**
 
 - <b>`community_id`</b> (``str``):  The community id 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The community media files 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the community media files could not be retrieved 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L313"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_community_media_files_by_status`

```python
get_community_media_files_by_status(
    community_id: str,
    status: str
) → List[Message]
```

Get community media files by status 



**Parameters:**
 
 - <b>`community_id`</b> (``str``):  The community id 
 - <b>`status`</b> (``str``):  The status of the media files 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The community media files 





**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the community media files could not be retrieved 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L370"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_flag_messages`

```python
get_flag_messages(user_id: int = None) → List[Message]
```

Get flagged messages 



**Parameters:**
 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The flagged messages 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the flagged messages could not be retrieved 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L215"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_group_chat_history`

```python
get_group_chat_history(
    group_id: str,
    community_id: str,
    user_id: int = None,
    page_limit: int = 100,
    page_offset=0
) → GroupChatHistory
```

Get group chat history 



**Parameters:**
 
 - <b>`group_id`</b> (``str``):  The group id 
 - <b>`community_id`</b> (``str``):  The community id 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 
 - <b>`page_limit`</b> (``int``, *optional*):  The page limit. Defaults to 100. 
 - <b>`page_offset`</b> (``int``, *optional*):  The page offset. Defaults to 0. 



**Returns:**
 
 - <b>```~switch.api.chat.models.GroupChatHistory```</b>:  The group chat history 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the group chat history could not be retrieved 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L195"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_message`

```python
get_message(message: int | Message) → Message
```

Get a message by id 



**Parameters:**
 
 - <b>`message`</b> (``int`` | ``~switch.api.chat.models.Message``):  The message id or message to get 



**Returns:**
 
 - <b>```~switch.api.chat.models.Message```</b>:  The message 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be retrieved 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L27"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_messages`

```python
get_messages(user_id: int = None) → List[Message]
```

Get messages for a user 



**Parameters:**
 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The messages 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the messages could not be retrieved 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L120"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_messages_between_users`

```python
get_messages_between_users(
    recipient_id: int,
    user_id: int = None,
    page_limit: int = 100,
    page_offset: int = 0
) → List[Message]
```

Get messages between two users 



**Parameters:**
 
 - <b>`recipient_id`</b> (``int``):  The recipient id 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 
 - <b>`page_limit`</b> (``int``, *optional*):  The page limit. Defaults to 100. 
 - <b>`page_offset`</b> (``int``, *optional*):  The page offset. Defaults to 0. 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The messages 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the messages could not be retrieved 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L409"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_unread_messages_count`

```python
get_unread_messages_count(user_id: int = None) → int
```

Get unread messages 



**Parameters:**
 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 



**Returns:**
 
 - <b>```int```</b>:  The unread messages count 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L335"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_user_media_files`

```python
get_user_media_files(user_id: int = None) → List[Message]
```

Get user media files 





**Parameters:**
 
 - <b>`user_id`</b> (``int``, *optional*):  The user id. Defaults to the current user id. 



**Returns:**
 
 - <b>```List[~switch.api.chat.models.Message]```</b>:  The user media files 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the user media files could not be retrieved 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/controllers/message_controller.py#L45"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `send_message`

```python
send_message(message: Message) → Message
```

Send a message 



**Parameters:**
 
 - <b>`message`</b> (``~switch.api.chat.models.Message``):  The message to send 



**Returns:**
 
 - <b>```~switch.api.chat.models.Message```</b>:  The message 



**Raises:**
 
 - <b>```~switch.error.SwitchError```</b>:  If the message could not be sent 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
