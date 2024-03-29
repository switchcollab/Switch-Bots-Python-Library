---
sidebar_position: 3
---

## BottomBarTile

Represents a tile in the bottom bar of a user interface.

### Properties

- `name` (Required): The name of the tile.
- `icon` (Optional): The icon URL of the tile.
- `selected_icon` (Optional): The icon URL of the selected tile.
- `dark_icon` (Optional): The icon URL of the tile in dark mode.
- `dark_selection_icon` (Optional): The icon URL of the selected tile in dark mode.
- `selected` (Optional): A boolean indicating whether the tile is selected.
- `callback_data` (Optional): The callback data associated with the tile.

### Methods

- **Constructor**

```python
def __init__(
    self,
    name: str,
    icon: str = "",
    selection_icon: str = "",
    dark_icon: str = "",
    dark_selection_icon: str = "",
    callback_data: str = "",
    selected: bool = False,
)
```

## BottomBarType

Represents the type of the bottom bar.

### Enum Values

- `DEFAULT`: Default bottom bar.
- `TOPLINE`: Top line bottom bar.
- `BOTTOMLINE`: Bottom line bottom bar.
- `TOP_NOTCH`: Top notch bottom bar.
- `BOTTOM_NOTCH`: Bottom notch bottom bar.

Each enum value corresponds to a specific layout style for the bottom bar in the user interface.

## BottomBar

Represents the bottom bar component in a user interface.

### Properties

- `options` (Required): List of `BottomBarTile` instances representing the tiles in the bottom bar.
- `type` (Optional): The type of the bottom bar, specified by `BottomBarType`.
- `theme_color` (Optional): The theme color of the bottom bar.

### Methods
```python
def __init__(
    self,
    options: List[BottomBarTile],
    type: BottomBarType = BottomBarType.DEFAULT,
    theme_color: str = ""
)
```

### Usage Example:

```python
# Create a BottomBarTile instance:
tiles = [
    BottomBarTile(
        name="Home", icon="https://example.com/home_icon.png",
        selected=True
    ),
    BottomBarTile(
        name="Saved", icon="https://example.com/saved.png",
    ),
    BottomBarTile(
        name="Settings", icon="https://example.com/settings.png",
    ),
]

# Create a BottomBar instance:
bottom_bar = BottomBar(
    options=tiles,
    type=BottomBarType.DEFAULT,
    theme_color="#ffffff"
)
```