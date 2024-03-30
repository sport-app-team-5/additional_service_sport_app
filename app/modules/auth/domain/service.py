from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import SecurityScopes
from app.seedwork.domain.services import Service
from app.seedwork.presentation.jwt import oauth2_scheme, decode_token


class AuthService(Service):
    @staticmethod
    def authorized(required_permissions: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]) -> None:
        token = decode_token(token)
        token_permissions = token.get("scopes", [])

        if not token_permissions:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not enough permissions")

        for required_permission in required_permissions.scopes:
            if required_permission not in token_permissions:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not enough permissions")
