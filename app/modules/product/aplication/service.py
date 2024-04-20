from sqlalchemy.orm import Session
from app.modules.product.aplication.dto import ProductRequestDTO, ProductResponseDTO
from app.modules.product.domain.repository import ProductRepository
from app.modules.product.infrastructure.factories import RepositoryFactory
from app.modules.third_party.aplication.service import ThirdPartyService


class ProductService:
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    def create_product(self, user_id: int, product: ProductRequestDTO, db: Session) -> ProductResponseDTO:
        third_party_service = ThirdPartyService()
        third_party = third_party_service.get_third_party_by_user_id(user_id, db)
        product.third_party_id = third_party.id
        repository = self.repository_factory.create_object(ProductRepository)
        return repository.create(product, db)
