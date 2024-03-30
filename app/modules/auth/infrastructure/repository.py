from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.moduls.auth.aplication.dto import TokenResponse
from app.moduls.auth.domain.repository import AuthRepository
from app.moduls.user.domain.entities import User
from app.seedwork.presentation.utils import verify_password
from app.seedwork.presentation.jwt import create_access_token


class AuthRepositoryPostgres(AuthRepository):
    def authenticate(self, form_data: OAuth2PasswordRequestForm, db: Session) -> TokenResponse:
        try:
            user = db.query(User).filter(User.email == form_data.username).first()
            if not user.is_active or not verify_password(form_data.password, user.password):
                raise HTTPException(status_code=400, detail="Incorrect username or password")

            permissions = user.role.permissions
            permission_codes = [permission.permission.code for permission in permissions]
            access_token = create_access_token(data={
                "sub": user.email,
                "role": user.role.code,
                "scopes": permission_codes
            })
            return TokenResponse(access_token=access_token, token_type="Bearer")
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
