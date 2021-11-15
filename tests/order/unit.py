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
        "username": "bilebara"
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
        "username": "bilebara"
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
        "username": "bilebara"
    }
    response = requests.post(f"http://localhost:80/order_api/orders", json=json)
    assert response.status_code == 422


def test_for_delete_order_not_existed():
    orderid = "884"
    response = requests.delete(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.status_code == 404


def test_for_create_update_delete_order():
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
    response = requests.post(f"http://localhost:80/order_api/orders", json=json)
    assert response.status_code == 201

    response = requests.get("http://localhost:80/order_api/orders")
    assert response.status_code == 200
    assert len(response.json()) == orderNum + 1
    orderid = orderNum + 1
    response = requests.get(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.json()[0]["status"] == "unpaid"

    json = {
        "drinks": [
            {
                "drink_id": 3,
                "drink_name": "Lemon Tea",
                "extra_charge": 0
            }
        ],
        "menu": [
            {
                "food_name": "Scrambled Eggs with BBQ Pork",
                "menu_id": 2,
                "price": 38
            }
        ]
    }
    response = requests.put(f"http://localhost:80/order_api/orders/{orderid}", json=json)
    assert response.status_code == 202
    response = requests.get(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.status_code == 200
    assert response.json()[0]["menu"][0]["food_name"] == "Scrambled Eggs with BBQ Pork"

    json = {
        "status": "shipping"
    }
    response = requests.patch(f"http://localhost:80/order_api/orders/{orderid}", json=json)
    assert response.status_code == 202
    response = requests.get(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.status_code == 200
    assert response.json()[0]["status"] == "shipping"

    response = requests.delete(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.status_code == 202
    response = requests.get(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.status_code == 404
    response = requests.get(f"http://localhost:80/order_api/orders")
    assert len(response.json()) == orderNum


def test_for_update_order_without_existing_order_id():
    orderid = "741"
    json = {
        "drinks": [
            {
                "drink_id": 3,
                "drink_name": "Lemon Tea",
                "extra_charge": 0
            }
        ],
        "menu": [
            {
                "food_name": "Scrambled Eggs with BBQ Pork",
                "menu_id": 2,
                "price": 38
            }
        ]
    }
    response = requests.put(f"http://localhost:80/order_api/orders/{orderid}", json=json)
    assert response.status_code == 404


def test_for_update_order_without_existing_jsonbody():
    orderid = 1
    response = requests.put(f"http://localhost:80/order_api/orders/{orderid}", json={})
    assert response.status_code == 422


def test_for_update_order_without_existing_json():
    orderid = 2
    response = requests.put(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.status_code == 400


def test_for_update_order_without_drinks():
    orderid = "4"
    json = {
        "menu": [
            {
                "food_name": "Scrambled Eggs with BBQ Pork",
                "menu_id": 2,
                "price": 38
            }
        ]
    }
    response = requests.put(f"http://localhost:80/order_api/orders/{orderid}", json=json)
    assert response.status_code == 422

def test_for_update_order_without_menus():
    orderid = "4"
    json = {
        "drinks": [
            {
                "drink_id": 3,
                "drink_name": "Lemon Tea",
                "extra_charge": 0
            }
        ]
    }
    response = requests.put(f"http://localhost:80/order_api/orders/{orderid}", json=json)
    assert response.status_code == 422


def test_for_update_order_status_without_jsonbody():
    orderid = 1
    response = requests.patch(f"http://localhost:80/order_api/orders/{orderid}", json={})
    assert response.status_code == 422


def test_for_update_order_status_without_json():
    orderid = 2
    response = requests.patch(f"http://localhost:80/order_api/orders/{orderid}")
    assert response.status_code == 400

def test_for_update_order_status_without_existing_orderid():
    orderid = 85488
    json = {
        "status": "shipping"
    }
    response = requests.patch(f"http://localhost:80/order_api/orders/{orderid}",json = json)


