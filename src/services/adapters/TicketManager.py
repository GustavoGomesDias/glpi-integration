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

    def convert_date(self, date: str) -> datetime:
        if date == None:
            return ''

        return datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    def clear_request_response(self, response: bytes) -> dict[str, str | int]:
        return json.loads(str(response).replace('b', '').replace("'", ""))

    def init_session(self) -> None:
        pass

    def kill_session(self) -> None:
        pass

    def get_ticket_info(self, ticket_number: int) -> Ticket:
        pass
