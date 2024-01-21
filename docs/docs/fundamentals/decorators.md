---
sidebar_position: 4
---

# Decorator Handlers

If you don't want to use the `add_handler` method, you can use decorators to register handlers to the app.

## Decorators
 
There are one to one matching decorators for each of the existing [`handlers`](./handlers) methods.

Let's say that you have defined your app as `app`, then you can use the following decorators to register handlers (change the `app` variable to whatever you have defined your app as):

- `@app.on_message`
- `@app.on_callback_query`
- `@app.on_command`
- `@app.on_channel_created`
- `@app.on_channel_updated`
- `@app.on_channel_deleted`
- `@app.on_group_created`
- `@app.on_group_updated`
- `@app.on_group_deleted`
- `@app.on_community_updated`
- `@app.on_member_joined`
- `@app.on_member_left`
- `@app.on_user_banned`
- `@app.on_unknown_command`
- `@app.on_inline_query`

The decorators are functions that take a function as an argument and return a function. The function that is returned is the handler that is registered to the app as a callback.

All of the decorators take the same arguments as the corresponding handler method. For example, the `@app.on_message` decorator takes the same arguments as the `app.add_handler(MessageHandler(...))` method, with the exception of the `callback` argument, which is the function that is decorated.

### Example


```python
from swibots import Client, MessageEvent, BotContext

app = Client("token", "your bot description")

@app.on_message()
async def message_handler(ctx: BotContext[MessageEvent]):
   await ctx.event.message.reply_text(f"Thank you! I received your message: {ctx.event.message.message}")

app.run()
```