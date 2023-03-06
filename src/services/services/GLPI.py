from src.services.adapters.TicketManager import TicketManager
from src.models.ticket import Ticket
from datetime import datetime
import requests
import base64


class GLPI(TicketManager):

    def __init__(self, user: str, password: str, access_token: str, api_link: str) -> None:
        self.statuses = {
            1: 'Novo',
            2: 'Em andamento (atribuido)',
            3: 'Em andamento (planejado)',
            4: 'Pendente',
            5: 'Solucionado',
            6: 'Fechado'
        }
        super().__init__(user, password, access_token, api_link)

    def init_session(self) -> None:
        login = '{}:{}'.format(self.user, self.password)
        login_b64 =  base64.b64encode(login.encode('ascii'))
        headers = {
            'Content-Type': 'applicatin/json',
            'Authorization': 'Basic ' + str(login_b64).replace('b', '').replace("'", ""),
            'App-Token': self.access_token
        }

        response = requests.get('{}/initSession'.format(self.api_link), headers=headers)
        self.session_token = self.clear_request_response(response.content)['session_token']


    def kill_session(self) -> None:
        headers = {
            'Content-Type': 'applicatin/json',
            'Session-Token': self.session_token,
            'App-Token': self.access_token
        }

        requests.get('{}/killSession'.format(self.api_link), headers=headers)

    def convert_date(self, date: str) -> datetime:
        if date == None:
            return ''

        return datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    def clear_content(self, content: str):
        return content.replace('&#60;/p&#62;', '').replace('&#60;p&#62;', '')

    def get_ticket_info(self, ticket_number: int) -> Ticket:
        if len(self.session_token ) <= 0:
            self.init_session()

        login = '{}:{}'.format(self.user, self.password)
        login_b64 =  base64.b64encode(login.encode('ascii'))

        headers = {
            'Content-Type': 'applicatin/json',
            'Authorization': 'Basic ' + str(login_b64).replace('b', '').replace("'", ""),
            'App-Token': self.access_token,
            'Session-Token':  self.session_token # 'trocar esse token depois de gerar um session_token'
        }
        response = requests.get('{}/Ticket/{}'.format(self.api_link, ticket_number), headers=headers)
        dict_response = self.clear_request_response(response.content)

        ticket = Ticket(dict_response['name'], self.convert_date(dict_response['date']), self.convert_date(dict_response['closedate']), self.convert_date(dict_response['solvedate']), self.convert_date(dict_response['date_mod']), self.clear_content(dict_response['content']), self.statuses[dict_response['status']])

        print(ticket.content)