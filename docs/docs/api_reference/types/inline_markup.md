# InlineMarkup

`Class swibots.api.chat.models.InlineMarkup`

The `InlineMarkup` class represents a markup that can be added to a message (Only bots can add markup to the messages).

## Properties

- `inline_keyboard` (List[List[[InlineKeyboardButton](./inline_keyboard_button)]]): The markup's buttons.


## Usage 

```python
from swibots import InlineKeyboardButton, InlineMarkup

button1 = InlineKeyboardButton(
    text="Button Text",
    url="https://example.com",
    callback_data="callback_data"
)

button2 = InlineKeyboardButton(
    text="Button Text",
    url="https://example.com",
    callback_data="callback_data"
)

button3 = InlineKeyboardButton(
    text="Button Text",
    url="https://example.com",
    callback_data="callback_data"
)

## create a row of buttons
row1 = [button1, button2, button3]

# add the row to the keyboard

keyboard = InlineMarkup(inline_keyboard=[row1])

# add the keyboard to the message

message = Message(text="Hello World", inline_markup=keyboard)

```