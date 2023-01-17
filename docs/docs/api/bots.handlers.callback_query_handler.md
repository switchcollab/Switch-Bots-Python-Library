<!-- markdownlint-disable -->

<a href="../../../src/switch/bots/handlers/callback_query_handler.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `bots.handlers.callback_query_handler`




**Global Variables**
---------------
- **TYPE_CHECKING**


---

<a href="../../../src/switch/bots/handlers/callback_query_handler.py#L17"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `CallbackQueryHandler`




<a href="../../../src/switch/bots/handlers/callback_query_handler.py#L18"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    callback: Callable[[BotContext[CallbackQueryEvent]], Coroutine[Any, Any, ~ResType]],
    filter: Optional[Filter] = None,
    **kwargs
)
```








---

<a href="../../../src/switch/bots/handlers/callback_query_handler.py#L26"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `should_handle`

```python
should_handle(context: BotContext[CallbackQueryEvent]) → bool
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
