# Badge

The `Badge` class represents a badge component in a user interface.

### Properties

- `text` (Required): The text content of the badge.
- `background` (Optional): The background color of the badge.
- `text_color` (Optional): The text color of the badge.

### Methods

```python
def __init__(
    self,
    text: str,
    background: str = None,
    text_color: str = None
)
```

### Usage Example:
```python
# Create a Badge instance:

badge = Badge(
    text="New",
    background="blue",
    text_color="white"
)
```