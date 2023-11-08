# edit_media

Edits the media of a message.

```python
async def edit_media(
        self: "swibots.ApiClient",
        message_id: Optional[int] = None,
        media_id: Optional[int] = None,
        message: Optional[str] = None,
        document: Optional[str] = None,
        thumb: Optional[str] = None,
        inline_markup: InlineMarkup = None,
        progress=None,
        progress_args: Optional[Tuple] = None,
        mime_type: Optional[str] = None,
        file_name: Optional[str] = None,
    ) -> Message:
```

### Parameters

| Parameter | Type | Description |
|---|---|---|
| message_id | Optional[int] | The ID of the message to edit. |
| media_id | Optional[int] | The ID of the media to update. |
| message | Optional[str] | The new message or caption. |
| document | Optional[str] | The path to the new media file. |
| thumb | Optional[str] | The path to the new thumbnail file. |
| inline_markup | InlineMarkup, optional | The new inline markup for the message. |
| progress | _type_, optional | A callback function to be called during the upload progress. |
| progress_args | Optional[Tuple], optional | Arguments to be passed to the progress callback. |
| mime_type | Optional[str], optional | The MIME type of the new media file. |
| file_name | Optional[str], optional | The name of the new media file. |

### Returns

| Type | Description |
|---|---|
| Media | The edited message. |

### Example

```python
message_id = 1111

await client.edit_media(
    message_id=message_id,
    document="file.pdf",
    thumb="image.png"
)
 ```