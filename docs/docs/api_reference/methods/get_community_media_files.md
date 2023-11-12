# get_community_media_files:
Get community media files.

### Parameters:

- `community_id` (str): The ID of the community.

### Returns:

- List[[Message](../types/message.md)]: A list of Message objects representing media files.

### Raises:
- `switch.error.SwitchError`: If the messages could not be retrieved.

### Example:

```python
media_files = await client.get_community_media_files("communityID")
print(media_files)
```
