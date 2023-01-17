<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/bot/controllers/bot_controller.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.bot.controllers.bot_controller`




**Global Variables**
---------------
- **TYPE_CHECKING**
- **BASE_PATH**


---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/bot/controllers/bot_controller.py#L16"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `BotController`
Bot controller 

This controller is used to communicate with the bot endpoints. 

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/bot/controllers/bot_controller.py#L22"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(client: 'BotClient')
```








---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/bot/controllers/bot_controller.py#L52"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `delete_bot_info`

```python
delete_bot_info(bot_id: str) → bool
```

Delete bot info 



**Parameters:**
 
 - <b>`bot_id`</b> (``str``):  The bot id. Defaults to the current bot id. 



**Returns:**
 
 - <b>```bool```</b>:  True if the bot was deleted 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/bot/controllers/bot_controller.py#L25"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `get_bot_info`

```python
get_bot_info(bot_id: str) → BotInfo
```

Get bot info 



**Parameters:**
 
 - <b>`bot_id`</b> (``str``):  The bot id. Defaults to the current bot id. 



**Returns:**
 
 - <b>`:obj`</b>: ``~switch.api.bot.models.BotInfo``: The bot info 

---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/bot/controllers/bot_controller.py#L39"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `update_bot_info`

```python
update_bot_info(bot_info: BotInfo) → BotInfo
```

Update bot info 



**Parameters:**
 
 - <b>`bot_info`</b> (``~switch.api.bot.models.BotInfo``):  The bot info to update 



**Returns:**
 
 - <b>`:obj`</b>: ``~switch.api.bot.models.BotInfo``: The bot info 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
