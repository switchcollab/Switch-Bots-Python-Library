class RegiterCommand:
    def __init__(
        self,
        command: str,
        description: str,
        channel: bool = False,
    ):
        self.command = command
        self.description = description
        self.channel = channel
