# ButtonGroup

The `ButtonGroup` class represents a group of action buttons in a user interface.

#### Properties

- `buttons` (Required, List[[Button](./Button.md)]): A list of `Button` components representing the buttons in the group.

#### Usage Example

```python
# Create a list of Button components for the ButtonGroup:
button_group_buttons = [
    Button(text="Button 1", callback_data="Callback Data 1"),
    Button(text="Button 2", callback_data="Callback Data 2"),
    Button(text="Button 3", callback_data="Callback Data 3"),
]

# Create a ButtonGroup instance:
button_group = ButtonGroup(buttons=button_group_buttons)
```