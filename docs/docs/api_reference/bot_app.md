---
sidebar_position: 1
---

# BotApp

`Class swibots.BotApp`

This is the main class of the library. It is used to create a bot app and to call the API methods.


## Properties

- `token` (`str`): Bot token (This is the token you must use to authenticate the bot)
- `bot_description` (`str`, Optional): Bot description (This is the description of the bot)
- `auto_update_bot` (`bool`, Optional): Auto update bot (This is the flag to enable/disable the auto update of the bot into the database)
- `receive_updates` (`bool`, Optional): Whether to receive event updates, defaults to `True`.
- `loop` (`asyncio.AbstractEventLoop`, Optional): AsyncIO Event loop (This is used in case you want to use a custom event loop)


## Example

```python
from swibots import BotApp

app = BotApp("token", "This is a bot")

with app:
    app.send_message(123, "Hello world")

```
