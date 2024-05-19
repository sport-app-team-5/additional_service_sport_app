from typing import List
from fastapi import HTTPException, status
from sqlalchemy import exists
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.modules.services.aplication.dto import EventResponseDTO, EventSportmanResponseDTO, ScheduleAppointmentResponseDTO, ServiceResponseDTO
from app.modules.services.domain.entities import EventSportman, Service, Event, ServiceSportman
from app.modules.services.domain.enums.service_type_enum import ServiceTypesEnum
from app.modules.services.domain.repository import EventRepository, ServicesRepository
from app.modules.services.domain.entities import Notification
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from typing import List


class ServicesRepositoryPostgres(ServicesRepository):
    @staticmethod
    def __validate_exist_Service(entity_id: int, db: Session) -> Service:
        service = db.query(Service).filter(Service.id == entity_id).first()
        if not service:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Service not found')

        return service

    def get_by_id(self, entity_id: int, db: Session) -> ServiceResponseDTO:
        try:
            service = self.__validate_exist_Service(entity_id, db)            
            return service
            
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    def get_by_type(self, service_type: str, db: Session) -> List[ServiceResponseDTO]:
        try:
            services = db.query(Service).filter(Service.type == service_type).all()
            if services is not None:
                return services
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Service not found by type {service_type}")
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_all_in_house(self, is_inside_house: bool, db: Session) -> List[ServiceResponseDTO]:
        try:
            if is_inside_house is not None:
                services = db.query(Service).filter(Service.is_inside_house == is_inside_house,
                                                    Service.type == ServiceTypesEnum.ACCOMPANIMENT.value).all()
            else:
                services = db.query(Service).all()
            return services
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    def get_all(self, third_party_id: int, db: Session) -> List[ServiceResponseDTO]:
        try:
            if third_party_id is not None:
                services = db.query(Service).filter(Service.third_party_id == third_party_id).all()            
                return services
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))    

    def create(self, entity: Service, db: Session) -> ServiceResponseDTO:
        try:
            service = Service(third_party_id=entity.third_party_id, type=entity.type, description=entity.description,
                              is_active=entity.is_active, cost=entity.cost, is_inside_house=entity.is_inside_house)
            db.add(service)
            db.commit()
            return service
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def update(self, entity_id: int, entity: Service, db: Session) -> ServiceResponseDTO:
        try:
            service = db.query(Service).filter(Service.id == entity_id).one_or_none()

            if service:
                service.cost = entity.cost
                service.description = entity.description
                service.is_active = entity.is_active
                service.type = entity.type
                db.commit()
                return service
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def deactivate(self, entity_id: int, db: Session) -> ServiceResponseDTO:
        try:
            service = db.query(Service).filter(Service.id == entity_id).one_or_none()

            if service:
                service.is_active = False
                db.commit()
                return service
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    def create_scheduler_appointment(self, entity: ServiceSportman, db: Session):
        try:
            service_sportman = ServiceSportman(service_id = entity.service_id, sportman_id = entity.sportman_id, sport = entity.sport, 
                                               injury_id = entity.injury_id, appointment_date = entity.appointment_date)
            
            db.add(service_sportman)
            db.commit()
            
            return service_sportman
            
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    def get_schedule_appointments(self, sportman_id: int, db: Session) -> List[ScheduleAppointmentResponseDTO]:
        try:
            result = []
            service_sportman = db.query(ServiceSportman).filter(ServiceSportman.sportman_id == sportman_id).all()            
            if service_sportman:
                for ss in service_sportman:
                    service_name = db.query(Service).filter(Service.id == ss.service_id).first().description
                    sport = ss.sport
                    appointment_date = ss.appointment_date
                    
                    result.append(ScheduleAppointmentResponseDTO(id=ss.id, sportman_id=ss.sportman_id, service_name=service_name, injury_id=ss.injury_id, sport=sport, appointment_date=appointment_date))
                return result
            else:
                return result          
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))    

    def create_notification(self, entity: Notification, db: Session) -> Notification:
        try:
            notification = Notification(status=entity.status, type=entity.type, message=entity.message)
            db.add(notification)
            db.commit()
            return notification
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_notification_by_status_and_type(self, status: str, type: str, db: Session) -> List[Notification]:
        try:
            notifications = db.query(Notification).filter(Notification.status == status, Notification.type == type).all()
            return notifications
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def update_notification_status(self, type: str, db: Session):
        status = "READED"
        try:
            notifications = db.query(Notification).filter(Notification.type == type).all()
            if notifications:
                for notification in notifications:              
                    notification.status = status
                    db.commit()
                return []
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


