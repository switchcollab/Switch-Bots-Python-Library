### StickyHeader

The `StickyHeader` class represents a sticky header component in a user interface.

#### Properties

- `text` (Required): The text content of the sticky header.
- `color` (Optional): The color of the sticky header. If not provided, the default color is used.
- `callback_data` (Optional): Data associated with a callback.
- `icon` (Optional): An icon associated with the sticky header, represented by an instance of the `Icon` class.

#### Usage Example

```python
# Create a StickyHeader instance:
sticky_header = StickyHeader(
    text="Example Sticky Header",
    color="#3498db",
    callback_data="StickyHeaderCallback",
    icon=Icon("https://example.com/icon.png")
)
```