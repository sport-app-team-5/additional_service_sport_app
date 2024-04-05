from enum import Enum


class RoleEnum(str, Enum):
    DEPORTISTA = ("DEPO", "Deportista")
    TERCERO = ("TECE", "Tercero")
    SUPER_USUARIO = ("SUUS", "Super usuario")

    def __new__(cls, code, desc):
        obj = str.__new__(cls)
        obj._value_ = code
        obj.desc = desc
        return obj

    @classmethod
    def lookup_by_code(cls, code):
        for member in cls.__members__.values():
            if member.value == code:
                return member.desc
        return None
