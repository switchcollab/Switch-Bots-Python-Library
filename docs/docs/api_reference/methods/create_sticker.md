## `create_sticker`
Creates a new sticker and adds it to a sticker pack.

### Signature

```python
async def create_sticker(
    self: "swibots.ApiClient",
    sticker: str | BytesIO,
    name: str,
    description: str,
    emoji: str,
    pack_id: str,
) -> Sticker:
```

### Parameters

- `sticker` (str | BytesIO): Path to the sticker file or BytesIO object with a `.name` attribute.
- `name` (str): Name of the sticker.
- `description` (str): Description of the sticker.
- `emoji` (str): Emoji linked with the sticker.
- `pack_id` (str): Pack ID to which the sticker belongs.

### Returns

- `Sticker`: The created sticker object.