import requests
import pytest

def test_for_menu_without_store_id():
    response = requests.get("http://localhost:15003/menu_api/menus")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_for_menu_with_store_id():
    storeid = "a123"
    response = requests.get(f"http://localhost:15003/menu_api/menus/{storeid}")
    assert response.status_code == 200
    menu = response.json()
    assert len(menu) == 1
    assert menu[0]["store_id"] == storeid
    assert len(menu[0]["menus"]) > 0


def test_for_menu_with_store_id_not_existing():
    storeid = "G730"
    response = requests.get(f"http://localhost:15003/menu_api/menus/{storeid}")
    assert response.status_code == 404


def test_for_create_new_menu_without_json():
    response = requests.post("http://localhost:15003/menu_api/menus")
    assert response.status_code == 400


def test_for_create_new_menu_without_jsonbody():
    response = requests.post("http://localhost:15003/menu_api/menus", json={})
    assert response.status_code == 422


def test_for_create_new_menu_with_existed_store_id():
    json = {
        "drinks": [
            {
                "drink_id": 1,
                "drink_name": "Scented Tea",
                "extra_charge": 10
            },
            {
                "drink_id": 2,
                "drink_name": "Tieguanyin",
                "extra_charge": 12
            }
        ],
        "menus": [
            {
                "food_name": "Har Gow",
                "menu_id": 1,
                "price": 20
            }
        ],
        "store_id": "c789"
    }
    response = requests.post("http://localhost:15003/menu_api/menus", json=json)
    assert response.status_code == 403


def test_for_create_new_menu_without_store_id():
    json = {
        "drinks": [
            {
                "drink_id": 1,
                "drink_name": "Scented Tea",
                "extra_charge": 10
            },
            {
                "drink_id": 2,
                "drink_name": "Tieguanyin",
                "extra_charge": 12
            }
        ],
        "menus": [
            {
                "food_name": "Har Gow",
                "menu_id": 1,
                "price": 20
            }
        ]
    }
    response = requests.post("http://localhost:15003/menu_api/menus", json=json)
    assert response.status_code == 422


def test_for_create_new_menu_without_menus():
    json = {
        "drinks": [
            {
                "drink_id": 1,
                "drink_name": "Scented Tea",
                "extra_charge": 10
            },
            {
                "drink_id": 2,
                "drink_name": "Tieguanyin",
                "extra_charge": 12
            }
        ],
        "store_id": "c789"
    }
    response = requests.post("http://localhost:15003/menu_api/menus", json=json)
    assert response.status_code == 403


def test_for_create_new_menu_without_drinks():
    json = {
        "menus": [
            {
                "food_name": "Har Gow",
                "menu_id": 1,
                "price": 20
            }
        ],
        "store_id": "c789"
    }
    response = requests.post("http://localhost:15003/menu_api/menus", json=json)
    assert response.status_code == 403


def test_for_delete_menu_not_existed():
    store_id = "F257"
    response = requests.delete(f"http://localhost:15003/menu_api/menus/{store_id}")
    assert response.status_code == 404


def test_for_create_and_delete_menu():
    storeid = "c999"
    json = {
        "drinks": [
            {
                "drink_id": 1,
                "drink_name": "Tea",
                "extra_charge": 10
            },
            {
                "drink_id": 2,
                "drink_name": "Coffee",
                "extra_charge": 12
            }
        ],
        "menus": [
            {
                "food_name": "Sandwich",
                "menu_id": 1,
                "price": 20
            }
        ],
        "store_id": storeid
    }
    response = requests.post("http://localhost:15003/menu_api/menus", json=json)
    assert response.status_code == 201
    response = requests.get(f"http://localhost:15003/menu_api/menus/{storeid}")
    assert response.status_code == 200
    assert len(response.json()) > 0
    response = requests.delete(f"http://localhost:15003/menu_api/menus/{storeid}")
    assert response.status_code == 200
    response = requests.get(f"http://localhost:15003/menu_api/menus/{storeid}")
    assert response.status_code == 404