class EventRepositoryPostgres(EventRepository):
    @staticmethod
    def __validate_exist_Service(entity_id: int, db: Session) -> List[Event]:
        service = db.query(Event).filter(Event.third_party_id == entity_id).all()
        if not service:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event not found')

        return service

    def get_by_id(self, entity_id: int, db: Session) -> List[EventResponseDTO]:
        try:
            service = self.__validate_exist_Service(entity_id, db)
            return service
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_all(self, db: Session) -> List[EventResponseDTO]:
        try:
            third_parties = db.query(Event).all()
            return third_parties
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def create(self, entity: Event, db: Session) -> EventResponseDTO:
        try:
            service = Event(third_party_id=entity.third_party_id, city_id=entity.city_id, sport_id=entity.sport_id,
                            location=entity.location, date=entity.date, capacity=entity.capacity,
                            description=entity.description, type=entity.type.value, name=entity.name)
            db.add(service)
            db.commit()
            return service
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def update(self, entity_id: int, entity: Event, db: Session) -> EventResponseDTO:
        try:
            service = db.query(Event).filter(Event.id == entity_id).one_or_none()

            if service:
                self.__update_event_attributes(service, entity)

                db.commit()
                return service
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        

    def __update_event_attributes(self, service: Event, entity: Event):
        if entity.third_party_id:
            service.third_party_id = entity.third_party_id
        if entity.city_id:
            service.city_id = entity.city_id
        if entity.sport_id:
            service.sport_id = entity.sport_id
        if entity.location:
            service.location = entity.location
        if entity.date:
            service.date = entity.date
        if entity.capacity:
            service.capacity = entity.capacity
        if entity.description:
            service.description = entity.description
        if entity.type:
            service.type = entity.type.value


    def associate_event_sportman(self, entity_id: int, entity: EventSportman, db: Session) -> EventSportmanResponseDTO:
        try:
            event_sportman = EventSportman(event_id = entity.event_id, sportman_id = entity.sportman_id)
            db.add(event_sportman)
            db.commit()
            return event_sportman
        
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
                

    def get_available_events(self, initial_date: str, final_date: str, city_id: int, db: Session) -> List[EventResponseDTO]:
        try:
            available_events = db.query(Event).filter(
                    Event.date >= initial_date,
                    Event.date <= final_date,
                    #Event.city_id == city_id,
                    ~exists().where(EventSportman.event_id == Event.id)             
            ).all()

            if available_events: 
                return available_events
            else:
                return []          
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    def get_suscribed_events(self, sportman_id: int, initial_date: str, final_date: str, db: Session) -> List[EventResponseDTO]:
        try:
            suscribed_events = db.query(Event).filter(
                    Event.date >= initial_date,
                    Event.date <= final_date,
                    exists().where(EventSportman.event_id == Event.id and EventSportman.sportman_id == sportman_id)
            ).all()

            if suscribed_events: 
                return suscribed_events
            else:
                return []
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))        
        
    def get_by_third_party_id(self, third_party_id: int, db: Session) -> List[EventResponseDTO]:
        try:
            events = db.query(Event).filter(Event.third_party_id == third_party_id).all()
            return events
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
