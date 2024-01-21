---
sidebar_position: 3
---

# Handlers

Handlers are functions that are called when an event is triggered. Handlers are registered with the calling `add_handler` funciton of app or using [`decorators`](./decorators).

## Handler functions

Handler functions are functions that are called when an event is triggered. They are registered with the `add_handler` function of the app. 
The function must accept a single argument, which is the [`BotContext`](./context) containig the info of the bot and the event.

There are one handler class for each event type. The handler class name is the same as the event class, but with the `Handler` suffix.


## Creating handlers

All handlers can be created calling the constructor of the handler class. The constructor accepts two arguments: the handler function, and a [filter](./filters) or a group of filters.

Each handler receives function (the first argument of the Handler) receives a BotContext[T] (where T is one of the EventTypes) as an argument. The BotContext contains the bot and the event that triggered the handler.

To define a handler callback function you must use the `async def` syntax, and the function must accept a single argument, which is the BotContext[T] of the event.

This is an example of how to create a handler function for each type of event:

```python
from swibots import Client, BotContext, MessageEvent, CommandEvent, CommandHandler, MessageHandler

app = Client("token", "your bot description")

async def message_handler(ctx: BotContext[MessageEvent]):
    await ctx.event.message.reply_text(f"Thank you! I received your message: {ctx.event.message.message}")

app.add_handler(MessageHandler(message_handler))

async def command_handler(ctx: BotContext[CommandEvent]):
    await ctx.event.message.reply_text(f"Thank you! I received your command: {ctx.event.command}")

app.add_handler(CommandHandler('THE_COMMAND', command_handler))

app.run()
```


## Registering handlers

Handlers are registered with the `add_handler` function of the app. The function accepts a single argument, which is the handler function.

This is an example of how to register a handler function:

```python
from swibots import Client, MessageHandler

app = Client("token", "your bot description")

async def message_handler(ctx: BotContext[MessageEvent]):
    await ctx.event.message.reply_text(f"Thank you! I received your message: {ctx.event.message.message}")

app.add_handler(MessageHandler(message_handler))

app.run()
```

## Chat handlers

### Message Handler

The `MessageHandler` is a handler for the `MessageEvent`. It is called when a message is sent to a chat.

#### Properties

