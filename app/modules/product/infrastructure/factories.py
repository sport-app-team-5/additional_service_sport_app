from dataclasses import dataclass
from app.seedwork.domain.factories import Factory
from .exceptions import ImplementationNotExistForFabricTypeException
from .repository import ProductRepositoryPostgres
from ..domain.repository import ProductRepository


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type) -> ProductRepositoryPostgres:
        if obj == ProductRepository:
            return ProductRepositoryPostgres()
        else:
            raise ImplementationNotExistForFabricTypeException()
