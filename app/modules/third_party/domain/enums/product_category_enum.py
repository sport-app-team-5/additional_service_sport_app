from enum import Enum


class DocumentTypeEnum(str, Enum):
    VEGETABLES = ("VEGETABLES", "Verduras")
    DAIRY_PRODUCTS = ("DAIRY_PRODUCTS", "Productos Lácteos")
    MEATS_BIRDS = ("MEATS_BIRDS", "Carnes de Aves")
    FISH_SEAFOOD = ("FISH_SEAFOOD", "Pescados y Mariscos")
    GRAIN_CEREALS = ("GRAIN_CEREALS", "Cereales de Grano")
    LEGUMES_DRIED_FRUITS = ("LEGUMES_DRIED_FRUITS", "Legumbres y Frutos Secos")
    BAKED_GOODS = ("BAKED_GOODS", "Productos Horneados")
    DRINKS = ("DRINKS", "Bebidas")

    def __new__(cls, code, desc):
        obj = str.__new__(cls)
        obj._value_ = code
        obj.desc = desc
        return obj
