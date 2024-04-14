from dataclasses import dataclass
from typing import Optional
from pydantic import ConfigDict, BaseModel


# @dataclass(frozen=True)
class ServiceRequestDTO(BaseModel):
    third_party_id: Optional[int] = None
    type: str
    description: str
    is_active: bool
    cost: float

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "third_party_id": 1,
            "type": "TRANSPORT",
            "description": "Servicio exclusivo para carreras de más de 4 horas",
            "is_active": True,
            "cost": 25.90         
        }
    })


@dataclass(frozen=True)
class ServiceResponseDTO(BaseModel):
    id: int
    third_party_id: int
    type: str
    description: str
    is_active: bool
    cost: float
    model_config = ConfigDict(from_attributes=True)
