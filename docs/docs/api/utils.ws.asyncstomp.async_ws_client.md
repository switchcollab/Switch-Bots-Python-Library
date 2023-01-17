<!-- markdownlint-disable -->

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_client.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `utils.ws.asyncstomp.async_ws_client`




**Global Variables**
---------------
- **VERSIONS**


---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_client.py#L14"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `AsyncWsClient`




<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_client.py#L15"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_client.py#L272"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `ack`

```python
ack(message_id, subscription, headers)
```





---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_client.py#L144"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

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

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_client.py#L218"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `disconnect`

```python
disconnect(disconnectCallback=None, headers=None)
```





---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_client.py#L278"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `nack`

```python
nack(message_id, subscription, headers)
```





---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_client.py#L208"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `read_messages`

```python
read_messages()
```





---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_client.py#L240"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `send`

```python
send(destination, headers=None, body=None)
```





---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_client.py#L247"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `subscribe`

```python
subscribe(destination, callback=None, headers=None)
```





---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_client.py#L268"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `unsubscribe`

```python
unsubscribe(id)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
