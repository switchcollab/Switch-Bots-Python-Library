<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/handlers/unknown_command_handler.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `bots.handlers.unknown_command_handler`




**Global Variables**
---------------
- **TYPE_CHECKING**
- **VALID_COMMAND_REGEX**


---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/handlers/unknown_command_handler.py#L17"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `UnknownCommandHandler`




<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/handlers/unknown_command_handler.py#L18"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    callback: Callable[[BotContext[Any]], Coroutine[Any, Any, ~ResType]],
    filter: Optional[Filter] = None,
    **kwargs
)
```








---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/bots/handlers/unknown_command_handler.py#L26"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `should_handle`

```python
should_handle(context: BotContext[Any]) → bool
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
