<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/handlers/base_handler.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `bots.handlers.base_handler`




**Global Variables**
---------------
- **TYPE_CHECKING**


---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/handlers/base_handler.py#L15"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `BaseHandler`




<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/handlers/base_handler.py#L16"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    callback: Callable[[~CtxType], Coroutine[Any, Any, ~ResType]],
    filter: Optional[Filter] = None,
    **kwargs
)
```








---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/handlers/base_handler.py#L34"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `handle`

```python
handle(context: ~CtxType) → ~ResType
```





---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/handlers/base_handler.py#L25"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `on_app_start`

```python
on_app_start(app: 'SwitchApp')
```





---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/handlers/base_handler.py#L28"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `on_app_stop`

```python
on_app_stop(app: 'SwitchApp')
```





---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/handlers/base_handler.py#L31"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `should_handle`

```python
should_handle(context: ~CtxType) → bool
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
