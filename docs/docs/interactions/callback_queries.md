---
sidebar_position: 4
---

# Callback queries
with the callback queries, you can respond the user with Alert,
callback queries are called after the user click the `InlineKeyboardButton`

### Example
```python
from swibots import CallbackQueryEvent, BotContext

@Client.on_callback_query()
async def onCallback(ctx: BotContext[CommandEvent]):
    await ctx.event.answer(
        text="Hello this is a alert!"
    )

```