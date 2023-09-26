# EmbeddedMedia

The `EmbeddedMedia` class is used to send embedded media in messages.

## Parameters

- `thumbnail` (str): The media upload request or cover Url in updates.
- `title` `(str)`: title of message.
- `description` (`str`): description of message.
- `header_name` (`str`): header name.
- `header_icon` (`str`): header icon (URL)
- `footer_title` (`str`): footer title.
- `footer_icon` (`str`): footer icon (URL).
- `inline_fields` (List[List[EmbedInlineField]](./embed_inline_field.md)): The inline fields.


## Usage 

```python
from swibots import EmbeddedMedia, EmbedInlineField, MediaUploadRequest

embedded = EmbeddedMedia(
    thumbnail=MediaUploadRequest("image.png"),
    title="Embedded Message",
    description="This is description",
    header_name="header",
    header_icon="https://icons8.com/icon/6nsw3h9gk8M8/bot",
    footer_title="footer",
    footer_icon="https://icons8.com/icon/6nsw3h9gk8M8/bot",
    inline_fields=[[
        EmbedInlineField("", "Value", "Title")
    ]]
)
await message.respond("Embedded Message", media=embedded)
```