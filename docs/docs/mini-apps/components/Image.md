# Image
The `Image` class represents an image in a user interface.

#### Properties
- `url` (Required, `str`): The URL of the image.
- `dark_url` (Optional, `str`): The URL of the image for dark mode.
- `callback_data` (Optional, `str`): Data associated with a callback.

#### Usage Example

```python
# Create an Image instance:
image = Image(url="https://example.com/image.jpg", callback_data="Callback Data")
```
