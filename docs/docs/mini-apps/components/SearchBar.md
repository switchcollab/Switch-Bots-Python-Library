# SearchBar

The `SearchBar` class represents a search bar in a user interface.

#### Properties

- `placeholder` (Optional): The placeholder text for the search bar.
- `label` (Optional): The label for the search bar.
- `value` (Optional): The current value of the search bar.
- `right_icon` (Optional): The icon on the right side of the search bar.
- `left_icon` (Optional): The icon on the left side of the search bar.
- `callback_data` (Optional): Data associated with a callback.

#### Usage Example

```python
# Create a SearchBar instance:
search_bar = SearchBar(
    placeholder="Search",
    label="Search Label",
    value="Initial Value",
    right_icon="https://img.icons8.com/?size=50&id=12773&format=png",
    left_icon="https://img.icons8.com/?size=50&id=47516&format=png",
    callback_data="Callback Data"
)
```