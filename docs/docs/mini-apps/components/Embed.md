# Embed

The `Embed` class represents an embedded content (i.e WebView) in a user interface.

### Properties

- `url` (Required): The URL of the embedded content.
- `height` (Optional): The height of the embedded content.
- `width` (Optional): The width of the embedded content.
- `expand` (Optional): A flag indicating whether the embedded content should be expandable.
- `full_screen` (Optional): A flag indicating whether the embedded content should be displayed in full screen.
- `landscape` (Optional): A flag indicating whether the embedded content should be displayed in landscape orientation.
- `allow_navigation` (Optional): A flag indicating whether navigation is allowed within the embedded content.
- `enable_ads` (Optional): A flag indicating whether ads are enabled within the embedded content.
- `view_ratio` (Optional): The view ratio of the embedded content.

### Methods

- **Constructor**

```python
def __init__(
    self,
    url: str,
    height: Optional[int] = 0,
    width: Optional[int] = 0,
    expand: Optional[bool] = False,
    full_screen: Optional[bool] = True,
    landscape: bool = False,
    allow_navigation: bool = True,
    enable_ads: bool = False,
    view_ratio: int = None,
)
```


```python
# Create an Embed instance:
embed = Embed(
    url="https://example.com/embedded-content",
    view_ratio=30
    # to show webview in 30% of screen
)
```