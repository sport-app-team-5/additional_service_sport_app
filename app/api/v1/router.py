from fastapi import APIRouter
from app.api.v1.public import third_party_router 

public_router = APIRouter(prefix="/additional_service")
public_router.include_router(third_party_router)