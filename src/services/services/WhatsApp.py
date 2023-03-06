from pathlib import Path
from src.services.adapters.Message import Message
from datetime import datetime
import pywhatkit

class WhatsApp(Message):

    def __init__(self) -> None:
        super().__init__()
    
    def send_message(self, phone_number: str, message: str):

        actual_hour = datetime.now().hour
        actual_minute = datetime.now().minute + 1

        pywhatkit.sendwhatmsg('+55027996091279', message, actual_hour, actual_minute, 15, True, 2)