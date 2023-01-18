---
sidebar_position: 2
---

# Keyboards

The `Message` class contains a property called `inline_markup` where you can add buttons to allow the user interact with your bot. This is called an inline keyboard.

## Creating an inline keyboard

You can create an inline keyboard using the `InlineKeyboard` class. This class contains a method called `add_button` that allows you to add buttons to the keyboard. This method takes 3 parameters:

- `text`: The text that will be shown on the button.
- `callback_data`: The data that will be sent to the bot when the button is pressed.
- `url`: The URL that will be opened when the button is pressed.

:::tip
You can also add a inline keyboard passing a *list of lists* (each list is an `inline_markup` row, containing another list with one or more `InlineKeyboardButton`) of `InlineKeyboardButton` objects to the `inline_keyboard` parameter of the `InlineMarkup` class.
:::

Here is an example of how to create an inline keyboard, add it to a message and receive the callback data when the user presses a button:

```python

from switch import (
    BotApp,
    BotContext,
    CallbackQueryEvent,
    CommandEvent,
    InlineMarkup,
    InlineKeyboardButton,
    regexp,
)


env_file = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(env_file)


TOKEN = "YOUR_BOT_TOKEN"

# initialize the app and register commands
app = BotApp(
    TOKEN,
    auto_update_bot=False,  # disable auto update bot info
)


# register buttons command
@app.on_command("buttons")
async def buttons_handler(ctx: BotContext[CommandEvent]):
    m = await ctx.bot.prepare_response_message(ctx.event.message)
    m.message = f"Please select an option:"

    inline_keyboard = [
        [
            InlineKeyboardButton(text="Option 1", callback_data="option1"),
            InlineKeyboardButton(text="Option 2", callback_data="option2"),
        ],
        [
            InlineKeyboardButton(text="Option 3", callback_data="option3"),
            InlineKeyboardButton(text="Option 4", callback_data="option4"),
        ],
    ]

    m.inline_markup = InlineMarkup(inline_keyboard=inline_keyboard)
    await ctx.bot.send_message(m)


# handle callback query
@app.on_callback_query(regexp(r"option\d"))
async def callback_query_handler(ctx: BotContext[CallbackQueryEvent]):
    message = ctx.event.message
    message.message = f"Option with data: {ctx.event.callback_data} selected!"
    await ctx.bot.edit_message(message)


app.run()
