---
sidebar_position: 1
---

# Commands

Commands are the primary way of interacting with a bot.

They are short messages that start with a `/` following byt 1 to 32 characters with no spaces, and are sent to the bot in the chat. The bot will then receive the command and act accordingly.

Commands have also parameters, which are separated by spaces. For example, the command `/command param1 param2` has two parameters: `param1` and `param2`.

## Registering commands

Commands must be registered into the bot creating an instance of `RegisterCommand` class and passing it to the `add_command` method of the `BotApp` class.

The `BotCommand` class takes 2 parameters:

- `command:str`: The command name.
- `description:str`: The command description (a short descriptive string of what the command does).
- `channel:bool`: Whether the command can be used in a channel or not. Defaults to `False`.

```python
from swibots import (
    BotApp,
    BotCommand)

TOKEN= "YOUR_TOKEN"

app = BotApp(
    TOKEN, "A cool bot with annotations and everything you could possibly want :)"
).set_bot_commands(
    [
        BotCommand("test", "Test command", True),
        BotCommand("echo", "Echoes the message", True),
        BotCommand("buttons", "Shows buttons", True),
    ]
)

app.run()
```

:::caution
All the commands must be registered before the bot is started. 
The server will not send a `Command` event to the bot if the command is not registered.
:::

## Handling commands

As has been explained on [the handlers page](/docs/fundamentals/handlers), the bot will receive a `CommandEvent` when a command is sent to it.
To handle the command, you must create a handler function and register it using the `on_command` decorator or calling `add_hanlder` method of your bot app.

The handler function must accept a `BotContext[CommandEvent]` as its only argument.

```python
from swibots import (
    BotApp,
    BotContext,
    CommandEvent)

TOKEN = "YOUR_TOKEN"

app = BotApp(
    TOKEN, "A cool bot with annotations and everything you could possibly want :)"
).set_bot_commands(
    [
        BotCommand("echo", "Echoes the message", True)
    ]
)


@app.on_command("echo")
async def echo_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.prepare_response_message(ctx.event.message)
    # Get the text to echo from the command parameters
    text = ctx.event.params or "Nothing to echo"
    m.message = f"Your message: {text}"
    await ctx.send_message(m)

app.run()

```