from dataclasses import dataclass
from typing import Optional
from pydantic import ConfigDict, BaseModel
from app.modules.services.domain.enums.service_type_enum import EventTypesEnum


class ServiceRequestDTO(BaseModel):
    third_party_id: Optional[int] = None
    is_inside_house: Optional[bool] = None
    type: str
    description: str
    is_active: bool
    cost: float

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "third_party_id": 1,
            "is_inside_house": True,
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
    is_inside_house: Optional[bool]
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
    name: Optional[str] = None
    capacity: int
    description: str
    type: EventTypesEnum
    model_config = ConfigDict(from_attributes=True)


class AssociateSportmanEventRequestDTO(BaseModel):
    sportman_id: int
    event_id: int

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "sportman_id": 1,
            "event_id": 1
        }
    })


class EventSportmanResponseDTO(BaseModel):
    id: int
    event_id: int
    sportman_id: int
    model_config = ConfigDict(from_attributes=True)

@dataclass(frozen=True)
class ScheduleAppointmentRequestDTO(BaseModel):
    sportman_id: int
    service_id: int
    injury_id: str
    sport: str
    appointment_date: str
    model_config = ConfigDict(json_schema_extra={
        "example": {
            "sportman_id": 1,
            "service_id": 1,
            "injury_id": "Notificación de prueba",
            "sport": "Ciclyn",
            "appointment_date": "2024-05-16"            
        }
    })

@dataclass(frozen=True)
class ScheduleAppointmentResponseDTO(BaseModel):
    id: int
    sportman_id: int
    service_id: int
    injury_id: str
    sport: str
    appointment_date: str
    model_config = ConfigDict(from_attributes=True)  


class NotificationRequestDTO(BaseModel):
    message: str
    status: str
    type: str
    model_config = ConfigDict(json_schema_extra={
        "example": {
            "id": 1,
            "message": "Notificación de prueba",
            "type": "IALE",
            "status": "UNREAD"            
        }
    })

class NotificationResponseDTO(BaseModel):
    id: int
    message: str
    status: str
    type: str
    model_config = ConfigDict(from_attributes=True)
