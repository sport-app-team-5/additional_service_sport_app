import pytest
from app.modules.services.aplication.service import ServicesService
from app.modules.services.infrastructure.exceptions import ImplementationNotExistForFabricTypeException


class NonRepository:
    pass


class TestThirdPartyException:
    def test_factory_third_party(self):
        third_party_service = ServicesService()

        with pytest.raises(ImplementationNotExistForFabricTypeException) as exc_info:
            third_party_service.repository_factory.create_object(NonRepository)

        assert 'There is no implementation for the repository with the given type' in str(exc_info.value)
