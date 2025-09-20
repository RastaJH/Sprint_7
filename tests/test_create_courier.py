import pytest
from data import EXPECTED_RESPONSES
from helpers import generate_unique_courier

@pytest.mark.courier
class TestCourierCreation:
    def test_create_courier_success(self, courier_api):
        courier = generate_unique_courier()
        resp = courier_api.create_courier(courier)
        assert resp.status_code == 201
        assert resp.json() == EXPECTED_RESPONSES["courier_created"]

    def test_create_same_courier_fails(self, courier_api):
        courier = generate_unique_courier()
        courier_api.create_courier(courier)
        resp = courier_api.create_courier(courier)
        assert resp.status_code == 409
        assert resp.json() == EXPECTED_RESPONSES["login_conflict"]

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_create_courier_missing_field(self, courier_api, field):
        courier = generate_unique_courier()
        courier.pop(field)
        resp = courier_api.create_courier(courier)
        assert resp.status_code == 400
        assert resp.json() == EXPECTED_RESPONSES["missing_field"]