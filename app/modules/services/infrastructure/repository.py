from typing import List
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.modules.services.aplication.dto import EventResponseDTO, ServiceResponseDTO
from app.modules.services.domain.entities import Service, Event
from app.modules.services.domain.repository import EventRepository, ServicesRepository


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

    def get_all(self, db: Session) -> List[ServiceResponseDTO]:
        try:
            third_parties = db.query(Service).all()
            return third_parties
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def create(self, entity: Service, db: Session) -> ServiceResponseDTO:
        try:
            service = Service(third_party_id=entity.third_party_id, type=entity.type, description=entity.description,
                              is_active=entity.is_active, cost=entity.cost)
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
                            description=entity.description, type=entity.type.value)
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
