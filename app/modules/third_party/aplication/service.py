from typing import List
from sqlalchemy.orm import Session
from app.modules.third_party.aplication.dto import ThirdPartyRequestDTO, ThirdPartyResponseDTO
from app.modules.third_party.domain.repository import ThirdPartyRepository
from app.modules.third_party.infrastructure.factories import RepositoryFactory
from app.seedwork.aplication.services import Service


class ThirdPartyService(Service):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    def create_third_party(self, third_party: ThirdPartyRequestDTO, db: Session) -> ThirdPartyResponseDTO:
        repository = self.repository_factory.create_object(ThirdPartyRepository.__class__)
        return repository.create(third_party, db)

    def get_third_parties(self, db: Session) -> List[ThirdPartyResponseDTO]:
        repository = self.repository_factory.create_object(ThirdPartyRepository.__class__)
        return repository.get_all(db)

    def get_third_party_by_id(self, third_party_id: int, db: Session) -> ThirdPartyResponseDTO:
        repository = self.repository_factory.create_object(ThirdPartyRepository.__class__)
        return repository.get_by_id(third_party_id, db)
