import pytest
import requests

def test_for_order_without_order_id():
    response = requests.get("http://localhost:80/order_api/orders")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_for_order_with_order_id():
    orderid = 3
    response = requests.get(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.status_code == 200
    assert len(response.json()) == 1
