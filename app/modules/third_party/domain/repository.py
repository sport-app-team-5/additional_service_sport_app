from abc import ABC, abstractmethod
from typing import List
from app.modules.third_party.aplication.dto import ThirdPartyRequestDTO
from app.modules.third_party.domain.entities import ThirdParty
from app.seedwork.domain.repositories import Repository
from sqlalchemy.orm import Session


class ThirdPartyRepository(Repository, ABC):
    @abstractmethod
    def get_by_id(self, entity_id: int, db: Session) -> ThirdPartyRequestDTO:
        ...

    @abstractmethod
    def get_by_user_id(self, entity_user_id: int, db: Session) -> ThirdPartyRequestDTO:
        ...
    
    @abstractmethod
    def get_all(self, db: Session) -> List[ThirdPartyRequestDTO]:
        ...

    @abstractmethod
    def create(self, entity: ThirdParty, db: Session) -> ThirdPartyRequestDTO:
        ...
