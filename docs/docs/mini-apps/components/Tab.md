# TabBar

Represents a component containing a tab bar.

### Properties:
- `tabs`: A list of `TabBarTile` instances representing individual tabs.
- `bar_type`: The type of the tab bar, default is `TabBarType.SWIPE`.


# TabBarType

Enumerates the types of tab bars available.

### Enum Values:

- `SWIPE`: Represents a swipeable tab bar.
- `SEGMENTED`: Represents a segmented tab bar.
- `BUTTON`: Represents a button-based tab bar.

# TabBarTile
Represents a tile in a tab bar.

### Properties:

- `title`: The title or icon of the tab.
- `callback_data` (Optional): Callback data associated with the tab.
- `selected`: Indicates whether the tab is selected (`True`) or not (`False`).

### Usage Example:

```python
tab_tile = TabBarTile(
    title="Tab Title",
    callback_data="tab_callback_data",
    selected=True
)
```

### Usage Example:

```python
tab_bar_layout = TabBarLayout(
    tabs=[tab_tile1, tab_tile2, tab_tile3],
    bar_type=TabBarType.SWIPE
)
```