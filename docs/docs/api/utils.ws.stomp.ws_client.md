<!-- markdownlint-disable -->

<a href="../../../src/switch/utils/ws/stomp/ws_client.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `utils.ws.stomp.ws_client`




**Global Variables**
---------------
- **VERSIONS**


---

<a href="../../../src/switch/utils/ws/stomp/ws_client.py#L12"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `WsClient`




<a href="../../../src/switch/utils/ws/stomp/ws_client.py#L14"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="../../../src/switch/utils/ws/stomp/ws_client.py#L203"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `ack`

```python
ack(message_id, subscription, headers)
```





---

<a href="../../../src/switch/utils/ws/stomp/ws_client.py#L133"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `connect`

```python
connect(
    login=None,
    passcode=None,
    headers=None,
    connectCallback=None,
    errorCallback=None,
    timeout=0,
    **kwargs
)
```





---

<a href="../../../src/switch/utils/ws/stomp/ws_client.py#L156"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `disconnect`

```python
disconnect(disconnectCallback=None, headers=None)
```





---

<a href="../../../src/switch/utils/ws/stomp/ws_client.py#L210"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `nack`

```python
nack(message_id, subscription, headers)
```





---

<a href="../../../src/switch/utils/ws/stomp/ws_client.py#L171"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `send`

```python
send(destination, headers=None, body=None)
```





---

<a href="../../../src/switch/utils/ws/stomp/ws_client.py#L53"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `start_heartbeat`

```python
start_heartbeat()
```





---

<a href="../../../src/switch/utils/ws/stomp/ws_client.py#L179"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `subscribe`

```python
subscribe(destination, callback=None, headers=None)
```





---

<a href="../../../src/switch/utils/ws/stomp/ws_client.py#L197"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `unsubscribe`

```python
unsubscribe(id)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
