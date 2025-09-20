BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

EXPECTED_RESPONSES = {
    "courier_created": {"ok": True},
    "missing_field": {"code": 400, "message": "Недостаточно данных для создания учетной записи"},
    "login_conflict": {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."},
    "not_found": {"code": 404, "message": "Учетная запись не найдена"},
    "wrong_creds": {"code": 404, "message": "Учетная запись не найдена"}
}

ORDER_DEFAULT = {
    "firstName": "Aboba",
    "lastName": "Uzumaki",
    "address": "Tataria, 142 home.",
    "metroStation": 4,
    "phone": "+7 800 555 35 35",
    "rentTime": 5,
    "deliveryDate": "2023-06-06",
    "comment": "Go home dog",
    "color": []
}