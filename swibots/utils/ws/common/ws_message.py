class WsMessage:
    def __init__(self, raw):
        self.raw = raw
        self.headers = raw.headers
        self.body = raw.body
        self.command = raw.command
        self.destination = raw.headers.get("destination")
        self.subscription = raw.headers.get("subscription")
        self.message_id = raw.headers.get("message-id")
        self.ack = raw.headers.get("ack")
        self.nack = raw.headers.get("nack")
