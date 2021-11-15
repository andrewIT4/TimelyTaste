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


def test_for_order_with_order_id_not_exists():
    orderid = 75
    resource = requests.get(f"http://localhost:80/order_api/orders/{orderid}")
    assert resource.status_code == 404


def test_for_order_with_unpaid_status():
    response = requests.get(f"http://localhost:80/order_api/orders/unpaid")
    assert response.status_code == 200
    order = response.json()
    assert order[0]["status"] == "unpaid"


def test_for_order_with_shipping_status():
    response = requests.get(f"http://localhost:80/order_api/orders/shipping")
    assert response.status_code == 200
    order = response.json()
    assert order[0]["status"] == "shipping"


def test_for_order_with_delivered_status():
    response = requests.get(f"http://localhost:80/order_api/orders/delivered")
    assert response.status_code == 200
    order = response.json()
    assert order[0]["status"] == "delivered"


def test_for_order_with_cancelled_status():
    response = requests.get(f"http://localhost:80/order_api/orders/cancelled")
    assert response.status_code == 200
    order = response.json()
    assert order[0]["status"] == "cancelled"


def test_for_create_new_order_without_json():
    response = requests.post("http://localhost:80/order_api/orders")
    assert response.status_code == 400


def test_for_create_new_order_without_jsonbody():
    response = requests.post(f"http://localhost:80/order_api/orders", json={})
    assert response.status_code == 422


def test_for_create_new_order_without_username():
    json = {
        "drinks": [
            {
                "drink_id": 2,
                "drink_name": "Coca Cola",
                "extra_charge": 0
            }
        ],
        "menu": [
            {
                "food_name": "Chinese fried rice",
                "menu_id": 1,
                "price": 38
            }
        ],
        "store_id": "b456"
    }
    response = requests.post(f"http://localhost:80/order_api/orders", json=json)
    assert response.status_code == 422

def test_for_create_new_order_without_store_id():
    json = {
        "drinks": [
            {
                "drink_id": 2,
                "drink_name": "Coca Cola",
                "extra_charge": 0
            }
        ],
        "menu": [
            {
                "food_name": "Chinese fried rice",
                "menu_id": 1,
                "price": 38
            }
        ],
        "username" : "bilebara"
    }
    response = requests.post(f"http://localhost:80/order_api/orders", json=json)
    assert response.status_code == 422

def test_for_create_new_order_without_menu():
    json = {
        "drinks": [
            {
                "drink_id": 2,
                "drink_name": "Coca Cola",
                "extra_charge": 0
            }
        ],
        "store_id": "b456",
        "username" : "bilebara"
    }
    response = requests.post(f"http://localhost:80/order_api/orders", json=json)
    assert response.status_code == 422

def test_for_create_new_order_without_drinks():
    json = {
        "menu": [
            {
                "food_name": "Chinese fried rice",
                "menu_id": 1,
                "price": 38
            }
        ],
        "store_id": "b456",
        "username" : "bilebara"
    }
    response = requests.post(f"http://localhost:80/order_api/orders", json=json)
    assert response.status_code == 422

def test_for_delete_order_not_existed():
    orderid = "884"
    response = requests.delete(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.status_code == 404

def test_for_create_and_delete_order():
    response = requests.get("http://localhost:80/order_api/orders")
    assert response.status_code == 200
    orderNum = len(response.json())

    json = {
        "drinks": [
            {
                "drink_id": 2,
                "drink_name": "Coca Cola",
                "extra_charge": 0
            }
        ],
        "menu": [
            {
                "food_name": "Chinese fried rice",
                "menu_id": 1,
                "price": 38
            }
        ],
        "store_id": "b456",
        "username": "bilebara"
    }
    response = requests.post(f"http://localhost:80/order_api/orders" , json = json)
    assert response.status_code == 201

    response = requests.get("http://localhost:80/order_api/orders")
    assert response.status_code == 200
    assert len(response.json()) == orderNum + 1
    assert response.json()[-0]["status"] == "unpaid"
    orderid = response.json()[-1]["order_id"]
    response = requests.delete(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.status_code == 202
    response = requests.get(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.status_code == 404
    response = requests.get(f"http://localhost:80/order_api/orders")
    assert len(response.json()) == orderNum

