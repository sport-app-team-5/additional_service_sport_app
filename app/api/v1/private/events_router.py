from typing import List
from fastapi import APIRouter, Depends, Path, status, Security
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.modules.auth.domain.enums.permission_enum import PermissionEnum
from app.modules.auth.domain.service import AuthService
from app.modules.services.aplication.dto import EventRequestDTO, EventResponseDTO, EventSportmanResponseDTO, EventUpdateRequestDTO, AssociateSportmanEventRequestDTO
from app.modules.services.aplication.service import EventService
from app.seedwork.presentation.jwt import get_current_user_id, oauth2_scheme

auth_service = AuthService()
authorized = auth_service.authorized
event_router = APIRouter(
    prefix='/events',
    tags=["events"],
    dependencies=[Depends(oauth2_scheme)]
)


@event_router.get("/third_parties", response_model=List[EventResponseDTO],
                  dependencies=[Security(authorized, scopes=[PermissionEnum.READ_SERVICE.code])])
def get_events_by_third_party_id(user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    event_service = EventService()
    events = event_service.get_events_by_third_party_id(user_id, db)
    return events


@event_router.post("", response_model=EventRequestDTO,
                   dependencies=[Security(authorized, scopes=[PermissionEnum.CREATE_SERVICE.code])],
                   status_code=status.HTTP_201_CREATED)
def create_event(event: EventRequestDTO,
                 db: Session = Depends(get_db),
                 user_id: int = Depends(get_current_user_id)):
    event_event = EventService()
    event_created = event_event.create_event(user_id, event, db)
    return event_created


@event_router.put("/{event_id}", response_model=EventUpdateRequestDTO,
                  dependencies=[Security(authorized, scopes=[PermissionEnum.UPDATE_SERVICE.code])],
                  status_code=status.HTTP_200_OK)
def update_event(event_id: int, event: EventUpdateRequestDTO, db: Session = Depends(get_db)):
    event_event = EventService()
    event_updated = event_event.update_event(event_id, event, db)
    return event_updated


@event_router.get("", response_model=List[EventResponseDTO],
                  dependencies=[Security(authorized, scopes=[PermissionEnum.READ_SERVICE.code])])
def get_events(db: Session = Depends(get_db)):
    event_event = EventService()
    events = event_event.get_events(db)
    return events


@event_router.get("/{sportsman_plan_id}", response_model=List[EventResponseDTO],
                  dependencies=[Security(authorized, scopes=[PermissionEnum.READ_SERVICE.code])])
def get_event_by_id(sportsman_plan_id: int = Path(ge=1), db: Session = Depends(get_db)):
    event_event = EventService()
    event = event_event.get_event_by_id(sportsman_plan_id, db)
    return event

@event_router.post("/associate", response_model=EventSportmanResponseDTO,
                    dependencies=[Security(authorized, scopes=[PermissionEnum.UPDATE_USER.code])]
                    )
def associate_event_sportman(association: AssociateSportmanEventRequestDTO, 
                             db: Session = Depends(get_db),
                             user_id: int = Depends(get_current_user_id)
                                 ):
    event_service = EventService()
    service_created = event_service.associate_event_sportman(user_id, association, db)
    return service_created


@event_router.get("/sport/event", response_model=List[EventResponseDTO],
                        dependencies=[Security(authorized, scopes=[PermissionEnum.READ_USER.code])])
def get_available_events(initial_date: str, final_date: str, city_id: int, db: Session = Depends(get_db)):    
    event_service = EventService()
    services = event_service.get_available_events(initial_date, final_date, city_id, db)
    return services

@event_router.get("/sport/event/subscribed", response_model=List[EventResponseDTO],
                        dependencies=[Security(authorized, scopes=[PermissionEnum.READ_USER.code])])
def get_suscribed_events(sportman_id: int, initial_date: str, final_date: str, db: Session = Depends(get_db)):
    event_service = EventService()
    services = event_service.get_suscribed_events(sportman_id, initial_date, final_date, db)
    return services


