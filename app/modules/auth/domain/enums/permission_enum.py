from enum import Enum


class PermissionEnum(str, Enum):
    # Acciones y permisos relacionados con los usuarios
    READ_USER = ("Read user", "read", "RUSO")
    UPDATE_USER = ("Update user", "update", "UUSO")
    DEACTIVATE_USER = ("Delete user", "deactivate", "DUSO")
    MANAGE_SESSION = ("Manage session", "manage", "MASE")

    # Acciones y permisos relacionados con los servicios
    CREATE_SERVICE = ("Create service", "create", "CSER")
    READ_SERVICE = ("Read service", "read", "RSER")
    UPDATE_SERVICE = ("Update service", "update", "USER")
    DEACTIVATE_SERVICE = ("Deactivate service", "deactivate", "DSER")

    # Acciones y permisos relacionados con los productos
    CREATE_PRODUCT = ("Create product", "create", "CPRO")
    READ_PRODUCT = ("Read product", "read", "RPRO")
    UPDATE_PRODUCT = ("Update product", "update", "UPRO")
    DEACTIVATE_PRODUCT = ("Deactivate product", "deactivate", "DPRO")

    # Acciones y permisos relacionados con los eventos
    CREATE_EVENT = ("Create event", "create", "CEVE")
    READ_EVENT = ("Read event", "read", "REVE")
    UPDATE_EVENT = ("Update event", "update", "UEVE")
    DEACTIVATE_EVENT = ("Deactivate event", "deactivate", "DEVE")

    def __new__(cls, value, action, code):
        obj = str.__new__(cls)
        obj._value_ = value
        obj.action = action
        obj.code = code
        return obj
