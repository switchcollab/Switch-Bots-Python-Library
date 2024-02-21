# ListItem

The `ListItem` class represents a list tile in a user interface.

## Properties

- `title` (Optional): The main title of the list tile.
- `subtitle` (Optional): The subtitle of the list tile.
- `subtitle2` (Optional): An additional subtitle for the list tile.
- `subtitle_action` (Optional): Action associated with the subtitle.
- `callback_data` (Optional): Data associated with a callback.
- `right` (Optional): A list of components to be displayed on the right side of the list tile.
- `left` (Optional): A list of components to be displayed on the left side of the list tile.

## Usage Example

```python
# Create a ListItem instance:
list_item = ListItem(
    title="Item Title",
    subtitle="Item Subtitle",
    subtitle2="Additional Subtitle",
    subtitle_action="Subtitle Action",
    callback_data="Callback Data",
#   right=[Components...],
#   left=[Components...]
)
```

:::info
Unlike `GridItem` which is used in `Grid`, `ListItem` is used in `Dropdown` and not `List`.
:::
