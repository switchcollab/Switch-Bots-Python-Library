<!-- markdownlint-disable -->

<a href="../../../src/switch/api/chat/models/inline_markup.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.chat.models.inline_markup`




**Global Variables**
---------------
- **TYPE_CHECKING**


---

<a href="../../../src/switch/api/chat/models/inline_markup.py#L10"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `InlineMarkup`




<a href="../../../src/switch/api/chat/models/inline_markup.py#L11"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(inline_keyboard: List[List[ForwardRef('InlineKeyboardButton')]] = None)
```






---

#### <kbd>property</kbd> inline_keyboard







---

<a href="../../../src/switch/api/chat/models/inline_markup.py#L23"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `add_row`

```python
add_row(buttons: List[ForwardRef('InlineKeyboardButton')])
```





---

<a href="../../../src/switch/api/chat/models/inline_markup.py#L34"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `from_json`

```python
from_json(data: Dict[str, Any]) → InlineMarkup
```





---

<a href="../../../src/switch/api/chat/models/inline_markup.py#L27"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `to_json`

```python
to_json() → Dict[str, Any]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
