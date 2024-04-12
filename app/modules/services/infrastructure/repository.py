from typing import List
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.modules.services.aplication.dto import ServiceRequestDTO
from app.modules.services.domain.entities import Service
from app.modules.services.domain.repository import ServicesRepository

class ServicesRepositoryPostgres(ServicesRepository):
    @staticmethod
    def __validate_exist_Service(entity_id: int, db: Session) -> Service:
        service = db.query(Service).filter(Service.id == entity_id).first()
        if not service:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Service not found')

        return service

    def get_by_id(self, entity_id: int, db: Session) -> ServiceRequestDTO:
        try:
            service = self.__validate_exist_Service(entity_id, db)
            return service
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_all(self, db: Session) -> List[ServiceRequestDTO]:
        try:
            third_parties = db.query(Service).all()
            return third_parties
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def create(self, entity: Service, db: Session) -> ServiceRequestDTO:
        try:
            service = Service(id = entity.id, city_id = entity.city_id, user_id = entity.user_id)            
            db.add(service)
            db.commit()
            return service
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def update(self, entity_id: int, entity: Service, db: Session) -> ServiceRequestDTO:
        try:

            service = db.query(Service).filter(Service.id == entity_id).first()
            print ('entity_id: ', entity_id)
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

    def delete(self, entity_id: int, db: Session) -> ServiceRequestDTO:
        raise NotImplementedError
