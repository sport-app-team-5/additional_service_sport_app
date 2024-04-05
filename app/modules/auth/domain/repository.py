from abc import ABC, abstractmethod
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.seedwork.domain.repositories import Repository


class AuthRepository(Repository, ABC):
    @abstractmethod
    def authenticate(self, form_data: OAuth2PasswordRequestForm, db: Session):
        pass
