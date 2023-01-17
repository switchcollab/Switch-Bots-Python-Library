<!-- markdownlint-disable -->

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/bot/bot_client.py#L0"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

# <kbd>module</kbd> `api.bot.bot_client`




**Global Variables**
---------------
- **APP_CONFIG**


---

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/bot/bot_client.py#L7"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

## <kbd>class</kbd> `BotClient`
Bot client 

This client is used to communicate with the bot service. 

Controllers: 
    - :attr:`bots`: :obj:`~switch.api.bot.controllers.BotController` : The bot controller 

Properties: 
    - :attr:`user`: :obj:`~switch.api.auth.models.auth_user.AuthUser` : The current user 

<a href="https://github.com/switchcollab/Switch-Bots-Python-Library/tree/main/src/switch/api/bot/bot_client.py#L20"><img align="right" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"/></a>

### <kbd>method</kbd> `__init__`

```python
__init__(base_url: str = 'http://51.159.11.53:9999')
```

Initialize the bot client 



**Parameters:**
 
 - <b>`base_url`</b> (``str``):  The base url of the bot service. Defaults to the value in the config. 


---

#### <kbd>property</kbd> base_url





---

#### <kbd>property</kbd> bots

Get the bot controller 

---

#### <kbd>property</kbd> token





---

#### <kbd>property</kbd> user










---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
