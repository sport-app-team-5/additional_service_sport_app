from fastapi import Response
import pytest

from app.modules.services.domain.entities import Event, Sport
from app.modules.third_party.domain.entities import ThirdParty


@pytest.fixture
def sport_man_seeders(db) -> None:
    db.add(ThirdParty(user_id=1))
    db.add(Sport(name="Ciclismo", code="CI"))
    db.commit()


@pytest.fixture
def event_seeders(db) -> None:
    db.add(ThirdParty(user_id=1))
    db.add(Sport(name="Ciclismo", code="CI"))
    db.add(Event(third_party_id=1, city_id=1, sport_id=1, location="parque", date="2024-04-27T02:17", capacity=3, description="ningun", type="ROUTE"))
    db.commit()


event_data = {
    "third_party_id": 1,
    "city_id": 1,
    "sport_id": 1,
    "location": "parque",
    "date": "2024-04-27T02:17",
    "capacity": 3,
    "description": "ningun",
    "type": "ROUTE"
  }


class TestEventRouter:

    def test_create_event(self, client, headers, sport_man_seeders):
        response = create_event(client, headers, event_data)
        assert response.status_code == 201
        assert response.json()["third_party_id"] == event_data["third_party_id"]

    def test_get_event(self, client, headers, event_seeders):
        response = get_event(client, headers=headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_get_event_by_id(self, client, headers, event_seeders):
        response = get_event_by_user_id(client, 1, headers=headers)
        assert response.status_code == 200
        assert response.json()[0]["id"] == 1

    def test_update_event(self, client, event_seeders, headers):
        updated_data = event_data.copy()
        updated_data["type"] = 'EVENT'
        response = update_sportsman(client, headers, 1, updated_data)
        assert response.status_code == 200
        assert response.json()["type"] ==  'EVENT'

    def test_get_event_by_invalid_id(self, client):
        response = client.get("/api/v1/auth/events/99999")
        assert response.status_code == 401

    def test_update_event_with_invalid_id(self, client):
        response = client.put("/api/v1/auth/sport_men/99999", json=event_data)
        assert response.status_code == 404


def create_event(client, headers, event_data) -> Response:
    result = client.post("/api/v1/auth/events", headers=headers, json=event_data)
    return result


def get_event(client, headers) -> Response:
    result = client.get("/api/v1/auth/events", headers=headers)
    return result


def get_event_by_user_id(client, user_id, headers) -> Response:
    result = client.get(f"/api/v1/auth/events/{user_id}", headers=headers)
    return result


def update_sportsman(client, headers, sportsman_id, event_data) -> Response:
    result = client.put(f"/api/v1/auth/events/{sportsman_id}", headers=headers, json=event_data)
    return result
