from dataclasses import dataclass
from app.seedwork.domain.factories import Factory
from app.seedwork.domain.repositories import Repository
from .repository import ThirdPartyRepositoryPostgres
from ..domain.repository import ThirdPartyRepository
from .exceptions import ImplementationNotExistForFabricTypeException


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type) -> Repository:
        if obj == ThirdPartyRepository:
            return ThirdPartyRepositoryPostgres()
        else:
            raise ImplementationNotExistForFabricTypeException()
