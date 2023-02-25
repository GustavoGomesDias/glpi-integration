from datetime import datetime

class MessageControl:
    def __init__(self,  message_from: str, send_message_hour: datetime) -> None:
        self.message_from = message_from
        self.send_mesage_hour = send_message_hour