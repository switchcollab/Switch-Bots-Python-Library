---
sidebar_position: 1
---

# Client

`Class swibots.Client`

This is the main class of the library. It is used to create a bot app and to call the API methods.


## Properties
- `token` (`str`, Optional): Bot token (This is the token you must use to authenticate the bot)
- `email` (`str`, Optional): Email (only required for user login)
- `password` (`str`, Optional): Password (only required for user login)
- `bot_description` (`str`, Optional): Bot description (This is the description of the bot)
- `auto_update_bot` (`bool`, Optional): Auto update bot (This is the flag to enable/disable the auto update of the bot into the database)
- `receive_updates` (`bool`, Optional): Whether to receive event updates, defaults to `True`.
- `loop` (`asyncio.AbstractEventLoop`, Optional): AsyncIO Event loop (This is used in case you want to use a custom event loop)
- `is_app` (`bool`, Optional): Whether to mark the bot as a APP!
- `home_callback` (`str`, Optional): The default callback data to send, if opened through 'open app' button!


## Example

```python
from swibots import Client

# login as a bot
app = Client("token", bot_description="This is a bot")
# login as a user
app = Client(
    email="user@mail.com",
    password="password"
)

async def main():
    await app.send_message(123, "Hello world")

app.run(main())
```
