from abc import ABC, abstractmethod
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


class AuthRepository(ABC):
    @abstractmethod
    def authenticate(self, form_data: OAuth2PasswordRequestForm, db: Session):
        pass
