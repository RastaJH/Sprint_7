import requests
from data import ORDER_URL

class OrderAPI:

    @staticmethod
    def create_order(payload):
        return requests.post(ORDER_URL, json=payload)

    @staticmethod
    def get_orders():
        return requests.get(ORDER_URL)
