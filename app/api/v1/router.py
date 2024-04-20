from fastapi import APIRouter
from app.api.v1.private import third_party_router as private_third_party_router, product_router
from app.api.v1.private import service_router as private_service_router
from app.api.v1.public import third_party_router as public_third_party_router

private_router = APIRouter(prefix="/auth")
private_router.include_router(private_third_party_router)
private_router.include_router(private_service_router)
private_router.include_router(product_router)


public_router = APIRouter(prefix="")
public_router.include_router(public_third_party_router)
