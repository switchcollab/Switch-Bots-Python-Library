class Command:
    def __init__(
        self,
        name: str,
        description: str,
        channel: bool = False,
    ):
        self.name = name
        self.description = description
        self.channel = channel
