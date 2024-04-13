from abc import ABC, abstractmethod
from typing import List
from app.modules.services.aplication.dto import ServiceResponseDTO
from app.modules.services.domain.entities import Service
from app.seedwork.domain.repositories import Repository
from sqlalchemy.orm import Session


class ServicesRepository(Repository, ABC):
    @abstractmethod
    def get_by_id(self, entity_id: int, db: Session) -> ServiceResponseDTO:
        ...
    
    @abstractmethod
    def get_all(self, db: Session) -> List[ServiceResponseDTO]:
        ...

    @abstractmethod
    def create(self, entity: Service, db: Session) -> ServiceResponseDTO:
        ...

    @abstractmethod
    def update(self, entity_id: int, entity: Service, db: Session) -> ServiceResponseDTO:
        ...

    @abstractmethod
    def deactivate(self, entity_id: int, db: Session) -> ServiceResponseDTO:
        ...
        
