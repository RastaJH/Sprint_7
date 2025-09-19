import allure
from api.courier_api import CourierAPI

@allure.title("Курьера можно создать")
def test_create_courier_success(courier_data):
    response = CourierAPI.create_courier(courier_data)
    assert response.status_code == 201
    assert response.json() == {"ok": True}

@allure.title("Нельзя создать двух одинаковых курьеров")
def test_create_duplicate_courier(courier_data, create_courier):
    response = CourierAPI.create_courier(courier_data)
    assert response.status_code == 409

@allure.title("Нельзя создать курьера без обязательных полей")
def test_create_courier_without_required_field():
    response = CourierAPI.create_courier({"login": "onlylogin"})
    assert response.status_code in (400, 422)
