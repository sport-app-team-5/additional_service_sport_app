import pytest
from app.modules.third_party.aplication.service import ThirdPartyService
from app.modules.third_party.infrastructure.exceptions import ImplementationNotExistForFabricTypeException


class NonRepository:
    pass


class TestThirdPartyException:
    def test_factory_third_party(self):
        third_party_service = ThirdPartyService()

        with pytest.raises(ImplementationNotExistForFabricTypeException) as exc_info:
            third_party_service.repository_factory.create_object(NonRepository)

        assert 'There is no implementation for the repository with the given type' in str(exc_info.value)
