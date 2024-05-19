import pytest
from httpx import Response
from app.modules.services.domain.entities import Notification, Service, ServiceSportman
from app.modules.third_party.domain.entities import ThirdParty


@pytest.fixture
def third_party_seeders(db) -> None:
    db.add(ThirdParty(user_id=1))
    db.add(Service(third_party_id=1, is_inside_house=False, type="SPORT_SPECIALIST", description="Servicio exclusivo para carreras de más de 4 horas", is_active=True, cost=25.90))
    db.commit()

@pytest.fixture
def notification_seeders(db) -> None:
    db.add(Notification(message="Notificación de prueba", type="IALE", status="UNREAD"))
    db.commit()

@pytest.fixture
def appointments_seeders(db) -> None:
    db.add(ServiceSportman(sportman_id=1, service_id=1, injury_id=1, sport="Ciclyn", appointment_date="2024-05-16" ))
    db.add(ServiceSportman(sportman_id=2, service_id=2, injury_id=1, sport="Running", appointment_date="2024-05-16" ))
    db.commit()




@pytest.fixture
def service_data() -> dict:
    return {
        "third_party_id": 1,
        "is_inside_house": False,
        "type": "SPORT_SPECIALIST",
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
    def test_create_service(self, client, headers, third_party_seeders, service_data):
        service_created = create_service(client, service_data, headers)
        service_created_json = service_created.json()

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

    def test_create_schedule_appointment(self, client, headers, third_party_seeders):
        appointment_data = {
            "sportman_id": 1,
            "service_id": 1,
            "injury_id": 1,
            "sport": "Ciclyn",
            "appointment_date":  "2024-05-16" 
        }
        response = create_schedule_appointment(client, appointment_data, headers)
        assert response.status_code == 201

    def test_get_schedule_appointment_no_data(self, client, headers, third_party_seeders):
        sportman_id = 1
        response = get_schedule_appointment(client, sportman_id, headers)
        response_json = response.json()

        assert response.status_code == 404        
        assert "detail" in response_json

    def test_get_schedule_appointment(self, client, headers, third_party_seeders, appointments_seeders):
        sportman_id = 1
        response = get_schedule_appointment(client, sportman_id, headers)
        response_json = response.json()

        assert response.status_code == 200
        assert "appointment_date" in response_json[0]
        assert "injury_id" in response_json[0]
        assert "service_name" in response_json[0]
        assert "id" in response_json[0]

    def test_create_notification(self, client, headers):
        notification_data = {
            "message": "Notificación de prueba",
            "type": "IALE",
            "status": "UNREAD"
        }
        response = create_notification(client, notification_data, headers)
        response_json = response.json()
        print("response_json: ", response_json)

        assert response.status_code == 201
        assert "id" in response_json

    def test_get_notification_by_invalid_status_and_type(self, client, headers, notification_seeders):
        status = "INVALID"
        notification_type = "IALE"
        response = get_notification_by_status_and_type(client, status, notification_type, headers)
        response_json = response.json()

        assert response.status_code == 404
        assert "detail" in response_json        

    def test_update_notification_status(self, client, headers, notification_seeders):
        
        notification_data = {
            "type": "IALE",
        }
        response = update_notification_status(client, notification_data, headers )

        assert response.status_code == 200

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
        print("service.json() ", service.json())            
        assert service.status_code == 200
        service_json = service.json()        
        assert len(service_json) > 0, "Expected 'service.json()' to be a non-empty list"
        assert "id" in service_json[0]

    def test_get_services_empty(self, client, headers):
        service = get_services(client, headers)

        assert service.status_code == 200
        service_json = service.json()      
        assert len(service_json) == 0, "Expected 'service.json()' to be an empty list"

    def test_get_service_by_type(self, client, headers, third_party_seeders):
        service_type = "SPORT_SPECIALIST"
        response = get_service_by_type(client, service_type, headers)
        response_json = response.json()

        assert response.status_code == 200
        assert "cost" in response_json[0]

    def test_get_service_with_invalid_type(self, client, headers, third_party_seeders):
        service_type = ""
        response = get_service_by_type(client, service_type, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json

    def test_get_service_no_exists(self, client, headers, third_party_seeders):
        service_type = "TEST"
        response = get_service_by_type(client, service_type, headers)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json.__len__() == 0    


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

class TestOthersServiceRouter:        

    def test_deactivate_service_with_invalid_id(self, client, headers):
        service_id = "invalid_id"
        response = deactivate_service(client, service_id, headers)

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

def get_service_by_type(client, service_type, headers) -> Response:
    service = client.get(f"/api/v1/auth/services/type/{service_type}", headers=headers)
    return service


def get_services(client, headers) -> Response:
    services = client.get("/api/v1/auth/services?/is_inside_house=false", headers=headers)
    return services


def create_third_party(client, data, headers) -> Response:
    third_party_created = client.post("/api/v1/third_parties", headers=headers, json=data)
    return third_party_created

def create_schedule_appointment(client, data, headers) -> Response:
    response = client.post("/api/v1/auth/services/appointment", headers=headers, json=data)
    return response 

def get_schedule_appointment(client, sportman_id, headers) -> Response:
    response = client.get(f"/api/v1/auth/services/appointment/{sportman_id}", headers=headers)
    return response

def create_notification(client, data, headers) -> Response:   
    response = client.post("/api/v1/auth/services/notification", headers=headers, json=data)
    return response 

def get_notification_by_status_and_type(client, status, type, headers) -> Response:
    response = client.get(f"/api/v1/auth/services/notifications/user?status={status}&type={type}", headers=headers)        
    return response

def update_notification_status(client, data, headers) -> Response:
    response = client.put("/api/v1/auth/services/notification/user", headers=headers, json=data)
    return response