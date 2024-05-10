from typing import List
from fastapi import APIRouter, Depends, Path, Security, status, Query
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.modules.auth.domain.enums.permission_enum import PermissionEnum
from app.modules.auth.domain.service import AuthService
from app.modules.services.aplication.dto import ServiceRequestDTO, ServiceResponseDTO
from app.modules.services.aplication.service import ServicesService
from app.seedwork.presentation.jwt import get_current_user_id, oauth2_scheme

auth_service = AuthService()
authorized = auth_service.authorized
service_router = APIRouter(
    prefix='/services',
    tags=["services"],
    dependencies=[Depends(oauth2_scheme)]
)


@service_router.post("", response_model=ServiceResponseDTO,
                     dependencies=[Security(authorized, scopes=[PermissionEnum.CREATE_SERVICE.code])],
                     status_code=status.HTTP_201_CREATED)
def create_service(service: ServiceRequestDTO,
                   db: Session = Depends(get_db),
                   user_id: int = Depends(get_current_user_id)):
    services_service = ServicesService()
    service_created = services_service.create_service(user_id, service, db)
    return service_created


@service_router.put("/{service_id}", response_model=ServiceResponseDTO,
                    dependencies=[Security(authorized, scopes=[PermissionEnum.UPDATE_SERVICE.code])],
                    status_code=status.HTTP_200_OK)
def update_service(service_id: int, service: ServiceRequestDTO, db: Session = Depends(get_db)):
    services_service = ServicesService()
    service_updated = services_service.update_service(service_id, service, db)
    return service_updated


@service_router.put("/deactivate/{service_id}", response_model=ServiceResponseDTO,
                    dependencies=[Security(authorized, scopes=[PermissionEnum.UPDATE_SERVICE.code])],
                    status_code=status.HTTP_200_OK)
def deactivate_service(service_id: int, db: Session = Depends(get_db)):
    services_service = ServicesService()
    service_updated = services_service.deactivate(service_id, db)
    return service_updated


@service_router.get("", response_model=List[ServiceResponseDTO],
                    dependencies=[Security(authorized, scopes=[PermissionEnum.READ_SERVICE.code])])
def get_services(is_inside_house: bool = Query(None), db: Session = Depends(get_db)):
    services_service = ServicesService()
    services = services_service.get_services(is_inside_house, db)
    return services


@service_router.get("/{service_id}", response_model=ServiceResponseDTO,
                    dependencies=[Security(authorized, scopes=[PermissionEnum.READ_SERVICE.code])])
def get_service_by_id(service_id: int = Path(ge=1), db: Session = Depends(get_db)):
    services_service = ServicesService()
    service = services_service.get_service_by_id(service_id, db)
    return service
