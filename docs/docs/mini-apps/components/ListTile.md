# ListTile

Represents a list item in a list view.

### Properties:

- `type`: The type of the list tile, set to "list_tile".
- `title`: The main title of the list tile.
- `description` (Optional): Additional information or description.
- `subtitle` (Optional): A secondary subtitle.
- `title_extra` (Optional): Extra information related to the title.
- `description_extra` (Optional): Extra information related to the description.
- `subtitle_extra` (Optional): Extra information related to the subtitle.
- `callback_data` (Optional): Callback data associated with the list tile.
- `thumb` (Optional): An image associated with the list tile. Can be an `Image` instance or a URL string.
- `badges`: (Optional, List[Badge]): Badges to show in compact list view.

### Usage Example:

```python
list_tile = ListTile(
    title="Example Tile",
    description="Description Text",
    subtitle="Subtitle Text",
    title_extra="Extra Title Info",
    description_extra="Extra Description Info",
    subtitle_extra="Extra Subtitle Info",
    callback_data="callback_data_value",
    thumb="https://example.com/image.jpg"
)
```


# SmallListTile

Represents a small-sized list item, inheriting from `ListTile`.

### Constructor:

- `title`: The main title of the small list tile.
- `icon` (Optional): An icon associated with the small list tile. Can be a URL string or an `Image` instance.
- `callback_data` (Optional): Callback data associated with the small list tile.

### Usage Example:

```python
small_list_tile = SmallListTile(
    title="Small Tile",
    icon="https://example.com/icon.png",
    callback_data="small_tile_callback_data"
)
```
