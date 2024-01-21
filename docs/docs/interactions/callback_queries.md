---
sidebar_position: 4
---

# Callback queries
with the callback queries, you can respond the user with Alert,
callback queries are called after the user click the `InlineKeyboardButton`

## `answer()`
#### Arguments
- `text` (`str`) the text to show.
- `show_alert` (`bool`): whether to show large/splash alert.
- `url` (`str`): the url as callback.
- `cache_time` (`int`):

### Example
```python
from swibots import Client, CallbackQueryEvent, BotContext

app = Client('TOKEN')

@Client.on_callback_query()
async def onCallback(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.answer(
        text="Hello this is a alert!",
        show_alert=True,
    )

```