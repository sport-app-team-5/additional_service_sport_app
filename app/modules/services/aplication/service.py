from typing import List
from sqlalchemy.orm import Session
from app.modules.services.aplication.dto import ServiceRequestDTO, ServiceResponseDTO
from app.modules.services.domain.repository import ServicesRepository
from app.modules.services.infrastructure.factories import RepositoryFactory
from app.seedwork.aplication.services import Service


class ServicesService(Service):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    def create_service(self, service: ServiceRequestDTO, db: Session) -> ServiceResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository.__class__)
        return repository.create(service, db)

    def get_services(self, db: Session) -> List[ServiceResponseDTO]:
        repository = self.repository_factory.create_object(ServicesRepository.__class__)
        return repository.get_all(db)

    def get_service_by_id(self, service_id: int, db: Session) -> ServiceResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository.__class__)
        return repository.get_by_id(service_id, db)
    
    def get_service_by_user_id(self, service_id: int, db: Session) -> ServiceResponseDTO:
        repository1 = self.repository_factory.create_object(ServicesRepository.__class__)
        return repository1.get_by_id(service_id, db)
