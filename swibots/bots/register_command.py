from swibots.utils.types import SCT


class RegisterCommand:
    def __init__(
        self,
        command: SCT[str],
        description: str,
        channel: bool = False,
    ):
        self.command = command
        self.description = description
        self.channel = channel
