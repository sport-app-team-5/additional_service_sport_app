from enum import Enum


class ServiceTypesEnum(str, Enum):
    TRANSPORT = ("TRANSPORT", "Transporte")
    ACCOMPANIMENT = ("ACCOMPANIMENT", "Acompañamiento")
    MECANIC = ("MECANIC", "Mecánica")

    def __new__(cls, code, desc):
        obj = str.__new__(cls)
        obj._value_ = code
        obj.desc = desc
        return obj
