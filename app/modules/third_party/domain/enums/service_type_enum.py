from enum import Enum


class DocumentTypeEnum(str, Enum):
    TRANSPORT = ("TRANSPORT", "Tramsporte")
    ACCOMPANIMENT = ("ACCOMPANIMENT", "Acompañamiento")
    MECANIC = ("MECANIC", "Mecanico")    

    def __new__(cls, code, desc):
        obj = str.__new__(cls)
        obj._value_ = code
        obj.desc = desc
        return obj
