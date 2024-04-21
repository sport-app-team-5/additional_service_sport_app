import pytest
from httpx import Response
from app.modules.third_party.domain.entities import ThirdParty


@pytest.fixture
def third_party_seeders(db) -> None:
    db.add(ThirdParty(user_id=1))
    db.commit()


@pytest.fixture
def product_data() -> dict:
    return {
        "category": "Suplementos",
        "description": "Proteina en polvo a base de suero de leche",
        "name": "Proteina",
        "cost": 100000
    }


@pytest.fixture
def product_data_invalid() -> dict:
    return {
        "description": "desc",
    }


class TestCreateProductRouter:
    def test_create_product(self, client, headers, third_party_seeders, product_data):
        product_created = create_product(client, product_data, headers)
        product_created_json = product_created.json()

        assert product_created.status_code == 201
        assert "id" in product_created_json

    def test_create_product_with_invalid_data(self, client, headers, product_data):
        product_data_fail = product_data["third_party_id"] = "invalid"
        response = create_product(client, product_data_fail, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json

    def test_create_product_with_no_user(self, client, headers, product_data):
        product_data_fail = product_data["third_party_id"] = None

        response = create_product(client, product_data_fail, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json

    def test_create_product_with_null_data(self, client, headers):
        response = create_product(client, None, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json
        assert "body" in response_json["detail"][0]["loc"]


def create_product(client, data, headers) -> Response:
    product_created = client.post("/api/v1/auth/products", headers=headers, json=data)
    return product_created
