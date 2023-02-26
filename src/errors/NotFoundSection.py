class NotFoundSection(Exception):
    def __init__(self, message: str = 'Seção inexistente') -> None:
        self.message = message
        super().__init__(self.message)