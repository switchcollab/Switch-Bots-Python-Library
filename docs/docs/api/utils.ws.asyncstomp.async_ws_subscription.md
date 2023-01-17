<!-- markdownlint-disable -->

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_subscription.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `utils.ws.asyncstomp.async_ws_subscription`






---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_subscription.py#L4"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `AsyncWsSubscription`




<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_subscription.py#L5"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    client,
    destination: str,
    id: str,
    headers: dict[str, str] = None,
    callback=None
)
```








---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_subscription.py#L18"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `receive`

```python
receive(message)
```





---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_subscription.py#L22"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `send`

```python
send(body: str, headers: dict[str, str] = None)
```





---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_subscription.py#L13"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `start`

```python
start()
```





---

<a href="../../../src/switch/utils/ws/asyncstomp/async_ws_subscription.py#L26"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `unsubscribe`

```python
unsubscribe()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
