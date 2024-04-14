from dataclasses import dataclass
from app.seedwork.domain.factories import Factory
from app.seedwork.domain.repositories import Repository
from .repository import ServicesRepositoryPostgres
from ..domain.repository import ServicesRepository
from .exceptions import ImplementationNotExistForFabricTypeException


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type) -> Repository:
        if obj == ServicesRepository:
            return ServicesRepositoryPostgres()
        else:
            raise ImplementationNotExistForFabricTypeException()
