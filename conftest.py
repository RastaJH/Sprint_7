import pytest
import requests
from data import COURIER_URL, COURIER_LOGIN_URL

@pytest.fixture
def courier_data():
    return {
        "login": "testuser123",
        "password": "testpass123",
        "firstName": "testname"
    }

@pytest.fixture
def create_courier(courier_data):
    resp = requests.post(COURIER_URL, json=courier_data)
    assert resp.status_code in (201, 409)
    yield courier_data
    login_payload = {"login": courier_data["login"], "password": courier_data["password"]}
    login_response = requests.post(COURIER_LOGIN_URL, json=login_payload)
    if login_response.status_code == 200 and "id" in login_response.json():
        courier_id = login_response.json()["id"]
        requests.delete(f"{COURIER_URL}/{courier_id}")
