# Creating Your First Bot: Echo Bot

In this example, we'll create a simple echo bot using SwiBots. This bot will respond to any message it receives by sending the same message back to the user.

## Prerequisites

Before you begin, make sure you have:

1. Installed SwiBots (`pip install swibots`)
2. Obtained a bot token from the Switch platform

## The Code

Here's the complete code for our echo bot:

```python
from swibots import Client, BotContext, MessageEvent

app = Client("YOUR_BOT_TOKEN")

@app.on_message()
async def message_handler(ctx: BotContext[MessageEvent]):
    message = ctx.event.message
    await message.respond(f"Received: {message.message}")


app.run()
```

## Running the Bot

To run the bot, simply execute the script:

```bash
python echo_bot.py
```

## Testing the Bot
