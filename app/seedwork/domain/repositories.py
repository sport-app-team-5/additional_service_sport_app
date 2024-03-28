from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session
from .entities import Entity


class Repository(ABC):
    @abstractmethod
    def get_by_id(self, entity_id: int, db: Session) -> Entity:
        ...

    @abstractmethod
    def get_all(self, db: Session) -> List[Entity]:
        ...

    @abstractmethod
    def create(self, entity: Entity, db: Session) -> Entity:
        ...

    @abstractmethod
    def update(self, entity_id: int, entity: Entity, db: Session) -> Entity:
        ...

    @abstractmethod
    def delete(self, entity_id: int, db: Session) -> Entity:
        ...
    