from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.modules.product.aplication.dto import ProductResponseDTO, ProductRequestDTO
from app.modules.product.domain.entities import Product
from app.modules.product.domain.repository import ProductRepository


class ProductRepositoryPostgres(ProductRepository):
    def create(self, entity: ProductRequestDTO, db: Session) -> ProductResponseDTO:
        try:
            product = Product(**entity.model_dump())
            db.add(product)
            db.commit()
            return product
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
