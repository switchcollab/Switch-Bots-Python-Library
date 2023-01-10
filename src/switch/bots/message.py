class Message:
    async def reply(self, text: str, **kwargs) -> dict:
        """Reply to a message"""
        raise NotImplementedError

    async def edit(self, text: str, **kwargs) -> dict:
        """Edit a message"""
        raise NotImplementedError

    async def delete(self, **kwargs) -> dict:
        """Delete a message"""
        raise NotImplementedError