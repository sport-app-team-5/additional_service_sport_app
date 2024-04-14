from fastapi import APIRouter
from app.api.v1.private import third_party_router as private_add_service_router
from app.api.v1.public import third_party_router as public_add_service_router

private_router = APIRouter(prefix="/auth")
private_router.include_router(private_add_service_router)


public_router = APIRouter(prefix="")
public_router.include_router(public_add_service_router)