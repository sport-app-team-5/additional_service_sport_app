from typing import List
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.modules.product.aplication.dto import ProductResponseDTO, ProductRequestDTO
from app.modules.product.domain.entities import Product
from app.modules.product.domain.repository import ProductRepository
from app.modules.third_party.domain.entities import ThirdParty


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
        
    def get_by_id(self, user_id: int, db: Session) -> List[ProductResponseDTO]:
        try:
            third_party = db.query(ThirdParty).filter(ThirdParty.user_id == user_id).one_or_none()
            if not third_party:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ThirdParty not found')
            return db.query(Product).filter(Product.third_party_id == third_party.id).all()
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    def get_all(self, category, db: Session) -> List[ProductResponseDTO]:
        try:
            print(category)
            if(category == 'all'):
                return db.query(Product).filter(Product.is_active == True).all()
            return db.query(Product).filter(Product.is_active == True, Product.category == category).all()
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
