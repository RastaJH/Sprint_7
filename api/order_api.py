import requests
import allure
from data import BASE_URL

class OrderAPI:
    @allure.step("Создание заказа")
    def create_order(self, payload):
        return requests.post(f"{BASE_URL}/orders", json=payload)

    @allure.step("Получение списка заказов")
    def get_orders(self):
        return requests.get(f"{BASE_URL}/orders")