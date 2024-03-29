# Icon

The `Icon` class represents an icon component in a user interface.

### Properties

- `url` (Required): The URL of the icon.
- `dark_url` (Optional): The URL of the icon to be used in dark mode. If not provided, the default icon URL will be used.

### Methods

```python
def __init__(self, url: str, dark_url: str = None)
```

#### Usage Example
```python

# Create an Icon instance:
icon = Icon(url="https://example.com/icon.png", dark_url="https://example.com/dark-icon.png")
```