def test_for_update_menu():
    storeid = "c789"
    json = {
        "drinks": [
            {
                "drink_id": 1,
                "drink_name": "Tea",
                "extra_charge": 10
            },
            {
                "drink_id": 2,
                "drink_name": "Coffee",
                "extra_charge": 12
            }
        ],
        "menus": [
            {
                "food_name": "Sandwich",
                "menu_id": 1,
                "price": 20
            }
        ]
    }
    response = requests.get(f"http://localhost:15003/menu_api/menus/{storeid}")
    store = response.json()
    assert store[0]["drinks"][0]["drink_name"] == "Scented Tea"
    response = requests.put(f"http://localhost:15003/menu_api/menus/{storeid}", json=json)
    assert response.status_code == 202
    response = requests.get(f"http://localhost:15003/menu_api/menus/{storeid}")
    store = response.json()
    assert store[0]["drinks"][0]["drink_name"] == "Tea"
    json = {
        "drinks": [
            {
                "drink_id": 1,
                "drink_name": "Scented Tea",
                "extra_charge": 10
            },
            {
                "drink_id": 2,
                "drink_name": "Tieguanyin",
                "extra_charge": 12
            },
            {
                "drink_id": 3,
                "drink_name": "Sowmee Tea",
                "extra_charge": 11
            }
        ],
        "menus": [
            {
                "food_name": "Har Gow",
                "menu_id": 1,
                "price": 20
            },
            {
                "food_name": "Pork Siu Mai",
                "menu_id": 2,
                "price": 20
            },
            {
                "food_name": "Sweet Tofu",
                "menu_id": 3,
                "price": 16
            }
        ]
    }
    response = requests.put(f"http://localhost:15003/menu_api/menus/{storeid}", json=json)
    assert response.status_code == 202
    response = requests.get(f"http://localhost:15003/menu_api/menus/{storeid}")
    store = response.json()
    assert store[0]["drinks"][0]["drink_name"] == "Scented Tea"


def test_for_update_menu_with_same_data():
    storeid = "c789"
    json = {
        "drinks": [
            {
                "drink_id": 1,
                "drink_name": "Scented Tea",
                "extra_charge": 10
            },
            {
                "drink_id": 2,
                "drink_name": "Tieguanyin",
                "extra_charge": 12
            },
            {
                "drink_id": 3,
                "drink_name": "Sowmee Tea",
                "extra_charge": 11
            }
        ],
        "menus": [
            {
                "food_name": "Har Gow",
                "menu_id": 1,
                "price": 20
            },
            {
                "food_name": "Pork Siu Mai",
                "menu_id": 2,
                "price": 20
            },
            {
                "food_name": "Sweet Tofu",
                "menu_id": 3,
                "price": 16
            }
        ]
    }
    response = requests.put(f"http://localhost:15003/menu_api/menus/{storeid}", json=json)
    assert response.status_code == 409


def test_for_update_menu_without_existed_store_id():
    storeid = "C2021"
    json = {
        "drinks": [
            {
                "drink_id": 1,
                "drink_name": "Tea",
                "extra_charge": 10
            }
        ],
        "menus": [
            {
                "food_name": "Sandwich",
                "menu_id": 1,
                "price": 20
            }
        ]
    }
    response = requests.put(f"http://localhost:15003/menu_api/menus/{storeid}", json=json)

    assert response.status_code == 404


def test_for_update_menu_without_jsonbody():
    storeid = "a123"
    response = requests.put(f"http://localhost:15003/menu_api/menus/{storeid}", json={})
    assert response.status_code == 422


def test_for_update_menu_without_json():
    storeid = "a123"
    response = requests.put(f"http://localhost:15003/menu_api/menus/{storeid}")
    assert response.status_code == 400

def test_for_update_menu_without_menu():
    storeid = "a123"
    json = {
        "drinks": [
            {
                "drink_id": 1,
                "drink_name": "Tea",
                "extra_charge": 10
            }
        ]
    }
    response = requests.put(f"http://localhost:15003/menu_api/menus/{storeid}", json=json)
    assert response.status_code == 422

def test_for_update_menu_without_drinks():
    storeid = "a123"
    json = {
        "menus": [
            {
                "food_name": "Sandwich",
                "menu_id": 1,
                "price": 20
            }
        ]
    }
    response = requests.put(f"http://localhost:15003/menu_api/menus/{storeid}", json=json)
    assert response.status_code == 422


# end of menu api testing