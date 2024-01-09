### GridTile

The `GridTile` class represents a tile within a grid layout.

#### Properties

- `title` (Required): The title of the grid tile.
- `media` (Required): The media content associated with the grid tile.
- `subtitle` (Optional): The subtitle of the grid tile.
- `callback_data` (Optional): Data associated with a callback.
- `selective` (Optional): A flag indicating whether the grid tile is selective.

#### Usage Example

```python
# Create a GridTile instance:
grid_tile = GridTile(
    title="Tile Title",
    media="tile_image.jpg",
    subtitle="Tile Subtitle",
    callback_data="Callback Data",
    selective=True
)
```