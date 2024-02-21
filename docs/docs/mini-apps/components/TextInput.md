## TextInput

The `TextInput` class represents an input box component for capturing user input in a user interface.

### Properties

- `label` (Required): The label associated with the input box.
- `value` (Optional): The current value of the input box.
- `width` (Optional): The width of the input box.
- `placeholder` (Optional): The placeholder text displayed in the input box.
- `callback_data` (Optional): Data associated with a callback.
- `keyboard_type` (Optional): The type of keyboard to be displayed (default is `KeyboardType.TEXT`).
- `error` (Optional): A boolean flag indicating whether an error state is present.
- `error_text` (Optional): The text to be displayed in case of an error.
- `password` (Optional): A boolean flag indicating whether the input should be treated as a password.
- `right_icon` (Optional): An icon displayed on the right side of the input box.
- `left_icon` (Optional): An icon displayed on the left side of the input box.
- `expanded` (bool): whether to show expanded text input.
- `multiline` (bool): whether to show multiline input.

## KeyboardType Enum

The `KeyboardType` enum defines the following keyboard types:

- `NUMBER`: Numeric keyboard.
- `TEXT`: Text keyboard (default).
- `EMAIL`: Email keyboard.
- `URL`: URL keyboard.

#### Usage Example

```python
# Create a TextInput instance:
text_input = TextInput(
    label="Username",
    value="",
    width=300,
    placeholder="Enter your username",
    callback_data="UsernameCallback",
    keyboardType=KeyboardType.TEXT,
    error=True,
    error_text="Invalid username",
    password=False,
    right_icon="https://img.icons8.com/?size=20&id=12345&format=png",
    left_icon="https://img.icons8.com/?size=20&id=67890&format=png",
)
```

:::note
The input value of TextInput can be obtained as shown below:

```python
@app.on_callback_query(regexp(...))
async def onCallback(ctx: BotContext[CallbackQueryEvent]):
    input_ = ctx.event.details.input_value
    print("User entered", input_)
```
:::