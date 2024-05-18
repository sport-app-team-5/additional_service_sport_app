from typing import List
from sqlalchemy.orm import Session
from app.modules.services.aplication.dto import (AssociateSportmanEventRequestDTO, EventRequestDTO, EventResponseDTO, EventSportmanResponseDTO, EventUpdateRequestDTO, NotificationRequestDTO, NotificationResponseDTO, ScheduleAppointmentRequestDTO, ScheduleAppointmentResponseDTO,
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
        if service.is_inside_house is None:
            service.is_inside_house = False
        third_party = third_party_service.get_third_party_by_user_id(user_id, db)
        
        if third_party:
            service.third_party_id = third_party.id
            repository = self.repository_factory.create_object(ServicesRepository)
            return repository.create(service, db)

    def get_services(self, is_inside_house: bool, user_id: int, db: Session) -> List[ServiceResponseDTO]:
        third_party_service = ThirdPartyService()
        third_party = third_party_service.get_third_party_by_user_id(user_id, db)
        
        repository = self.repository_factory.create_object(ServicesRepository)
        if third_party:
            services = repository.get_all(third_party.id, db)
        else :
            services = repository.get_all(is_inside_house, db)

        return services

    def get_service_by_id(self, service_id: int, db: Session) -> ServiceResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.get_by_id(service_id, db)
    
    def get_service_by_type(self, type: str, db: Session) -> List[ServiceResponseDTO]:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.get_by_type(type, db)
    
    def update_service(self, service_id: int, service: ServiceRequestDTO, db: Session) -> ServiceResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.update(service_id, service, db)
    
    def deactivate(self, service_id: int, db: Session) -> ServiceResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.deactivate(service_id, db)
    
    def create_schedule_appointment(self, appointment: ScheduleAppointmentRequestDTO, db: Session):
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.create_scheduler_appointment(appointment, db)
    
    def get_schedule_appointments(self, sportman_id: int, db: Session) -> List[ScheduleAppointmentResponseDTO]:
        repository = self.repository_factory.create_object(ServicesRepository)        
        appointments = repository.get_schedule_appointments(sportman_id, db)
        return appointments
    
    def create_notification(self, entity: NotificationRequestDTO, db: Session) -> NotificationResponseDTO:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.create_notification(entity, db)

    def get_notification_by_status_and_type(self, status: str, type: str, db: Session) -> List[NotificationResponseDTO]:
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.get_notification_by_status_and_type(status, type, db)

    def update_notification_status(self, status: str, db: Session):
        repository = self.repository_factory.create_object(ServicesRepository)
        return repository.update_notification_status(status, db)


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
            services_service = ServicesService()
            notification = NotificationRequestDTO(message=event.name, type="ENEW", status="UNREAD")
            services_service.create_notification(notification, db)
            return repository.create(event, db)

    def get_events(self, user_id: int, db: Session) -> List[EventResponseDTO]:
        third_party_service = ThirdPartyService()
        third_party = third_party_service.get_third_party_by_user_id(user_id, db)
        
        repository = self.repository_factory.create_object(EventRepository)

        if third_party:        
            events = repository.get_by_third_party_id(third_party.id, db)
        else:   
            events = repository.get_all(db)
        
        return events

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


    def associate_event_sportman(self, user_id: int, association: AssociateSportmanEventRequestDTO, db: Session) -> EventSportmanResponseDTO:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.associate_event_sportman(user_id, association, db)
    
    def get_available_events(self, initial_date: str, final_date: str, city_id: int, db: Session) -> List[EventResponseDTO]:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.get_available_events(initial_date, final_date, city_id, db)
    
    def get_suscribed_events(self, sportman_id, initial_date, final_date, db: Session) -> List[EventResponseDTO]:
        repository = self.repository_factory.create_object(EventRepository)
        return repository.get_suscribed_events(sportman_id, initial_date, final_date, db)