import pytest
from data import ORDER_DEFAULT

@pytest.mark.order
class TestCreateOrder:
    @pytest.mark.parametrize("color", [[], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_create_order_with_colors(self, color, order_api):
        payload = ORDER_DEFAULT.copy()
        payload["color"] = color
        resp = order_api.create_order(payload)
        assert resp.status_code == 201
        assert "track" in resp.json()