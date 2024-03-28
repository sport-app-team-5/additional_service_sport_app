class DomainException(Exception):
    ...


class FactoryException(DomainException):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return str(self.__message)
