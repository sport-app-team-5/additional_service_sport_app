from app.seedwork.domain.exceptions import FactoryException


class ImplementationNotExistForFabricTypeException(FactoryException):
    def __init__(self, message='No existe una implementación para el repositorio con el tipo dado.'):
        self.__message = message

    def __str__(self):
        return str(self.__message)
