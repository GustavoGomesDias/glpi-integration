import abc
from src.models.ticket import Ticket
from datetime import datetime
import json

class TicketManager(metaclass=abc.ABCMeta):

    def __init__(self, user: str, password: str, access_token: str, api_link: str) -> None:
        self.user = user
        self.password = password
        self.access_token = access_token
        self.session_token: str = ''
        self.api_link = api_link

    @abc.abstractmethod
    def convert_date(self, date: str) -> datetime:
        pass

    @abc.abstractmethod
    def clear_request_response(self, response: bytes) -> dict[str, str | int]:
        return json.loads(str(response).replace('b', '').replace("'", ""))

    @abc.abstractmethod
    def init_session(self) -> None:
        pass

    @abc.abstractmethod
    def kill_session(self) -> None:
        pass

    @abc.abstractmethod
    def get_ticket_info(self, ticket_number: int) -> Ticket:
        pass
