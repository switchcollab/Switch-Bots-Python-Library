# Button
The `Button` class represents an action button in a user interface.

#### Properties

- `text` (Required): The text content of the button. It can be either a string or a `Text` component.
- `icon` (Optional): The icon associated with the button. It can be either a string (URL) or an `Icon` component.
- `callback_data` (Optional): Data associated with a callback.

#### Methods

- **Constructor**

```python
def __init__(
    self,
    text: Union[str, Text],
    icon: Union[str, Icon] = "",
    callback_data: Optional[str] = None,
)
```

#### Usage Example

```python
# Create a Button instance:
button = Button(
    text="Click Me",
    icon="https://example.com/icon.png",
    callback_data="Callback Data"
)
```