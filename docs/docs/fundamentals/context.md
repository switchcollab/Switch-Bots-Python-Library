---
sidebar_position: 5
---

# Bot Context

The `BotContext` is the object that is passed to the handler functions. It contains the information of the bot and the event that triggered the handler.
You can use the `BotContext` to send messages, get information about the user, etc (All of the methods available in the API are callable via the context).

## BotContext properties

- `bot:Bot` - The bot that owns the current context.
- `event:Event` - The event that triggered the handler.