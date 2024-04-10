from typing import List
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.modules.third_party.aplication.dto import ThirdPartyRequestDTO
from app.modules.third_party.domain.entities import ThirdParty
from app.modules.third_party.domain.repository import ThirdPartyRepository

class ThirdPartyRepositoryPostgres(ThirdPartyRepository):
    @staticmethod
    def __validate_exist_third_party(entity_id: int, db: Session) -> ThirdParty:
        third_party = db.query(ThirdParty).filter(ThirdParty.id == entity_id).first()
        if not third_party:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ThirdParty not found')

        return third_party

    def get_by_id(self, entity_id: int, db: Session) -> ThirdPartyRequestDTO:
        try:
            third_party = self.__validate_exist_third_party(entity_id, db)
            return third_party
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_by_user_id(self, entity_user_id: int, db: Session) -> ThirdPartyRequestDTO:
        try:
            third_party = db.query(ThirdParty).filter(ThirdParty.user_id == entity_user_id).first()
            return third_party
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))        

    def get_all(self, db: Session) -> List[ThirdPartyRequestDTO]:
        try:
            third_parties = db.query(ThirdParty).all()
            return third_parties
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def create(self, entity: ThirdParty, db: Session) -> ThirdPartyRequestDTO:
        try:
            third_party = self.get_by_user_id(entity.user_id, db)
            
            if not third_party:
                third_party = ThirdParty(user_id = entity.user_id)            
                db.add(third_party)
                db.commit()
                return third_party
            else:
                raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail=str(e))    
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def update(self, entity_id: int, entity: ThirdParty, db: Session) -> ThirdPartyRequestDTO:
        try:

            third_party = db.query(ThirdParty).filter(ThirdParty.id == entity_id).first()
            if third_party:
                try:
                    third_party.user_id = entity.user_id
                    db.commit()
                    return third_party
                except Exception as e:
                    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="User was not provided")    
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Third party not found")    
            
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def delete(self, entity_id: int, db: Session) -> ThirdPartyRequestDTO:
        raise NotImplementedError
