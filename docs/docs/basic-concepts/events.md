---
sidebar_position: 3
---

# Handling events

[Events](../fundamentals/events) are actions that happen in your Switch account (incoming messages, new members join, bot button presses, etc.), and you can use them to trigger actions in your bot.

To listen to an event, you need to register [event handlers](../fundamentals/handlers). 

Each handler deals with a specific event and once a matching update arrives from the app, your registered callback function will be called back by the framework and its body executed.

## Registering a handler

To explain how handlers work let’s examine the one which will be in charge for handling `Message` updates coming from all around your chats. Every other kind of handler shares the same setup logic and you should not have troubles settings them up once you learn from this section.

### Using decorators

The most elegant way to register a message handler is by using the `on_message()` decorator:

```python
from swibots import BotApp, BotContext,  MessageEvent

app = BotApp("TOKEN")

@app.on_message()
async def message_handler(ctx: BotContext[MessageEvent]):
   await m.reply_text(f"Thank you! I received your message: {ctx.event.message.message}")

app.run()
```

The defined function `message_handler`, which accepts one argument (`ctx`, of type `BotContext[MessageEvent]`), will be the function that gets executed every time a new message arrives.

In the last line we see again the `run()` method, this time used without any argument. Its purpose here is simply to automatically `start()`, keep the app online so that it can listen for updates and` stop()` it once you hit `CTRL+C`.

### Using the `add_handler()` method

If you prefer to use the `add_handler()` method instead of the decorator, you can do so by calling `add_hanlder` of the app with an instance of `MessageHandler` object:

```python
from swibots import BotApp, BotContext, MessageEvent, MessageHandler

app = BotApp("TOKEN")

async def handle_message(ctx: BotContext[MessageEvent]):
    await m.reply_text(f"Thank you! I received your message: {ctx.event.message.message}")

app.add_handler(MessageHandler(handle_message))

app.run()
```