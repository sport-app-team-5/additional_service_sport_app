from typing import List
from fastapi import APIRouter, Depends, Path, status, Security
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.modules.auth.domain.enums.permission_enum import PermissionEnum
from app.modules.auth.domain.service import AuthService
from app.modules.services.aplication.dto import EventRequestDTO, EventResponseDTO, EventUpdateRequestDTO
from app.modules.services.aplication.service import EventService
from app.seedwork.presentation.jwt import get_current_user_id, oauth2_scheme

auth_service = AuthService()
authorized = auth_service.authorized
event_router = APIRouter(
    prefix='/events',
    tags=["events"],
    dependencies=[Depends(oauth2_scheme)]
)


@event_router.post("", response_model=EventRequestDTO,
                    dependencies=[Security(authorized, scopes=[PermissionEnum.CREATE_SERVICE.code])],
                     status_code=status.HTTP_201_CREATED)
def create_service(service: EventRequestDTO,
                   db: Session = Depends(get_db),
                   user_id: int = Depends(get_current_user_id)):
    event_service = EventService()
    service_created = event_service.create_service(user_id, service, db)
    return service_created


@event_router.put("/{event_id}", response_model=EventUpdateRequestDTO,
                    dependencies=[Security(authorized, scopes=[PermissionEnum.UPDATE_SERVICE.code])],
                    status_code=status.HTTP_200_OK)
def update_service(event_id: int, service: EventUpdateRequestDTO, db: Session = Depends(get_db)):
    event_service = EventService()
    service_updated = event_service.update_service(event_id, service, db)
    return service_updated



@event_router.get("", response_model=List[EventResponseDTO],
                    dependencies=[Security(authorized, scopes=[PermissionEnum.READ_SERVICE.code])]
                    )
def get_services(db: Session = Depends(get_db)):
    event_service = EventService()
    services = event_service.get_services(db)
    return services


@event_router.get("/{sportman_plan_id}", response_model=List[EventResponseDTO],
                    dependencies=[Security(authorized, scopes=[PermissionEnum.READ_SERVICE.code])]
                    )
def get_service_by_id(sportman_plan_id: int = Path(ge=1), db: Session = Depends(get_db)):
    event_service = EventService()
    service = event_service.get_service_by_id(sportman_plan_id, db)
    return service
