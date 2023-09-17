## `create_sticker_pack` Method

Creates a new sticker pack.

### Signature

```python
async def create_sticker_pack(
    name: str,
    pack_type: str,
    access: str = "GLOBAL",
    thumb: Optional[str | BytesIO] = None,
) -> StickerPack:
```

### Parameters

- `name` (str): Name of the sticker pack.
- `pack_type` (str): Pack type for the sticker pack (STATIC, ANIMATED, VIDEO).
- `access` (str, optional): Access mode for the pack. Defaults to "GLOBAL".
- `thumb` (Optional[str | BytesIO], optional): Path to the sticker pack thumbnail. Defaults to None.

### Returns

- `StickerPack`: The resultant StickerPack object.
