from dataclasses import dataclass
from app.seedwork.domain.factories import Factory
from app.seedwork.domain.repositories import Repository
from .repository import EventRepositoryPostgres, ServicesRepositoryPostgres
from ..domain.repository import EventRepository, ServicesRepository
from .exceptions import ImplementationNotExistForFabricTypeException


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type) -> Repository:
        if obj == ServicesRepository:
            return ServicesRepositoryPostgres()
        elif obj == EventRepository:
            return EventRepositoryPostgres()
        else:
            raise ImplementationNotExistForFabricTypeException()
