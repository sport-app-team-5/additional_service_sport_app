from enum import Enum


class DocumentTypeEnum(str, Enum):
    ROUTE = ("ROUTE", "Ruta")
    EVENT = ("EVENT", "Evento")

    def __new__(cls, code, desc):
        obj = str.__new__(cls)
        obj._value_ = code
        obj.desc = desc
        return obj
