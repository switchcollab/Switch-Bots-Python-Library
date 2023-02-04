# InlineKeyboardButton

`Class pybots.api.chat.models.InlineKeyboardButton`

The `InlineKeyboardButton` class represents a button that can be added to an [inline keyboard](./inline_markup).

## Properties

- `text` (`str`): The button's text.
- `url` (`str`): The button's url.
- `callback_data` (`str`): The button's callback data.

## Usage 

```python
from pybots import InlineKeyboardButton, InlineMarkup

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



```