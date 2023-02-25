from adapters.Message import Message
from models.message_control import MessageControl

class WhatsApp(Message):
    
    def t():
        print('ok')

    def check_if_have_only_number(self, message: str):
        return
    
    def send_message_reply(self, message_replt: str):
        return
    
    def check_if_is_initial_message(self, message_contro: MessageControl):
        return

    def add_in_message_control(self, message_control: MessageControl):
        return