from typing import List
from fastapi import APIRouter, Depends, Path, Security, status
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.modules.auth.domain.enums.permission_enum import PermissionEnum
from app.modules.auth.domain.service import AuthService
from app.modules.services.aplication.dto import ServiceRequestDTO, ServiceResponseDTO
from app.modules.services.aplication.service import ServicesService
from app.seedwork.presentation.jwt import oauth2_scheme

auth_service = AuthService()
authorized = auth_service.authorized
service_router = APIRouter(
    prefix='/services',
    tags=["services"],
    #dependencies=[Depends(oauth2_scheme)]
)

@service_router.post("", response_model=ServiceRequestDTO
                        #  ,dependencies=[Security(authorized, scopes=[PermissionEnum.READ_USER.code])]
                         , status_code=status.HTTP_201_CREATED)
async def create_service(service: ServiceResponseDTO, db: Session = Depends(get_db)):
    services_service = ServicesService()
    service_created = services_service.create_service(service, db)
    return service_created

@service_router.get("", response_model=List[ServiceRequestDTO]
                        # ,dependencies=[Security(authorized, scopes=[PermissionEnum.READ_USER.code])]
                        )
async def get_services(db: Session = Depends(get_db)):
    services_service = ServicesService()
    services = services_service.get_services(db)
    return services


@service_router.get("/{service_id}", response_model=ServiceRequestDTO
                        # ,dependencies=[Security(authorized, scopes=[PermissionEnum.READ_USER.code])]
                        )
async def get_service_by_id(service_id: int = Path(ge=1), db: Session = Depends(get_db)):
    services_service = ServicesService()
    service = services_service.get_service_by_id(service_id, db)
    return service


@service_router.get("/user/{user_id}", response_model=ServiceRequestDTO
                        # ,dependencies=[Security(authorized, scopes=[PermissionEnum.READ_USER.code])]
                        )
async def get_service_by_user_id(user_id: int = Path(ge=1), db: Session = Depends(get_db)):
    services_service = ServicesService()
    service = services_service.get_service_by_user_id(user_id, db)
    return service
