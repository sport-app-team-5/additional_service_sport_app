import pytest
from pytest_mock import mocker
from unittest.mock import Mock
from app.modules.third_party.infrastructure.repository import (ThirdPartyRepositoryPostgres)
from sqlalchemy.orm import Session
from app.modules.third_party.domain.entities import ThirdParty
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

@pytest.fixture
def mock_session():
    return ThirdParty(city_id=1, user_id=2)

def test_third_party_repository_update(mocker, mock_session):
    updated_city_id = 2
    updated_third_party = ThirdParty(id=1, city_id=1, user_id=2)
    db = mocker.MagicMock(Session)
    db.query().filter().first.return_value = mock_session  # Mocking the query
    repository = ThirdPartyRepositoryPostgres()
    updated_result = repository.update(1, updated_city_id, db)
    assert updated_result.city_id == updated_city_id
    db.commit.assert_called_once()  # Ensuring that commit is called

def test_third_parties_repository_get_all(mocker):
    repository = ThirdPartyRepositoryPostgres()

    db = mocker.MagicMock(Session)

    db.query.return_value.all.return_value = [
        
        ThirdParty(id=1, city_id=1, user_id=2),
        ThirdParty(id=3, city_id=2, user_id=1),
        ThirdParty(id=2, city_id=3, user_id=3),
    ]

    third_parties = repository.get_all(db)
    assert len(third_parties) == 3
    assert third_parties[0].id == 1
    assert third_parties[0].city_id == 1
    assert third_parties[0].user_id == 2
    assert third_parties[1].id == 3
    assert third_parties[1].city_id == 2
    assert third_parties[1].user_id == 1
    assert third_parties[2].id == 2
    assert third_parties[2].city_id == 3
    assert third_parties[2].user_id == 3
    
def test_third_party_repository_update(mocker):
    repository = ThirdPartyRepositoryPostgres()

    db = mocker.MagicMock(Session)
    entity = ThirdParty(id=1, city_id=1, user_id=2)
    updated_entity = repository.update(1, entity, db)
    assert updated_entity.city_id == 1
    assert updated_entity.user_id == 2
    db.query.assert_called_once()
    db.commit.assert_called_once()

def test_third_party_repository_create(mocker):
    repository = ThirdPartyRepositoryPostgres()
    db = mocker.MagicMock(Session)
    entity = ThirdParty(id=4, city_id=1, user_id=4)
    created_entity = repository.create(entity, db)
    assert created_entity.id == 4
    assert created_entity.city_id == 1
    assert created_entity.user_id == 4
    db.commit.assert_called_once()

def test_third_party_repository_create(mocker):
    repository = ThirdPartyRepositoryPostgres()
    db = mocker.MagicMock(Session)
    entity = ThirdParty(id=4, city_id=1, user_id=4)
    db.add.side_effect = SQLAlchemyError

    with pytest.raises(HTTPException) as exc_info:
        repository.create(entity, db)
    assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


def test_third_party_repository_get_by_id(mocker):
    repository = ThirdPartyRepositoryPostgres()

    third_party_object = ThirdParty(id=5, city_id=1, user_id=4)
    db = mocker.MagicMock()

    db.query(ThirdParty).filter.return_value.first.return_value = third_party_object

    third_party = repository.get_by_id(5, db)
    assert third_party.id == 5