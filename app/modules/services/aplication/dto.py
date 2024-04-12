from dataclasses import dataclass
from pydantic import ConfigDict, EmailStr, BaseModel


@dataclass(frozen=True)
class ServiceRequestDTO(BaseModel):
    id: int
    third_party_id: int
    type: int
    description: str
    is_active: bool
    cost: float

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "third_party_id": 1,
            "type": "",
            "description": "",
            "is_active": True,
            "cost": 25.90         
        }
    })


@dataclass(frozen=True)
class ServiceResponseDTO(BaseModel):
    id: int
    third_party_id: int
    type: int
    description: str
    is_active: bool
    cost: float
    model_config = ConfigDict(from_attributes=True)
