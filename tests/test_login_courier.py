import pytest
from data import EXPECTED_RESPONSES

@pytest.mark.courier
class TestCourierLogin:
    def test_login_success(self, new_courier, courier_api):
        courier, courier_id = new_courier
        resp = courier_api.login_courier({
            "login": courier["login"],
            "password": courier["password"]
        })
        assert resp.status_code == 200
        assert "id" in resp.json()

    def test_login_missing_fields(self, courier_api):
        resp = courier_api.login_courier({"login": "only_login"})
        assert resp.status_code in [400, 404]

    def test_login_wrong_password(self, new_courier, courier_api):
        courier, courier_id = new_courier
        resp = courier_api.login_courier({
            "login": courier["login"],
            "password": "wrongpass"
        })
        assert resp.status_code == 404
        assert resp.json() == EXPECTED_RESPONSES["wrong_creds"]

    def test_login_nonexistent_user(self, courier_api):
        resp = courier_api.login_courier({
            "login": "fakeuser123",
            "password": "fakepass123"
        })
        assert resp.status_code == 404
        assert resp.json() == EXPECTED_RESPONSES["not_found"]