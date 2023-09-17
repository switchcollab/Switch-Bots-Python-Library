## `sort_stickers` Method

Sorts stickers within a sticker pack.

### Signature

```python
async def sort_stickers(
    pack: StickerPack, sorted_stickers: List[str]
) -> StickerPack:
```

### Parameters

- `pack` (StickerPack): Sticker pack to sort stickers within.
- `sorted_stickers` (List[str]): List of sticker IDs representing the desired sorting order.

### Returns

- `StickerPack`: Sticker pack with stickers sorted as specified.
```