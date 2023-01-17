<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/chat_client.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.chat_client`




**Global Variables**
---------------
- **APP_CONFIG**


---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/chat_client.py#L14"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `ChatClient`
Chat client 

This client is used to communicate with the chat service. 

Controllers: 
    - :attr:`messages`: :obj:`~switch.api.chat.controllers.MessageController` : The message controller 

Properties: 
    - :attr:`user`: :obj:`~switch.api.auth.models.auth_user.AuthUser` : The current user 
    - :attr:`ws`: :obj:`~switch.base.SwitchWSAsyncClient` : The websocket client 

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/chat_client.py#L28"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    base_url: str = 'http://51.159.11.53:9999',
    ws_url: str = 'ws://51.159.11.53:9999/v1/websocket/message/ws'
)
```

Initialize the chat client 



**Parameters:**
 
 - <b>`base_url`</b> (``str``):  The base url of the chat service. Defaults to the value in the config. 
 - <b>`ws_url`</b> (``str``):  The websocket url of the chat service. Defaults to the value in the config. 


---

#### <kbd>property</kbd> base_url





---

#### <kbd>property</kbd> messages

Get the message controller 

---

#### <kbd>property</kbd> token





---

#### <kbd>property</kbd> user





---

#### <kbd>property</kbd> ws







---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/chat_client.py#L122"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `start`

```python
start()
```

Start the chat websocket client 

**Raises:**
 
 - <b>`:obj`</b>: `~switch.error.SwitchError`: If the user is not set 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/chat_client.py#L132"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `stop`

```python
stop()
```

Stop the chat websocket client 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/chat_client.py#L69"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `subscribe`

```python
subscribe(endpoint: str, callback=None) → AsyncWsSubscription
```

Subscribe to a websocket endpoint 



**Parameters:**
 
 - <b>`endpoint`</b> (``str``):  The endpoint to subscribe to 
 - <b>`callback`</b> (``callable``):  The callback to call when a message is received 



**Returns:**
 
 - <b>`:obj`</b>: `~switch.utils.ws.asyncstomp.async_ws_subscription.AsyncWsSubscription`: The subscription 



**Raises:**
 
 - <b>`:obj`</b>: `~switch.error.SwitchError`: If the user is not set or the callback is not set 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/chat/chat_client.py#L88"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `subscribe_to_notifications`

```python
subscribe_to_notifications(callback=None) → AsyncWsSubscription
```

Subscribe to the notification endpoint 



**Parameters:**
 
 - <b>`callback`</b> (``callable``):  The callback to call when a message is received 



**Returns:**
 
 - <b>`:obj`</b>: `~switch.utils.ws.asyncstomp.async_ws_subscription.AsyncWsSubscription`: The subscription 



**Raises:**
 
 - <b>`:obj`</b>: `~switch.error.SwitchError`: If the user is not set or the callback is not set 

This is a shortcut for :meth:`subscribe` with the endpoint set to ``/chat/queue/events`` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
