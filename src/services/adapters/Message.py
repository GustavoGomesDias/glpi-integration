import abc

class Message(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def convert_phone_number(phone_number: str):
        return

    @abc.abstractmethod
    def send_message(self, phone_number: str, message: str):
        return