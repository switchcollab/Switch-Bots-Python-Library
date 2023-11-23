## `get_all_sticker_packs`
Retrieves all sticker packs.

### Signature

```python
async def get_all_sticker_packs(
    limit: Optional[int] = 20,
    offset: Optional[int] = 0,
) -> List[StickerPack]:
```

### Parameters

- `limit` (Optional[int]): The maximum number of sticker packs to retrieve. Defaults to 20.
- `offset` (Optional[int]): The offset for fetching sticker packs. Defaults to 0.

### Returns

- `List[StickerPack]`: List of all available sticker packs.