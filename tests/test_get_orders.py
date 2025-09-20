import pytest

@pytest.mark.order
class TestOrdersList:
    def test_get_orders_returns_list(self, order_api):
        resp = order_api.get_orders()
        assert resp.status_code == 200
        assert "orders" in resp.json()
        assert isinstance(resp.json()["orders"], list)