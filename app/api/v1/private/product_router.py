from typing import List
from fastapi import APIRouter, Depends, Security, status
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.modules.auth.domain.enums.permission_enum import PermissionEnum
from app.modules.auth.domain.service import AuthService
from app.modules.product.aplication.dto import ProductResponseDTO, ProductRequestDTO
from app.modules.product.aplication.service import ProductService
from app.seedwork.presentation.jwt import get_current_user_id, oauth2_scheme

auth_product = AuthService()
authorized = auth_product.authorized
product_router = APIRouter(
    prefix='/products',
    tags=["Products"],
    dependencies=[Depends(oauth2_scheme)]
)


@product_router.post("", response_model=ProductResponseDTO,
                     dependencies=[Security(authorized, scopes=[PermissionEnum.CREATE_PRODUCT.code])],
                     status_code=status.HTTP_201_CREATED)
def create_product(product: ProductRequestDTO,
                   db: Session = Depends(get_db),
                   user_id: int = Depends(get_current_user_id)):
    product_service = ProductService()
    product_created = product_service.create_product(user_id, product, db)
    return product_created

@product_router.get("/get", response_model=List[ProductResponseDTO],
                    dependencies=[Security(authorized, scopes=[PermissionEnum.READ_PRODUCT.code])])
def get_all_by_user_id( db: Session = Depends(get_db)):
    product_service = ProductService()
    product_created = product_service.get_by_id(7, db)
    return product_created

@product_router.get("/{category}", response_model=List[ProductResponseDTO],
                    dependencies=[Security(authorized, scopes=[PermissionEnum.READ_PRODUCT.code])])
def get_all(category: str, db: Session = Depends(get_db)):
    product_service = ProductService()
    product_created = product_service.get_all(category, db)
    return product_created