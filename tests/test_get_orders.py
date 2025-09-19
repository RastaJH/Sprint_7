import allure
from api.order_api import OrderAPI

@allure.title("Получение списка заказов")
def test_get_orders_list():
    response = OrderAPI.get_orders()
    assert response.status_code == 200
    body = response.json()
    assert "orders" in body
    assert isinstance(body["orders"], list)
