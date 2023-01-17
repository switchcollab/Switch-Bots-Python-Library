<!-- markdownlint-disable -->

<a href="../../../src/switch/bots/handlers/event_handler.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `bots.handlers.event_handler`




**Global Variables**
---------------
- **TYPE_CHECKING**
- **VALID_COMMAND_REGEX**


---

<a href="../../../src/switch/bots/handlers/event_handler.py#L19"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `EventHandler`




<a href="../../../src/switch/bots/handlers/event_handler.py#L20"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    event_types: Optional[EventType, Collection[EventType]],
    callback: Callable[[BotContext[Event]], Coroutine[Any, Any, ~ResType]],
    filter: Optional[Filter] = None,
    **kwargs
)
```








---

<a href="../../../src/switch/bots/handlers/event_handler.py#L35"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `should_handle`

```python
should_handle(context: BotContext[Event]) → bool
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
