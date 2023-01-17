<!-- markdownlint-disable -->

<a href="../../../src/switch/api/bot/methods/get_bot_info.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.bot.methods.get_bot_info`






---

<a href="../../../src/switch/api/bot/methods/get_bot_info.py#L6"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `GetBotInfo`







---

<a href="../../../src/switch/api/bot/methods/get_bot_info.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_bot_info`

```python
get_bot_info(self: 'ApiClient', bot_id: str) → BotInfo
```

Get bot info 



**Parameters:**
 
 - <b>`bot_id`</b> (``str``):  The bot id. Defaults to the current bot id. 



**Returns:**
 
 - <b>`:obj`</b>: ``~switch.api.bot.models.BotInfo``: The bot info 

This functions does the same as :meth:`~switch.api.bot.controllers.BotController.get_bot_info`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
