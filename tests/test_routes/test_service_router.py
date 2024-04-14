import pytest
from httpx import Response

from app.modules.services.domain.entities import Service
from app.modules.third_party.domain.entities import ThirdParty

@pytest.fixture
def third_party_seeders(db) -> None:
    db.add(ThirdParty(user_id=1))
    db.commit()

# @pytest.fixture
# def service_seeders(db) -> None:
#     db.add(Service(third_party_id=1, type))
#     db.commit()


@pytest.fixture
def service_data() -> dict:
    return {
        "third_party_id": 1,
        "type": "TRANSPORT",
        "description": "Servicio exclusivo para carreras de más de 4 horas",
        "is_active": True,
        "cost": 25.90      
    }

@pytest.fixture
def service_data_invalid() -> dict:
    return {
        "description": "desc",
    }


class TestCreateServiceRouter:
    def test_create_service(self, client, headers,  third_party_seeders, service_data):

        service_created = create_service(client, service_data, headers)
        service_created_json = service_created.json()

        print("service_created_json: " , service_created_json)

        assert service_created.status_code == 201
        assert "id" in service_created_json
        assert service_data['third_party_id'] == service_created_json["third_party_id"]

    def test_create_service_with_invalid_data(self, client, headers, service_data):
        service_data_fail = service_data["third_party_id"] = "invalid"
        response = create_service(client, service_data_fail, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json

    def test_create_service_with_no_user(self, client, headers, service_data):
        
        service_data_fail = service_data["third_party_id"] = None

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
    def test_get_service(self, client, headers, third_party_seeders, service_data):
        service_created = create_service(client, service_data, headers)
        service_created_json = service_created.json()
        service = get_service(client, service_created_json["id"], headers)

        assert service.status_code == 200
        assert "id" in service.json()
        assert service_data["third_party_id"] == service.json()["third_party_id"]

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

class TestGetServicesRouter:
    def test_get_services(self, client, headers, third_party_seeders, service_data):
        create_service(client, service_data, headers)
        service = get_services(client, headers)
        assert service.status_code == 200
        service_json = service.json()
        assert len(service_json) > 0, "Expected 'service.json()' to be a non-empty list"
        assert "id" in service_json[0]

    def test_get_services_empty(self, client, headers):
        service = get_services(client, headers)

        assert service.status_code == 200
        assert [] == service.json()


class TestDeactivateServiceRouter:
    def test_deactivate_service(self, client, headers, third_party_seeders, service_data):
        service_created = create_service(client, service_data, headers)
        service_created_json = service_created.json()
        service = deactivate_service(client, service_created_json["id"], headers)

        assert service.status_code == 200
        assert "id" in service.json()
        assert service_data["is_active"] != service.json()["is_active"]

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

def create_service(client, data, headers) -> Response:
    service_created = client.post("/api/v1/auth/services", headers=headers, json=data)
    return service_created

def update_services(client, service_id, data, headers) -> Response:
    services = client.put("/api/v1/auth/services/{service_id}", headers=headers, json=data)
    return services

def deactivate_service(client, service_id, headers) -> Response:
    service = client.put(f"/api/v1/auth/services/deactivate/{service_id}", headers=headers)
    return service

def get_service(client, service_id, headers) -> Response:
    service = client.get(f"/api/v1/auth/services/{service_id}", headers=headers)
    return service

def get_services(client, headers) -> Response:
    services = client.get("/api/v1/auth/services", headers=headers)
    return services

def create_third_party(client, data, headers) -> Response:
    third_party_created = client.post("/api/v1/third_parties", headers=headers, json=data)
    return third_party_created