- `callback` (`Callable[[BotContext[MessageEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example
```python
from swibots import Client, MessageHandler, MessageEvent, BotContext

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def message_handler(context: BotContext[MessageEvent]):
    message = context.event.message
    await message.reply_text("Hello world!")

# register handler
app.add_handler(MessageHandler(message_handler))
```

### Command Handler

The `CommandHandler` is a handler for the `CommandEvent`. It is called when a command is sent to a chat.

#### Properties

- `command` (`str` | `List[str]`): The command that will be used to filter the event. If a list is passed, the handler will be called if any of the commands is found.
- `callback` (`Callable[[BotContext[CommandEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example
```python
from swibots import Client, CommandHandler, CommandEvent, BotContext

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def command_handler(context: BotContext[CommandEvent]):
    message = context.event.message
    await message.reply_text("Hello world!")

# register handler
app.add_handler(CommandHandler("hello", command_handler))
```


### Callback Query Handler

The `CallbackQueryHandler` is a handler for the `CallbackQueryEvent`. It is called when a callback query is sent to a chat (the user pressed a button of the reply markup for example).

#### Properties

- `callback` (`Callable[[BotContext[CallbackQueryEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example
```python

from swibots import Client, CallbackQueryHandler, CallbackQueryEvent, BotContext

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def callback_query_handler(context: BotContext[CallbackQueryEvent]):
    message = context.event.message
    await message.reply_text("Hello world!")

# register handler
app.add_handler(CallbackQueryHandler(callback_query_handler))
```

### Inline Query Handler

The `InlineQueryHandler` is a handler for the `InlineQueryEvent`. It is called when an inline query is sent to a chat.

#### Properties

- `callback` (`Callable[[BotContext[InlineQueryEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example

```python

from swibots import Client, InlineQueryHandler, InlineQueryEvent, InlineQuery, BotContext

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def inline_query_handler(context: BotContext[InlineQueryEvent]):
    query: InlineQuery = ctx.event.query
    await query.answer(f"Searching results for {query.query}...")
    # ... search results and send them

# register handler
app.add_handler(InlineQueryHandler(inline_query_handler))
```


## Community handlers

### Community Updated Handler

The `CommunityUpdatedHandler` is a handler for the `CommunityUpdatedEvent`. It is called when a community is updated.

#### Properties

- `callback` (`Callable[[BotContext[CommunityUpdatedEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example

```python

from swibots import Client, CommunityUpdatedHandler, CommunityUpdatedEvent, BotContext, Community

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def community_updated_handler(context: BotContext[CommunityUpdatedEvent]):
    community: Community = ctx.event.community
    # ... do something with the community

# register handler
app.add_handler(CommunityUpdatedHandler(community_updated_handler))
```


### Member Joined Handler

The `MemberJoinedHandler` is a handler for the `MemberJoinedEvent`. It is called when a member joins a community.

#### Properties

- `callback` (`Callable[[BotContext[MemberJoinedEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example

```python

from swibots import Client, MemberJoinedHandler, MemberJoinedEvent, BotContext, User

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def member_joined_handler(context: BotContext[MemberJoinedEvent]):
    member: User = ctx.event.user # the user that joined the community
    # ... do something with the member

# register handler
app.add_handler(MemberJoinedHandler(member_joined_handler))
```


### Member Left Handler

The `MemberLeftHandler` is a handler for the `MemberLeftEvent`. It is called when a member leaves a community.

#### Properties

- `callback` (`Callable[[BotContext[MemberLeftEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example

```python

from swibots import Client, MemberLeftHandler, MemberLeftEvent, BotContext, User

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def member_left_handler(context: BotContext[MemberLeftEvent]):
    member: User = ctx.event.user # the user that left the community
    # ... do something with the member

# register handler
app.add_handler(MemberLeftHandler(member_left_handler))
```

### Channel Updated Handler

The `ChannelUpdatedHandler` is a handler for the `ChannelUpdatedEvent`. It is called when a channel is updated.

#### Properties

- `callback` (`Callable[[BotContext[ChannelUpdatedEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example

```python

from swibots import Client, ChannelUpdatedHandler, ChannelUpdatedEvent, BotContext, Channel

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def channel_updated_handler(context: BotContext[ChannelUpdatedEvent]):
    channel: Channel = ctx.event.channel
    # ... do something with the channel

# register handler
app.add_handler(ChannelUpdatedHandler(channel_updated_handler))
```


### Channel Created Handler

The `ChannelCreatedHandler` is a handler for the `ChannelCreatedEvent`. It is called when a channel is created.

#### Properties

- `callback` (`Callable[[BotContext[ChannelCreatedEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example

```python

from swibots import Client, ChannelCreatedHandler, ChannelCreatedEvent, BotContext, Channel

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def channel_created_handler(context: BotContext[ChannelCreatedEvent]):
    channel: Channel = ctx.event.channel
    # ... do something with the channel

# register handler
app.add_handler(ChannelCreatedHandler(channel_created_handler))
```

### Channel Deleted Handler

The `ChannelDeletedHandler` is a handler for the `ChannelDeletedEvent`. It is called when a channel is deleted.

#### Properties

- `callback` (`Callable[[BotContext[ChannelDeletedEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example

```python

from swibots import Client, ChannelDeletedHandler, ChannelDeletedEvent, BotContext, Channel

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def channel_deleted_handler(context: BotContext[ChannelDeletedEvent]):
    channel: Channel = ctx.event.channel
    # ... do something with the channel

# register handler
app.add_handler(ChannelDeletedHandler(channel_deleted_handler))
```

### Group Updated Handler

The `GroupUpdatedHandler` is a handler for the `GroupUpdatedEvent`. It is called when a group is updated.

#### Properties

- `callback` (`Callable[[BotContext[GroupUpdatedEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example

```python

from swibots import Client, GroupUpdatedHandler, GroupUpdatedEvent, BotContext, Group

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def group_updated_handler(context: BotContext[GroupUpdatedEvent]):
    group: Group = ctx.event.group
    # ... do something with the group

# register handler
app.add_handler(GroupUpdatedHandler(group_updated_handler))
```

### Group Created Handler

The `GroupCreatedHandler` is a handler for the `GroupCreatedEvent`. It is called when a group is created.

#### Properites

- `callback` (`Callable[[BotContext[GroupCreatedEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example

```python

from swibots import Client, GroupCreatedHandler, GroupCreatedEvent, BotContext, Group

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def group_created_handler(context: BotContext[GroupCreatedEvent]):
    group: Group = ctx.event.group
    # ... do something with the group

# register handler

app.add_handler(GroupCreatedHandler(group_created_handler))
```


### Group Deleted Handler

The `GroupDeletedHandler` is a handler for the `GroupDeletedEvent`. It is called when a group is deleted.

#### Properties

- `callback` (`Callable[[BotContext[GroupDeletedEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example

```python

from swibots import Client, GroupDeletedHandler, GroupDeletedEvent, BotContext, Group

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def group_deleted_handler(context: BotContext[GroupDeletedEvent]):
    group: Group = ctx.event.group
    # ... do something with the group

# register handler
app.add_handler(GroupDeletedHandler(group_deleted_handler))
```

### User Banned Handler

The `UserBannedHandler` is a handler for the `UserBannedEvent`. It is called when a user is banned from a group.

#### Properties

- `callback` (`Callable[[BotContext[UserBannedEvent]], Awaitable]`): The callback function that will be called when the event is triggered.
- `filter` (`Filter`, optional): The filter that will be used to filter the event. (Default: `None`)

#### Example

```python

from swibots import Client, UserBannedHandler, UserBannedEvent, BotContext, User, Group

# create app and call it app
app = Client('TOKEN')

# handler callback function
async def user_banned_handler(context: BotContext[UserBannedEvent]):
    user: User = ctx.event.user
    group: Group = ctx.event.group # or ctx.event.channel if the user was banned from a channel
    # ... do something with the user and the group 

# register handler
app.add_handler(UserBannedHandler(user_banned_handler))
```




