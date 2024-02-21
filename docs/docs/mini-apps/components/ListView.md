# ListView

Represents a list view containing multiple list tiles.

### Constructor:

- `options`: A list of `ListTile` or `SmallListTile` instances.
- `view_type` (Optional): The type of the list view, default is `ListViewType.DEFAULT`.

## ListViewType

Enumerates the types of list views available.

#### Enum Values:

- `DEFAULT`: Represents the default list view type.
- `SMALL`: Represents a small-sized list view.
- `LARGE`: Represents a large-sized list view.


### Usage Example:

```python
list_view = ListView(
    options=[list_tile, small_list_tile],
    view_type=ListViewType.SMALL
)
```

