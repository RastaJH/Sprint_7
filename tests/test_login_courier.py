import allure
from api.courier_api import CourierAPI

@allure.title("Курьер может авторизоваться")
def test_login_courier(create_courier):
    response = CourierAPI.login_courier({
        "login": create_courier["login"],
        "password": create_courier["password"]
    })
    assert response.status_code == 200
    assert "id" in response.json()

@allure.title("Ошибка при неверном пароле")
def test_login_wrong_password(create_courier):
    response = CourierAPI.login_courier({
        "login": create_courier["login"],
        "password": "wrongpass"
    })
    assert response.status_code in (400, 404)
