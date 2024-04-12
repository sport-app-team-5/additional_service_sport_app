import pytest
from app.modules.services.domain.enums.service_type_enum import ServiceTypesEnum


class TestServiceTypesEnum:
    def test_service_enum_values(self):
        assert ServiceTypesEnum.ACCOMPANIMENT.value == "Read user"
        assert ServiceTypesEnum.MECANIC.value == "Create service"
        assert ServiceTypesEnum.TRANSPORT.value == "Deactivate product"

    def test_permission_enum_action(self):
        assert ServiceTypesEnum.ACCOMPANIMENT.action == "Read user"
        assert ServiceTypesEnum.MECANIC.action == "Create service"
        assert ServiceTypesEnum.TRANSPORT.action == "Deactivate product"

    def test_permission_enum_code(self):
        assert ServiceTypesEnum.ACCOMPANIMENT.code == "Read user"
        assert ServiceTypesEnum.MECANIC.code == "Create service"
        assert ServiceTypesEnum.TRANSPORT.code == "Deactivate product"

    @pytest.mark.parametrize("permission", [
        ServiceTypesEnum.ACCOMPANIMENT,
        ServiceTypesEnum.MECANIC,
        ServiceTypesEnum.TRANSPORT
    ])
    def test_sercice_types_enum_instance(self, service_types):
        assert isinstance(service_types, ServiceTypesEnum)


