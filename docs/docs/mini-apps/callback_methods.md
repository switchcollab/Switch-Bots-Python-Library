---
sidebar_position: 2
title: "Callback Methods"
---
This page contain certain tasks which are made available to the mini-apps to interact with user.

## copy
#### Arguments:
- `text`: (str): text to copy on user's device.

#### Example
```python
@app.on_callback_query()
async def onQuery(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.copy(
        "Here is the secret copied message, https://switch.pe/"
    )
```

## redirect
#### Arguments:
- `url`: (str): redirect user to the given url!

#### Example
```python
@app.on_callback_query()
async def onQuery(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.redirect(
        url="https://switch.pe/"
    )
```

## share
#### Arguments:
- `text` (str): text to prompt share on user device.
#### Example
```python
@app.on_callback_query()
async def onQuery(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.share(
        text="Share this cool app with yours friends! https://switch.pe/"
        
    )
```