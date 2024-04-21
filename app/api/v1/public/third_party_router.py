from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.modules.auth.domain.service import AuthService
from app.modules.third_party.aplication.dto import ThirdPartyRequestDTO, ThirdPartyResponseDTO
from app.modules.third_party.aplication.service import ThirdPartyService

auth_service = AuthService()
authorized = auth_service.authorized
third_party_router = APIRouter(
    prefix='/third_parties',
    tags=["ThirdParty"]
)


@third_party_router.post("", response_model=ThirdPartyResponseDTO
    , status_code=status.HTTP_201_CREATED)
async def create_third_party(third_party: ThirdPartyRequestDTO, db: Session = Depends(get_db)):
    third_party_service = ThirdPartyService()
    third_party_created = third_party_service.create_third_party(third_party, db)
    return third_party_created
