# get_community_media_files by status:
Get community media files by status.

### Parameters:
- `community_id` (`str`): The ID of the community.
- `status` (`int` | `List[int]`): status to look for.
- `channel_id` (`str`, optional): Channel id
- `group_id` (`str`, optional): group id
- `user_id` (`str`, optional): user id

### Returns:

- List[[Message](../types/message.md)]: A list of Message objects representing media files.

### Raises:
- `switch.error.SwitchError`: If the messages could not be retrieved.

### Example:
```python
# look for images

media_files = await client.get_community_media_files_by_status(community_id="communityID", status=1)
print(media_files)

# or to get the status, use enum
from swibots.types import MediaType
# status=MediaType.DOCUMENT.value
```
