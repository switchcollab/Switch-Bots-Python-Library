# remove_handler

Remove a handler from the bot.

## Signature

`def remove_handler(self, handler: BaseHandler | List[BaseHandler]) -> BotApp`

## Parameters

- `handler` (`BaseHandler | List[BaseHandler]`): The handler to remove from the bot, or a list of handlers to add to the bot (see [Hanlders](../../fundamentals/handlers) for more information on handlers)


## Example

```python


from swibots import BotApp, BotContext, CommandEvent, MessageEvent, CallbackQueryEvent, filters, InlineKeyboardButton, InlineMarkup, BotCommandInfo

from swibots.bots.handlers import (
    MessageHandler,
    UnknownCommandHandler,
    CallbackQueryHandler,
    CommandHandler,
)


async def echo(ctx: BotContext[CommandEvent]):
    m = await ctx.bot.prepare_response_message(ctx.event.message)
    text = ctx.event.params or "No args"
    m.message = f"Your message: {text}"
    await ctx.bot.send_message(m)

app = BotApp()

# register your handlers here

echo_handler = CommandHandler(
    command="echo",
    callback=echo,
)
app.add_handler(
    echo_handler
)

# remove the handler
app.remove_handler(
    echo_handler
)

# now the handler won't be called when the user sends the /echo command

app.run()

```