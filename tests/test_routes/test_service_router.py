import pytest
from httpx import Response
from app.modules.services.domain.entities import Service


@pytest.fixture
def service_seeders(db) -> None:
    db.commit()


@pytest.fixture
def service_data() -> dict:
    return {
        "user_id": 1
    }

@pytest.fixture
def service_data_invalid() -> dict:
    return {
    }


class TestCreateServiceRouter:
    def test_create_service(self, client, headers,  service_data):
        service_created = create_service(client, service_data, headers)
        service_created_json = service_created.json()

        assert service_created.status_code == 201
        assert "id" in service_created_json
        assert service_data['user_id'] == service_created_json["user_id"]

    def test_create_service_with_invalid_data(self, client, headers, service_data):
        service_data_fail = service_data["user_id"] = "invalid"
        response = create_service(client, service_data_fail, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json

    def test_create_service_with_no_user(self, client, headers, service_data):
        
        service_data_fail = service_data["user_id"] = None

        response = create_service(client, service_data_fail, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json

    def test_create_service_with_null_data(self, client, headers):
        response = create_service(client, None, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json
        assert "body" in response_json["detail"][0]["loc"]


class TestGetServiceRouter:
    def test_get_service(self, client, headers, service_seeders, service_data):
        service_created = create_service(client, service_data, headers)
        service_created_json = service_created.json()
        service = get_service(client, service_created_json["id"], headers)

        assert service.status_code == 200
        assert "id" in service.json()
        assert service_data["user_id"] == service.json()["user_id"]

    def test_get_service_with_no_found_id(self, client, headers):
        service_id = 4
        response = get_service(client, service_id, headers)

        assert response.status_code == 404
        assert "detail" in response.json()

    def test_get_service_with_none_id(self, client, headers):
        service_id = None
        response = get_service(client, service_id, headers)

        assert response.status_code == 422
        assert "detail" in response.json()

class TestGetServiceRouterByUserId:
    def test_get_service_by_user_id(self, client, headers, service_data):
        service_created = create_service(client, service_data, headers)
        service_created_json = service_created.json()
        service = get_service_by_user_id(client, service_created_json["user_id"], headers)

        assert service.status_code == 200
        assert "id" in service.json()
        assert service_data["user_id"] == service.json()["user_id"]

    def test_get_service_with_no_found_user_id(self, client, headers):
        user_id = 9999
        response = get_service_by_user_id(client, user_id, headers)

        assert response.status_code == 404
        assert "detail" in response.json()

    def test_get_service_with_none_user_id(self, client, headers):
        user_id = None
        response = get_service_by_user_id(client, user_id, headers)

        assert response.status_code == 422
        assert "detail" in response.json()


class TestGetServicesRouter:
    def test_get_services(self, client, headers, service_data):
        create_service(client, service_data, headers)
        service = get_services(client, headers)

        assert service.status_code == 200
        assert "id" in service.json()[0]

    def test_get_services_empty(self, client, headers):
        service = get_services(client, headers)

        assert service.status_code == 200
        assert [] == service.json()


def create_service(client, data, headers) -> Response:
    service_created = client.post("/api/v1/additional_service/services", headers=headers, json=data)
    return service_created

def get_service(client, service_id, headers) -> Response:
    service = client.get(f"/api/v1/additional_service/services/{service_id}", headers=headers)
    return service

def get_service_by_user_id(client, user_id, headers) -> Response:
    service = client.get(f"/api/v1/additional_service/services/user/{user_id}", headers=headers)
    return service

def get_services(client, headers) -> Response:
    services = client.get("/api/v1/additional_service/services", headers=headers)
    return services


