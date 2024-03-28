from app.modules.third_party.aplication.service import ThirdPartyService
from unittest.mock import MagicMock
from app.modules.third_party.aplication.dto import ThirdPartyRequestDTO, ThirdPartyResponseDTO


class MockRepositoryFactory:
    def create_object(self, repository):
        return MagicMock()

class MockSession:
    pass

def create_third_party():
    service = ThirdPartyService()
    service._repository_factory = MockRepositoryFactory()

    model = ThirdPartyRequestDTO(id=6, city_id=2, user_id=1)
    db = MockSession()

    assert service.start(model, db) is not None

def get_third_parties():
    service = ThirdPartyService()
    service._repository_factory = MockRepositoryFactory()

    model = ThirdPartyRequestDTO(id=6, city_id=2, user_id=1)
    db = MockSession()

    assert service.get_third_parties(model, db) is not None

def get_third_party_by_id():
    service = ThirdPartyService()
    service._repository_factory = MockRepositoryFactory()

    model = ThirdPartyRequestDTO(id=6, city_id=2, user_id=1)
    db = MockSession()

    assert service.register(model, db) is not None
