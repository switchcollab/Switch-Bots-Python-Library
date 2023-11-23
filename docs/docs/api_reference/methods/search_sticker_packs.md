## `search_sticker_packs```
Searches for sticker packs using a query.

### Signature

```python
async def search_sticker_packs(
    query: str,
    limit: Optional[int] = 20,
    offset: Optional[int] = 0,
) -> List[StickerPack]:
```

### Parameters

- `query` (str): Query to search for sticker packs.
- `limit` (Optional[int]): The maximum number of sticker packs to retrieve. Defaults to 20.
- `offset` (Optional[int]): The offset for fetching sticker packs. Defaults to 0.

### Returns

- `List[StickerPack]`: List of matching sticker packs.