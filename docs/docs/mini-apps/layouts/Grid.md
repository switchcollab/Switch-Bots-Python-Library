# Grid

The `Grid` class represents a grid layout.

#### Properties

- `title` (Optional | `str`): The title of the grid.
- `horizontal` (Optional | `bool` = `False`): A flag indicating whether the grid layout is a scrollable horizontal layout.
- `options` (Optional | `List[GridItem]`): A list of `GridItem` objects representing the grid items.
- `size` (Optional | int = `3`): The size of the grid. If `horizontal` is false, this many numbers of `GridItem`s will be shown per line.
- `expansion` (Optional | `Expansion` = `Expansion.DEFAULT`): The expansion type of the grid.
- `right_image` (Optional | `str`): A link to image to show at end of the Grid title towards right.
- `image_callback` (Optional | `str`): The callback data to the `right_image`

#### Usage Example

```python
# Create a Grid instance:
grid_layout = Grid(
    title="Grid Title",
    horizontal=False,
    options=[GridItem(...), GridItem(...), GridItem(...)],
    size=3,
    expansion=Expansion.HORIZONTAL,
    right_image='https://i.imgur.com/rfukFDY.png',
    image_callback='some_callback_data',
)
```