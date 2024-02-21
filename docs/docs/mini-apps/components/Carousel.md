### Carousel

The `Carousel` class represents a carousel layout in a user interface.

#### Properties

- `images` (Required): A list of `Image` components representing the carousel images.
- `title` (Optional): The title of the carousel.
- `subtitle` (Optional): The subtitle or additional information about the carousel.

#### Usage Example

```python
# Create a list of Image components for the Carousel:
carousel_images = [
    Image(url="https://example.com/image1.jpg", callback_data="Callback Data 1"),
    Image(url="https://example.com/image2.jpg", callback_data="Callback Data 2"),
    Image(url="https://example.com/image3.jpg", callback_data="Callback Data 3"),
]

# Create a Carousel instance:
carousel = Carousel(
    images=carousel_images,
    title="Carousel Title",
    subtitle="Carousel Subtitle"
)
```