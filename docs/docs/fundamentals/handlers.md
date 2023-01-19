---
sidebar_position: 3
---

# Handlers

Handlers are the way that SwiBots interacts with the outside world. Handlers are functions that are called when an event is triggered. Handlers are registered with the calling `add_hanlder` funciton of app or using [`decorators`](./decorators).

## Handler functions

Handler functions are functions that are called when an event is triggered. They are registered with the `add_handler` function of the app. 
The function must accept a single argument, which is the [`BotContext`](./context) containig the info of the bot and the event.

There are one handler class for each event type. The handler class name is the same as the event class, but with the `Handler` suffix.

### Chat handlers

- `MessageHandler` - A message was sent to a chat.
- `ComandHandler` - A command was sent to a chat.
- `CallbackQueryHandler` - A query callback was sent (user pressed a button, for example).
- `UnknownCommandHandler` - A registered was found but there are no handlers that can process it. (This can be used to create a default handler for commands.)

### Community handlers

- `CommunityUpdatedHandler` - A community was updated
- `MemberJoinedHandler` - A community was joined by an user
- `MemberLeftHandler` - A community was left by an user
- `ChannelCreatedHandler` - A channel was created
- `ChannelUpdatedHandler` - A channel was updated
- `ChannelDeletedHandler` - A channel was deleted
- `GroupCreatedHandler` - A group was created
- `GroupUpdatedHandler` - A group was updated
- `GroupDeletedHandler` - A group was deleted
- `UserBannedHandler` - An user was banned

## Registering handlers

Handlers are registered with the `add_handler` function of the app. The function accepts a single argument, which is the handler function.

This is an example of how to register a handler function:

```python
from swibots import BotApp, MessageHandler

app = BotApp("token", "your bot description")

async def message_handler(ctx: BotContext[MessageEvent]):
    m = await ctx.prepare_response_message(ctx.event.message)
    m.message = f"Thank you! I received your message: {ctx.event.message.message}"
    await ctx.send_message(m)

app.add_handler(MessageHandler(message_handler))

app.run()
```