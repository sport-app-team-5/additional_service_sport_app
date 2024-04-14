import uuid
from typing import Any
from typing import Generator
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from app.config.db import Base, get_db
from app.main import app
from app.modules.auth.domain.service import AuthService
from app.seedwork.presentation.jwt import get_current_user_id

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def __app() -> Generator[FastAPI, Any, None]:
    Base.metadata.create_all(engine)
    yield app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db() -> Generator[SessionTesting, Any, None]: # type: ignore
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(__app: FastAPI, db: SessionTesting) -> Generator[TestClient, Any, None]: # type: ignore
    def __get_test_db():
        yield db

    def __get_current_user_id():
        return 1    

    def __authorized():
        pass    

    # noinspection PyUnresolvedReferences
    app.dependency_overrides.update({get_db: __get_test_db, AuthService.authorized: __authorized, get_current_user_id: __get_current_user_id})

    with TestClient(__app) as client:
        yield client


@pytest.fixture
def headers() -> dict:
    uuid_token = uuid.uuid4()
    return {"Authorization": f"Bearer {uuid_token}"}
