import requests
import allure
from data import BASE_URL

class CourierAPI:
    @allure.step("Создание курьера")
    def create_courier(self, payload):
        return requests.post(f"{BASE_URL}/courier", json=payload)

    @allure.step("Авторизация курьера")
    def login_courier(self, payload):
        return requests.post(f"{BASE_URL}/courier/login", json=payload)

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        return requests.delete(f"{BASE_URL}/courier/{courier_id}")