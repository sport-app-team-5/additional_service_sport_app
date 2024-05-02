from dataclasses import dataclass
from typing import Optional
from pydantic import ConfigDict, BaseModel
from app.modules.services.domain.enums.service_type_enum import EventTypesEnum


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


class EventRequestDTO(BaseModel):
    third_party_id: Optional[int] = None
    city_id: int
    sport_id: int
    location: str
    date: str
    name: str
    capacity: int
    description: str
    type: EventTypesEnum


class EventUpdateRequestDTO(BaseModel):
    third_party_id: Optional[int] = None
    city_id: Optional[int] = None
    sport_id: Optional[int] = None
    location: Optional[str] = None
    date: Optional[str] = None
    capacity: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[EventTypesEnum] = None

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "third_party_id": 1,
            "city_id": 2,
            "sport_id": 1,
            "name": "Maratón de Buenos Aires",
            "location": "Stadium",
            "date": "2022-12-31",
            "capacity": 5000,
            "description": "Servicio exclusivo para carreras de más de 4 horas",
            "type": "ROUTE"
        }
    })


class SportResponseDTO(BaseModel):
    id: int
    name: str


class EventResponseDTO(BaseModel):
    id: Optional[int] = None
    third_party_id: Optional[int] = None
    city_id: int
    sport: SportResponseDTO
    location: str
    date: str
    name: str
    capacity: int
    description: str
    type: EventTypesEnum
    model_config = ConfigDict(from_attributes=True)
