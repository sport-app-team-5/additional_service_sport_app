from typing import List
from sqlalchemy.orm import Session
from app.modules.services.aplication.dto import AssociateSportmanEventRequestDTO, EventRequestDTO, EventResponseDTO, EventSportmanResponseDTO, EventUpdateRequestDTO, ServiceRequestDTO, ServiceResponseDTO
from app.modules.services.domain.repository import EventRepository, ServicesRepository
from app.modules.services.infrastructure.factories import RepositoryFactory
from app.seedwork.aplication.services import Service

from app.modules.third_party.aplication.service import ThirdPartyService


class ServicesService:
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    def create_service(self, user_id: int, service: ServiceRequestDTO, db: Session) -> ServiceResponseDTO:

        print("user_id: ", user_id)
        third_party_service = ThirdPartyService()
        third_party = third_party_service.get_third_party_by_user_id(user_id, db)
        
        if third_party:
            service.third_party_id = third_party.id
            repository = self.repository_factory.create_object(ServicesRepository)
            return repository.create(service, db)

    def get_services(self, db: Session) -> List[ServiceResponseDTO]:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.get_all(db)

    def get_service_by_id(self, service_id: int, db: Session) -> ServiceResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.get_by_id(service_id, db)
    
    def update_service(self, service_id: int, service: ServiceRequestDTO, db: Session) -> ServiceResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.update(service_id, service, db)
    
    def deactivate(self, service_id: int, db: Session) -> ServiceResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.deactivate(service_id, db)


class EventService:
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    def create_service(self, user_id: int, service: EventRequestDTO, db: Session) -> EventResponseDTO:

        print("user_id: ", user_id)
        third_party_service = ThirdPartyService()
        third_party = third_party_service.get_third_party_by_user_id(user_id, db)
        
        if third_party:
            service.third_party_id = third_party.id
            repository = self.repository_factory.create_object(EventRepository)
            return repository.create(service, db)

    def get_services(self, db: Session) -> List[EventResponseDTO]:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.get_all(db)

    def get_service_by_id(self, service_id: int, db: Session) -> List[EventResponseDTO]:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.get_by_id(service_id, db)
    
    def update_service(self, service_id: int, service: EventUpdateRequestDTO, db: Session) -> EventResponseDTO:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.update(service_id, service, db)
    
    def associate_event_sportman(self, user_id: int, association: AssociateSportmanEventRequestDTO, db: Session) -> EventSportmanResponseDTO:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.associate_event_sportman(user_id, association, db)
    
    def get_available_events(self, initial_date: str, final_date: str, city_id: int, db: Session) -> List[EventResponseDTO]:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.get_available_events(initial_date, final_date, city_id, db)
    
    def get_suscribed_events(self, sportman_id, initial_date, final_date, db: Session) -> List[EventResponseDTO]:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.get_suscribed_events(sportman_id, initial_date, final_date, db)
