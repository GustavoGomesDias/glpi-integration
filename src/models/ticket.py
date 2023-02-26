from datetime import datetime
from typing import Any

class Ticket:
    def __init__(self, name: str, date: datetime, closedate: datetime, solvedate: datetime, datemod: datetime, content:  str, status: str | int) -> None:
        self.name = name
        self.date = date
        self.closedate = closedate
        self.solvedate = solvedate
        self.datemod = datemod
        self.status = status
        self.content = content

    def __getattribute__(self, item):
        # Calling the super class to avoid recursion
        return super(Ticket, self).__getattribute__(item)
        