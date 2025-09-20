import pytest
import requests
from data import BASE_URL
from helpers import generate_unique_courier
from api.courier_api import CourierAPI 
from api.order_api import OrderAPI      

@pytest.fixture
def courier_api():
    return CourierAPI()

@pytest.fixture
def order_api():
    return OrderAPI()

@pytest.fixture
def new_courier():
    courier = generate_unique_courier()
    resp = requests.post(f"{BASE_URL}/courier", json=courier)
    if resp.status_code == 201:
        login_resp = requests.post(f"{BASE_URL}/courier/login", json={
            "login": courier["login"],
            "password": courier["password"]
        })
        courier_id = login_resp.json().get("id")
        yield courier, courier_id
        if courier_id:
            requests.delete(f"{BASE_URL}/courier/{courier_id}")
    else:
        yield courier, None