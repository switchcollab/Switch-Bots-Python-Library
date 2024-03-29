### GridItem

The `GridItem` class represents a tile within a grid layout.

#### Properties

- `title` (Required | `str`): The title of the grid tile.
- `media` (Required | `str`): Link to an image to be shown as media.
- `dark_media` (Optional | `str`): Link to an image to be shown in dark mode.
- `subtitle` (Optional | `str`): The subtitle of the grid tile.
- `callback_data` (Optional | `str`): Data associated with a callback.
- `selective` (Optional | `bool` = `False`): A flag indicating whether the grid tile is selective.

#### Usage Example

```python
# Create a GridTile instance:
grid_item = GridItem(
    title="Tile Title",
    media="https://i.imgur.com/0Gzqukk.jpeg",
    subtitle="Tile Subtitle",
    callback_data="Callback Data",
    selective=False,
)
```