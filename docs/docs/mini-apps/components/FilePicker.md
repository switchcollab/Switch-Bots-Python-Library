### FilePicker

The `FilePicker` class represents a component for selecting files in a user interface.

#### Properties

- `callback_data` (Required): Data associated with a callback.
- `files_count` (Optional): The maximum number of files that can be selected (default is 1).
- `mime_type` (Optional): A list of allowed file types based on MIME types. By default, it allows "png", "jpg", "jpeg", and "webp" files.

#### Usage Example

```python
# Create a FilePicker instance:
file_picker = FilePicker(
    callback_data="FilePickerCallback",
    files_count=1,
    mime_type=["png", "jpg", "jpeg", "webp"]
)
```

:::note
The response can be obtained as shown below:

```python
@app.on_callback_query(regexp(...))
async def onCallback(ctx: BotContext[CallbackQueryEvent]):
    details = ctx.event.details
    print("User Upload", details.file_name, details.file_url)
```
:::