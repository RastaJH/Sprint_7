import requests
from data import COURIER_URL, COURIER_LOGIN_URL

class CourierAPI:

    @staticmethod
    def create_courier(payload):
        return requests.post(COURIER_URL, json=payload)

    @staticmethod
    def login_courier(payload):
        return requests.post(COURIER_LOGIN_URL, json=payload)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{COURIER_URL}/{courier_id}")
