# Poll Bot Example

This example demonstrates how to create a poll bot using SwiBots. The bot allows users to create polls, vote on them, and view results.

## Prerequisites

Before you begin, make sure you have:

1. Installed SwiBots (`pip install swibots`)
2. Obtained a bot token from the Switch platform

## The Code

Here's the complete code for our poll bot:

```python
import json
from swibots import (
    Client, BotContext, MessageEvent, CallbackQueryEvent,
    InlineKeyboardButton, InlineMarkup
)

app = Client("YOUR_BOT_TOKEN")
polls = {}  # In-memory storage for polls

@app.on_message()
async def message_handler(ctx: BotContext[MessageEvent]):
    message = ctx.event.message
    if message.message.startswith("/createpoll"):
        await create_poll(ctx)
    elif message.message.startswith("/viewpolls"):
        await view_polls(ctx)

@app.on_callback_query()
async def callback_handler(ctx: BotContext[CallbackQueryEvent]):
    data = json.loads(ctx.event.data)
    if data["action"] == "vote":
        await handle_vote(ctx, data)

async def create_poll(ctx: BotContext[MessageEvent]):
    parts = ctx.event.message.message.split("\n")
    if len(parts) < 4:
        await ctx.event.message.respond("Please provide a question and at least 2 options.")
        return

    question = parts[0].replace("/createpoll ", "")
    options = parts[1:]
    poll_id = str(len(polls) + 1)
    polls[poll_id] = {"question": question, "options": options, "votes": {opt: 0 for opt in options}}

    await ctx.event.message.respond(f"Poll created with ID: {poll_id}")

async def view_polls(ctx: BotContext[MessageEvent]):
    if not polls:
        await ctx.event.message.respond("No polls available.")
        return

    for poll_id, poll in polls.items():
        buttons = []
        for option in poll["options"]:
            buttons.append([InlineKeyboardButton(
                text=f"{option} ({poll['votes'][option]} votes)",
                callback_data=json.dumps({"action": "vote", "poll_id": poll_id, "option": option})
            )])

        markup = InlineMarkup(buttons)
        await ctx.event.message.respond(
            f"Poll {poll_id}: {poll['question']}",
            inline_markup=markup
        )

async def handle_vote(ctx: BotContext[CallbackQueryEvent], data):
    poll_id = data["poll_id"]
    option = data["option"]
    polls[poll_id]["votes"][option] += 1

    await ctx.event.answer("Vote recorded!")
    await view_polls(ctx)

app.run()
```

## Running the Bot

To run the bot, simply execute the script:

```bash
python poll_bot.py
```

## Using the Bot

1. Create a poll:
   ```
   /createpoll What's your favorite color?
   Red
   Blue
   Green
   Yellow
   ```

2. View active polls:
   ```
   /viewpolls
   ```

3. Vote on a poll by clicking the option buttons.

## Features Demonstrated

1. Command handling
2. Inline keyboards
3. Callback query handling
4. Basic data persistence (in-memory)
5. Dynamic message updates

## Note

This is a basic implementation. For a production-ready bot, consider adding error handling, input validation, and persistent storage for polls.