---
sidebar_position: 1
---

# Quick start

Let's discover **SwiBots in less than 5 minutes**.

## Getting Started

You can start building your first app with SwiBots in less than 5 minutes.

### 1. Install swibots library

```bash
pip install swibots -U
```

:::caution
This library requires Python 3.10 or higher. Please make sure you
have the latest version of Python installed. Check your Python version with the
following command:

```bash
python --version
```

If you don't have Python 3.10 or higher, you can download it from
[here](https://www.python.org/downloads/). (Follow the instructions for your
operating system)
:::

### 2. Open the editor of your choice and create a python file echobot.py (or
   whatever name you want!), and paste the following code:

```python title="echobot.py"
import logging
logging.basicConfig(level=logging.INFO)

from swibots import (
    Client,
    BotContext,
    MessageEvent
    BotCommand
)

TOKEN = "MY SUPER SECRET TOKEN" # Always keep this token in [.env] file

# initialize the app class
app = Client(
    TOKEN, # Your Bot Authorization Token
)
app.set_bot_commands(
    [
        BotCommand("start", "Start the bot", True)
    ]
)

@app.on_message()
async def listen_handler(ctx: BotContext[MessageEvent]):
    # easy way to prepare a mesage that is a response of an incomming message
    message = ctx.event.message
    # send the message back to the user
    await message.respond(
        f"Thank you! I received your message: {message.message}",
    )

app.run() # Run the bot
```

### 3. Save your file and run it

```bash
python echobot.py
```

#### 4. Open your switch app and send a message to the bot `Hello world!`

#### 5. You will receive a message from your bot saying
   `Thank you! I received your message: Hello world!`
