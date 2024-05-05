from typing import List
from sqlalchemy.orm import Session
from app.modules.services.aplication.dto import (EventRequestDTO, EventResponseDTO, EventUpdateRequestDTO,
                                                 ServiceRequestDTO, ServiceResponseDTO)
from app.modules.services.domain.repository import EventRepository, ServicesRepository
from app.modules.services.infrastructure.factories import RepositoryFactory
from app.modules.third_party.aplication.service import ThirdPartyService


class ServicesService:
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    def create_service(self, user_id: int, service: ServiceRequestDTO, db: Session) -> ServiceResponseDTO:
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

    def create_event(self, user_id: int, event: EventRequestDTO, db: Session) -> EventResponseDTO:
        third_party_event = ThirdPartyService()
        third_party = third_party_event.get_third_party_by_user_id(user_id, db)
        
        if third_party:
            event.third_party_id = third_party.id
            repository = self.repository_factory.create_object(EventRepository)
            return repository.create(event, db)

    def get_events(self, db: Session) -> List[EventResponseDTO]:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.get_all(db)

    def get_event_by_id(self, event_id: int, db: Session) -> List[EventResponseDTO]:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.get_by_id(event_id, db)
    
    def update_event(self, event_id: int, event: EventUpdateRequestDTO, db: Session) -> EventResponseDTO:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.update(event_id, event, db)

    def get_events_by_third_party_id(self, user_id: int, db: Session) -> List[EventResponseDTO]:
        third_party_event = ThirdPartyService()
        third_party = third_party_event.get_third_party_by_user_id(user_id, db)

        if third_party:
            repository = self.repository_factory.create_object(EventRepository)
            return repository.get_by_third_party_id(third_party.id, db)
