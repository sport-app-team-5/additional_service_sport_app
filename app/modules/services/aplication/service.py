from typing import List
from sqlalchemy.orm import Session
from app.modules.services.aplication.dto import ServiceRequestDTO, ServiceResponseDTO
from app.modules.services.domain.repository import ServicesRepository
from app.modules.services.infrastructure.factories import RepositoryFactory
from app.seedwork.aplication.services import Service

from app.modules.third_party.aplication.service import ThirdPartyService


class ServicesService(Service):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    def create_service(self, service: ServiceRequestDTO, db: Session) -> ServiceResponseDTO:

        # user_id = get_current_user_id()
        # third_party = ThirdPartyService.get_third_party_by_user_id(user_id)
        # service.third_party_id = third_party.id

        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.create(service, db)

    def get_services(self, db: Session) -> List[ServiceResponseDTO]:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.get_all(db)

    def get_service_by_id(self, service_id: int, db: Session) -> ServiceResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.get_by_id(service_id, db)
    
    def get_service_by_user_id(self, service_id: int, db: Session) -> ServiceResponseDTO:
        # user_id = get_current_user_id()
        # third_party = ThirdPartyService.get_third_party_by_user_id(user_id)
        # service.third_party_id = third_party.id
        
        repository1 = self.repository_factory.create_object(ServicesRepository)
        return repository1.get_by_id(service_id, db)
    
    def update_service(self, service_id: int, service: ServiceRequestDTO, db: Session) -> ServiceResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.update(service_id, service, db)
    
    def deactivate(self, service_id: int, db: Session) -> ServiceResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.deactivate(service_id, db)
