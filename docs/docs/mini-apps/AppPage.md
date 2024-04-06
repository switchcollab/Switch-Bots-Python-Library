---
sidebar_position: 2
---

### AppPage

The `AppPage` class represents a page within a Switch application.

#### Properties

- `screen` (Optional): The type of screen for the page, default is `ScreenType.SCREEN`.
- `components` (Optional): A list of standalone components to be included in the page.
- `app_bar` (Optional): The app bar component for the page.
- `disable_appbar` (Optional, bool): Whether to disable the appbar for current page.
- `bottom_bar` (Optional): The bottom bar component for the page.

#### Methods

- **Constructor**

```python
def __init__(
    self,
    app: "swibots.App" = None,
    screen: ScreenType = ScreenType.SCREEN,
    layouts: List[Layout] = None,
    components: List[Component] = None,
    app_bar: AppBar = None,
    disable_appbar: bool = None,
    bottom_bar: BottomBar = None,
)
```

#### Usage Example

```python
# Create an AppPage instance:
app_page = AppPage(
    screen=ScreenType.FULLSCREEN,
    layouts=[Carousel(images=[Image(url="https://example.com/image1.jpg")])],
    components=[Button(text="Click Me")],
    app_bar=AppBar(title="My Page")
)
```

### ScreenType (Enum):
- `BOTTOM`: to display bottom sheet.
- `SCREEN`: to display as page.