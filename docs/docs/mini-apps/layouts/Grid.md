### Grid

The `Grid` class represents a grid layout.

#### Properties

- `size` (Optional): The size of the grid.
- `options` (Optional): A list of `GridItem` objects representing the grid items.
- `horizontal` (Optional): A flag indicating whether the grid layout is horizontal.
- `title` (Optional): The title of the grid.
- `expansion` (Optional): The expansion type of the grid.

#### Methods

#### Usage Example

```python
# Create a Grid instance:
grid_layout = Grid(
    title="Grid Title",
    horizontal=True,
    options=[GridItem(...), GridItem(...), GridItem(...)],
    size=3,
    expansion=Expansion.DEFAULT
)
```