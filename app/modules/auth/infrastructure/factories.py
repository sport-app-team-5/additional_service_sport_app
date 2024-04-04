from dataclasses import dataclass
from .exceptions import ImplementationNotExistForFabricTypeException
from app.seedwork.domain.factories import Factory
from .repository import AuthRepositoryPostgres
from ..domain.repository import AuthRepository


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj_type) -> AuthRepositoryPostgres:
        if obj_type == AuthRepository:
            return AuthRepositoryPostgres()
        else:
            raise ImplementationNotExistForFabricTypeException()
