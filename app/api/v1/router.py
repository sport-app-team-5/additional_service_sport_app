from fastapi import APIRouter
from app.api.v1.private import third_party_router 

private_router = APIRouter(prefix="/aditional_service")
private_router.include_router(third_party_router)