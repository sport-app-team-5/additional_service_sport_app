from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.moduls.auth.aplication.dto import TokenResponse
from app.moduls.auth.domain.repository import AuthRepository
from app.moduls.auth.infrastructure.factories import RepositoryFactory
from app.seedwork.aplication.services import Service


class AuthService(Service):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    def authenticate_user(self, form_data: OAuth2PasswordRequestForm, db: Session) -> TokenResponse:
        repository = self.repository_factory.create_object(AuthRepository.__class__)
        return repository.authenticate(form_data, db)
