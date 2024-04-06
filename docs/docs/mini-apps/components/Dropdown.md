# Dropdown

The `Dropdown` class represents a dropdown in a user interface.

## Properties

- `placeholder` (Optional, `str`): The placeholder text for the dropdown.
- `selected` (Optional, `int`): The index of the selected item in the dropdown.
- `options` (List[ListTile]): A list of items representing the dropdown options.
- `disabled` (Optional, `bool`): A flag indicating whether the dropdown is disabled.


## Example
```python
from swibots import CallbackQueryEvent, BotContext
from swibots import AppPage, AppBar, Dropdown, ListItem

# handle callback query
@app.on_callback_query()
async def onCallback(ctx: BotContext[CallbackQueryEvent]):
    # create a callback component
    await ctx.event.answer(
        callback=AppPage(
            app_bar=AppBar(title="Hello from Swibots"),
            components=[
                Dropdown(
                    placeholder="Choose Option",
                    options=[
                        ListItem("1. Orange", callback_data="option1"),
                        ListItem("2. Yellow", callback_data="option2"),
                        ListItem("3. Green", callback_data="option3"),
                        ListItem("4. Green", callback_data="option4"),
                    ],
                )
            ],
        )
    )
```
