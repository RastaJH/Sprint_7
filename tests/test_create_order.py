import pytest
import allure
from api.order_api import OrderAPI

base_order = {
    "firstName": "test",
    "lastName": "user",
    "address": "Moscow",
    "metroStation": 4,
    "phone": "+79999999999",
    "rentTime": 5,
    "deliveryDate": "2025-09-19",
    "comment": "test order"
}

@allure.title("Создание заказа с разными параметрами цвета")
@pytest.mark.parametrize("color", [[], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
def test_create_order_with_colors(color):
    payload = base_order.copy()
    payload["color"] = color
    response = OrderAPI.create_order(payload)
    assert response.status_code == 201
    assert "track" in response.json()
