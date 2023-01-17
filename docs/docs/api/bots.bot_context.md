<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/bot_context.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `bots.bot_context`




**Global Variables**
---------------
- **TYPE_CHECKING**


---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/bot_context.py#L10"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `BotContext`




<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/bot_context.py#L11"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(bot: 'Bot', event: ~EventType)
```






---

#### <kbd>property</kbd> auth_service

Get the auth client 

---

#### <kbd>property</kbd> bots_service

Get the bot client 

---

#### <kbd>property</kbd> chat_service

Get the chat client 

---

#### <kbd>property</kbd> community_service

Get the community client 

---

#### <kbd>property</kbd> token

Get the token 

---

#### <kbd>property</kbd> user







---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/bot_context.py#L20"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `prepare_message`

```python
prepare_message(receiver_id: int, text: str, **kwargs) → Message
```

Prepares a message to be sent to the given receiver. 



**Parameters:**
 
 - <b>`receiver_id`</b> (:obj:`int`):  The receiver's id. 
 - <b>`text`</b> (:obj:`str`):  The message's text. 
 - <b>`**kwargs`</b>:  Additional keyword arguments to pass to the message constructor. 



**Returns:**
 
 - <b>`:obj`</b>: `switch.api.chat.models.Message`: The prepared message. 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/bot_context.py#L34"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `prepare_response_message`

```python
prepare_response_message(message: Message) → Message
```

Prepares a message to be sent as a response to the given message. 



**Parameters:**
 
 - <b>`message`</b> (:obj:`switch.api.chat.models.Message`):  The message to respond to. 



**Returns:**
 
 - <b>`:obj`</b>: `switch.api.chat.models.Message`: The prepared message. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
