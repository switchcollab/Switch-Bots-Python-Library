---
sidebar_position: 1
---

# Bots
Every bot is an instance of the `Client` class. You can create a new bot by calling the `Client` constructor and passing it the bot token and the bot description.

```python
from swibots import Client

app = Client("token", "your bot description")

app.run()

```

## Register bot commands

**In order to be able to use the bot commands, you need to register them with the `set_bot_commands` method of the app.** This method accepts a list of `BotCommand` objects.

```python
from swibots import Client, BotCommand

app = Client("token", "your bot description", auto_update_bot=False) # [False] here means the commands are set one time until the bot is running

app.set_bot_commands([
    BotCommand("hello", "Hello description", True), # [True] here means the command is available in communities
    BotCommand("bye", "By description", False), # [False] here means its only available in personal chats with the bot
])

app.run()
```

The app will update your bot commands every time you run it, you can disable this behavior (for example, you just want to register your commands one time and you are not planning to update them) 
setting `auto_update_bot` param on the `Client` constructor to `False`.


:::info
The switch server will only send a [`CommandEvent`] to you only if you have it registred as a command!
Otherwise it's a normal message.
:::

### `BotCommand` class

The `BotCommand` class is a dataclass that contains the following fields:

- `command:str` - The command.
- `description:str` - The command description.
- `channel:bool` - Whether the command is available for use in communities or not.