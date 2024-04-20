from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.modules.product.aplication.dto import ProductResponseDTO
from app.modules.product.domain.entities import Product
from app.seedwork.domain.repositories import Repository


class ProductRepository(Repository, ABC):
    @abstractmethod
    def create(self, entity: Product, db: Session) -> ProductResponseDTO:
        pass
