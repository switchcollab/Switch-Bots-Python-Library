## `get_media` Method

Retrieves media content by its media ID.

### Signature

```python
async def get_media(
    media_id: int
) -> Media:
```

### Parameters
- `media_id` (int): The unique identifier of the media content.

### Returns
- [Media](../types/media.md): The retrieved media content.

### Description

The `get_media` method allows you to fetch media content, such as images, videos, or other multimedia assets, by providing its unique media ID. This method is useful for accessing and displaying media content within your application.

## Example

```python
# Usage example:
media_id = 12345  # Replace with the actual media ID
media = await app.get_media(media_id)
# Now you can use the 'media' object for further processing or display.
```

Use this method to retrieve media content based on its ID, enabling you to integrate and showcase media elements within your application easily.