import pytest
from app.modules.auth.domain.enums.permission_enum import PermissionEnum
from app.modules.auth.domain.enums.role_enum import RoleEnum


class TestPermissionEnum:
    def test_permission_enum_values(self):
        assert PermissionEnum.READ_USER.value == "Read user"
        assert PermissionEnum.CREATE_SERVICE.value == "Create service"
        assert PermissionEnum.DEACTIVATE_PRODUCT.value == "Deactivate product"

    def test_permission_enum_action(self):
        assert PermissionEnum.READ_USER.action == "read"
        assert PermissionEnum.UPDATE_SERVICE.action == "update"
        assert PermissionEnum.DEACTIVATE_EVENT.action == "deactivate"

    def test_permission_enum_code(self):
        assert PermissionEnum.READ_USER.code == "RUSO"
        assert PermissionEnum.UPDATE_PRODUCT.code == "UPRO"
        assert PermissionEnum.CREATE_EVENT.code == "CEVE"

    @pytest.mark.parametrize("permission", [
        PermissionEnum.READ_USER,
        PermissionEnum.UPDATE_SERVICE,
        PermissionEnum.DEACTIVATE_PRODUCT
    ])
    def test_permission_enum_instance(self, permission):
        assert isinstance(permission, PermissionEnum)




class TestRoleEnum:
    def test_role_enum_values(self):
        assert RoleEnum.DEPORTISTA.value == "DEPO"
        assert RoleEnum.TERCERO.value == "TECE"
        assert RoleEnum.SUPER_USUARIO.value == "SUUS"

    def test_role_enum_description(self):
        assert RoleEnum.DEPORTISTA.desc == "Deportista"
        assert RoleEnum.TERCERO.desc == "Tercero"
        assert RoleEnum.SUPER_USUARIO.desc == "Super usuario"

    def test_role_enum_lookup_by_code(self):
        assert RoleEnum.lookup_by_code("DEPO") == "Deportista"
        assert RoleEnum.lookup_by_code("TECE") == "Tercero"
        assert RoleEnum.lookup_by_code("SUUS") == "Super usuario"
        assert RoleEnum.lookup_by_code("INVALID_CODE") is None

    def test_role_enum_instance(self):
        for role in RoleEnum:
            assert isinstance(role, RoleEnum)