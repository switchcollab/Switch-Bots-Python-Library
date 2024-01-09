# Embed

The `Embed` class represents an embedded content in a user interface.

#### Properties

- `url` (Required): The URL of the embedded content.
- `height` (Optional): The height of the embedded content.
- `width` (Optional): The width of the embedded content.
- `full_screen` (Optional): A flag indicating whether the embedded content should be displayed in full screen.

#### Methods

- **Constructor**

```python
def __init__(
    self,
    url: str,
    height: Optional[int] = 0,
    width: Optional[int] = 0,
    full_screen: Optional[bool] = True,
)
```

#### Usage Example

```python
# Create an Embed instance:
embed = Embed(
    url="https://example.com/embedded-content",
    height=300,
    width=400,
    full_screen=False
)
```