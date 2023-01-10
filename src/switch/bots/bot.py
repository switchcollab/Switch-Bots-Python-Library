from .message import Message

class Bot:
    def __init__(self, token: str):
        self._token = token
        self._commands = []
        self._me = None
        self._info = None

    async def get_me(self) -> dict:
        """Get user bot info"""
        raise NotImplementedError

    async def get_info(self) -> dict:
        """Get bot info"""
        raise NotImplementedError

    async def get_commands(self) -> list:
        """Get the commands"""
        raise NotImplementedError
    
    async def _send_message(self, **kwargs) -> Message | bool:
        """Send a message"""
        raise NotImplementedError

    async def send_message(self, message: str, **kwargs) -> Message | bool:
        """Send a message"""
        raise NotImplementedError
    
    async def edit_message(self, message: str, **kwargs) -> Message | bool:
        """Edit a message"""
        raise NotImplementedError
    
    async def delete_message(self, **kwargs) -> bool:
        """Delete a message"""
        raise NotImplementedError