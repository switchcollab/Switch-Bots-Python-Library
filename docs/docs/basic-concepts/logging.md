---
sidebar_position: 4
---

# Logging

It is crucial you turn on the logging for swibots for better productivity!

```python {3,4} title="main.py"
from switbots import BotApp

import logging
logging.basicConfig(level=logging.INFO)

TOKEN = "" # Always import from [.env] file or system env

bot = BotApp(TOKEN, "My bot description")

bot.run()
```

:::info
The output these 2 specific lines produce is very informative!
:::

```bash title="Output"
INFO:swibots.bot_app:🚀 Starting app...
INFO:swibots.bot_app:Logged in as ['Bot Name'][bot_username_bot][bot_id]
INFO:swibots.bot_app:🚀 App started!
```