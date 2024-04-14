import pytest
from httpx import Response
from app.modules.third_party.domain.entities import ThirdParty


@pytest.fixture
def third_party_seeders(db) -> None:
    db.commit()


@pytest.fixture
def third_party_data() -> dict:
    return {
        "user_id": 1
    }

@pytest.fixture
def third_party_data_invalid() -> dict:
    return {
    }


class TestCreateThirdPartyRouter:
    def test_create_third_party(self, client, headers,  third_party_data):
        third_party_created = create_third_party(client, third_party_data, headers)
        third_party_created_json = third_party_created.json()

        assert third_party_created.status_code == 201
        assert "id" in third_party_created_json
        assert third_party_data['user_id'] == third_party_created_json["user_id"]

    def test_create_third_party_with_invalid_data(self, client, headers, third_party_data):
        third_party_data_fail = third_party_data["user_id"] = "invalid"
        response = create_third_party(client, third_party_data_fail, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json

    def test_create_third_party_with_no_user(self, client, headers, third_party_data):
        
        third_party_data_fail = third_party_data["user_id"] = None

        response = create_third_party(client, third_party_data_fail, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json

    def test_create_third_party_with_null_data(self, client, headers):
        response = create_third_party(client, None, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json
        assert "body" in response_json["detail"][0]["loc"]


class TestGetThirdPartyRouter:
    def test_get_third_party(self, client, headers, third_party_seeders, third_party_data):
        third_party_created = create_third_party(client, third_party_data, headers)
        third_party_created_json = third_party_created.json()
        third_party = get_third_party(client, third_party_created_json["id"], headers)

        assert third_party.status_code == 200
        assert "id" in third_party.json()
        assert third_party_data["user_id"] == third_party.json()["user_id"]

    def test_get_third_party_with_no_found_id(self, client, headers):
        third_party_id = 4
        response = get_third_party(client, third_party_id, headers)

        assert response.status_code == 404
        assert "detail" in response.json()

    def test_get_third_party_with_none_id(self, client, headers):
        third_party_id = None
        response = get_third_party(client, third_party_id, headers)

        assert response.status_code == 422
        assert "detail" in response.json()

class TestGetThirdPartyRouterByUserId:
    def test_get_third_party_by_user_id(self, client, headers, third_party_data):
        third_party_created = create_third_party(client, third_party_data, headers)
        third_party_created_json = third_party_created.json()
        third_party = get_third_party_by_user_id(client, third_party_created_json["user_id"], headers)

        assert third_party.status_code == 200
        assert "id" in third_party.json()
        assert third_party_data["user_id"] == third_party.json()["user_id"]

    def test_get_third_party_with_no_found_user_id(self, client, headers):
        user_id = 9999
        response = get_third_party_by_user_id(client, user_id, headers)

        assert response.status_code == 404
        assert "detail" in response.json()

    def test_get_third_party_with_none_user_id(self, client, headers):
        user_id = None
        response = get_third_party_by_user_id(client, user_id, headers)

        assert response.status_code == 422
        assert "detail" in response.json()


class TestGetThirdPartiesRouter:
    def test_get_third_parties(self, client, headers, third_party_data):
        create_third_party(client, third_party_data, headers)
        third_party = get_third_parties(client, headers)

        assert third_party.status_code == 200
        assert "id" in third_party.json()[0]

    def test_get_third_parties_empty(self, client, headers):
        third_party = get_third_parties(client, headers)

        assert third_party.status_code == 200
        assert [] == third_party.json()


def create_third_party(client, data, headers) -> Response:
    third_party_created = client.post("/api/v1/third_parties", headers=headers, json=data)
    return third_party_created

def get_third_party(client, third_party_id, headers) -> Response:
    third_party = client.get(f"/api/v1/auth/third_parties/{third_party_id}", headers=headers)
    return third_party

def get_third_party_by_user_id(client, user_id, headers) -> Response:
    third_party = client.get(f"/api/v1/auth/third_parties/user/{user_id}", headers=headers)
    return third_party

def get_third_parties(client, headers) -> Response:
    third_parties = client.get("/api/v1/auth/third_parties", headers=headers)
    return third_parties


