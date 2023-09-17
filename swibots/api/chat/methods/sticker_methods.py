from typing import Type, TypeVar, Optional, List
import swibots
from io import BytesIO
from swibots.api.chat.models import Sticker, StickerPack


class StickerMethods:
    async def create_sticker(
        self: "swibots.ApiClient",
        sticker: str | BytesIO,
        name: str,
        description: str,
        emoji: str,
        pack_id: str,
    ) -> Sticker:
        """Create Sticker

        Args:
            sticker (str | BytesIO): path to file or BytesIO Object with .name
            name (str): Name of the sticker
            description (str): Description of the sticker.
            emoji (str): emoji linked with sticker.
            pack_id (str): pack Id to which sticker belongs.

        Returns:
            Sticker: the sticker object.
        """
        return await self.chat_service.stickers.create_sticker(
            sticker=sticker,
            name=name,
            description=description,
            emoji=emoji,
            pack_id=pack_id,
        )

    async def get_stickers(
        self: "swibots.ApiClient",
        pack_id: str,
        limit: Optional[int] = 30,
        offset: Optional[int] = 0,
    ) -> List[Sticker]:
        """Get All stickers from the pack

        Args:
            pack_id (str): Pack id of sticker.
            limit (Optional[int], optional): limit . Defaults to 30.
            offset (Optional[int], optional): offset to fetch. Defaults to 0.

        Returns:
            List[Sticker]
        """
        return await self.chat_service.stickers.get_stickers(
            pack_id, limit=limit, offset=offset
        )

    async def create_sticker_pack(
        self: "swibots.ApiClient",
        name: str,
        pack_type: str,
        access: str = "GLOBAL",
        thumb: Optional[str | BytesIO] = None,
    ) -> StickerPack:
        """Create Sticker pack

        Args:
            name (str): Name of sticker pack.
            pack_type (str): pack type for the sticker pack (STATIC, ANIMATED, VIDEO).
            access (str, optional): access mode for the pack. Defaults to "GLOBAL".
            thumb (Optional[str | BytesIO], optional): path to sticker pack thumbnail. Defaults to None.

        Returns:
            StickerPack: the resultant StickerPack
        """
        return await self.chat_service.stickers.create_sticker_pack(
            name=name, pack_type=pack_type, access=access, thumb=thumb
        )

    async def delete_sticker(self: "swibots.ApiClient", sticker_id: str) -> bool:
        """Delete sticker

        Args:
            sticker_id (str): Sticker ID

        Returns:
            bool: whether sticker was deleted
        """
        return await self.chat_service.stickers.delete_sticker(sticker_id)

    async def delete_sticker_pack(self: "swibots.ApiClient", pack_id: str) -> bool:
        """Delete sticker pack

        Args:
            pack_id (str): Pack ID

        Returns:
            bool: whether sticker pack was deleted
        """
        return await self.chat_service.stickers.delete_sticker_pack(pack_id)

    async def search_sticker_packs(
        self: "swibots.ApiClient",
        query: str,
        limit: Optional[int] = 20,
        offset: Optional[int] = 0,
    ) -> List[StickerPack]:
        """Search Sticker Packs

        Args:
            query (str): query to search
            limit (Optional[int], optional): Defaults to 20.
            offset (Optional[int], optional):  Defaults to 0.

        Returns:
            List[StickerPack]: List of sticker packs.
        """
        return await self.chat_service.stickers.search_sticker_packs(
            query=query, limit=limit, offset=offset
        )

    async def get_all_sticker_packs(
        self: "swibots.ApiClient", limit: Optional[int] = 20, offset: Optional[int] = 0
    ) -> List[StickerPack]:
        """Get All Sticker packs

        Args:
            limit (Optional[int], optional): Defaults to 20.
            offset (Optional[int], optional): Defaults to 0.

        Returns:
            List[StickerPack]
        """
        return await self.chat_service.stickers.get_all_sticker_packs(
            limit=limit, offset=offset
        )

    async def sort_stickers(
        self: "swibots.ApiClient", pack: StickerPack, sorted_stickers: List[str]
    ) -> StickerPack:
        """Sort stickers in sticker pack

        Args:
            pack (StickerPack): Sticker Pack
            sorted_stickers (List[str]): Sorted stickers.

        Returns:
            StickerPack: Sticker pack with sorted stickers.
        """
        return await self.chat_service.stickers.sort_stickers(
            pack=pack, sorted_stickers=sorted_stickers
        )
