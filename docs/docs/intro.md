---
sidebar_position: 1
---

# Quick start

Let's discover **PySwitch in less than 5 minutes**.

## Getting Started

You can start building your first app with PySwitch in less than 5 minutes.

1. Clone the PySwitch repository and install the requirements

```bash
git clone https://github.com/switchcollab/Switch-Bots-Python-Library
cd Switch-Bots-Python-Library/src
python install -r requirements.txt
```




2. Open the editor of your choice and create a python file echobot.py (or whatever name you want!), and paste the following code:

```python title="echobot.py"
from pyswitch import (
    BotApp,
    BotContext,
    MessageEvent
)

TOKEN = "MY SUPER SECRET TOKEN"

# initialize the app and register commands
app = BotApp(
    TOKEN, "A cool bot with annotations and everything you could possibly want :)"
)


@app.on_message()
async def message_handler(ctx: BotContext[MessageEvent]):
    # easy way to prepare a mesage that is a response of an incomming message
    m = await ctx.prepare_response_message(ctx.event.message)
    m.message = f"Thank you! I received your message: {ctx.event.message.message}"
    # send the message back to the user
    await ctx.send_message(m)


app.run()
```

3. Save your file and run it

```bash
python echobot.py
```

4. Open your switch app and send a message to the bot ```Hello world!```

5. You will receive a reply from your bot saying ```Thank you! I received your message: Hello world! ```