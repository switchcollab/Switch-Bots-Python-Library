## `get_stickers` Method

Retrieves a list of stickers from a sticker pack.

### Signature

```python
async def get_stickers(
    pack_id: str,
    limit: Optional[int] = 30,
    offset: Optional[int] = 0,
) -> List[Sticker]:
```

### Parameters

- `pack_id` (str): Pack ID of the sticker pack.
- `limit` (Optional[int]): The maximum number of stickers to retrieve. Defaults to 30.
- `offset` (Optional[int]): The offset to fetch stickers. Defaults to 0.

### Returns

- `List[Sticker]`: List of stickers from the specified pack.
