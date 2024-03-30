from enum import Enum


class PermissionEnum(str, Enum):
    READ_USER = ("Read user", "read", "RUSO")
    CREATE_USER = ("Create user", "create", "CUSO")
    UPDATE_USER = ("Update user", "update", "UUSO")
    DELETE_USER = ("Delete user", "delete", "DUSO")

    def __new__(cls, value, action, code):
        obj = str.__new__(cls)
        obj._value_ = value
        obj.action = action
        obj.code = code
        return obj
