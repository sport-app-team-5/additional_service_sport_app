import pytest
from app.modules.services.domain.enums.service_type_enum import ServiceTypesEnum


class TestServiceTypesEnum:
    def test_service_type_enum_code(self):
        assert ServiceTypesEnum.ACCOMPANIMENT.value == "ACCOMPANIMENT"
        assert ServiceTypesEnum.MECANIC.value == "MECANIC"
        assert ServiceTypesEnum.TRANSPORT.value == "TRANSPORT"

    def test_service_type_enum_desc(self):
        assert ServiceTypesEnum.ACCOMPANIMENT.desc == "Acompañamiento"
        assert ServiceTypesEnum.MECANIC.desc == "Mecánica"
        assert ServiceTypesEnum.TRANSPORT.desc == "Transporte"

    @pytest.mark.parametrize("service_types", [
        ServiceTypesEnum.ACCOMPANIMENT,
        ServiceTypesEnum.MECANIC,
        ServiceTypesEnum.TRANSPORT
    ])
    def test_sercice_types_enum_instance(self, service_types):
        assert isinstance(service_types, ServiceTypesEnum)


