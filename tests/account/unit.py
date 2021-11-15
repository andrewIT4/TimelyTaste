import pytest
import requests


def test_for_account_without_username():
    response = requests.get(f"http://localhost:15001/account_api/accounts")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_for_account_with_username():
    username = "wword555"
    response = requests.get(f"http://localhost:15001/account_api/accounts/{username}")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_for_account_username_not_exists():
    username = "I don't exist"
    response = requests.get(f"http://localhost:15001/account_api/accounts/{username}")
    assert response.status_code == 404


def test_for_register_new_account_without_json():
    response = requests.post(f"http://localhost:15001/account_api/signup")
    assert response.status_code == 500


def test_for_register_new_account_without_jsonbody():
    response = requests.post(f"http://localhost:15001/account_api/signup", json={})
    assert response.status_code == 500


def test_for_register_new_account_with_exsiting_account():
    json = {
        "password": "kkk5000",
        "username": "wword555"
    }
    response = requests.post(f"http://localhost:15001/account_api/signup", json=json)
    assert response.status_code == 401


def test_for_register_new_account_without_username():
    json = {
        "password": "kkk5000"
    }
    response = requests.post(f"http://localhost:15001/account_api/signup", json=json)
    assert response.status_code == 500


def test_for_register_new_account_without_password():
    json = {
        "username": "wword555"
    }
    response = requests.post(f"http://localhost:15001/account_api/signup", json=json)
    assert response.status_code == 500


def test_for_delete_account_not_existed():
    username = "iUsedToRuleTheWorld"
    response = requests.delete(f"http://localhost:15001/account_api/accounts/{username}")
    assert response.status_code == 404


def test_for_create_login_update_and_delete_account():
    json = {
        "password": "polarbearwalking",
        "username": "polarbearLover"
    }
    username = "polarbearLover"
    response = requests.post(f"http://localhost:15001/account_api/signup", json=json)
    assert response.status_code == 200

    response = requests.post(f"http://localhost:15001/account_api/login", json=json)
    assert response.status_code == 200

    response = requests.get(f"http://localhost:15001/account_api/accounts/{username}")
    assert response.status_code == 200
    assert len(response.json()) == 1

    json = {
        "credit_no": "2000000",
        "firstname": "polar",
        "lastname": "bear",
        "location": "artic",
        "role": "customer"
    }
    response = requests.put(f"http://localhost:15001/account_api/accounts/{username}", json=json)
    assert response.status_code == 202

    response = requests.get(f"http://localhost:15001/account_api/accounts/{username}")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["credit_no"] == "2000000"

    response = requests.delete(f"http://localhost:15001/account_api/accounts/{username}")
    assert response.status_code == 200

    response = requests.get(f"http://localhost:15001/account_api/accounts/{username}")
    assert response.status_code == 404


def test_for_update_customer_with_same_data():
    username = "admin2"
    json = {
        "credit_no": "2",
        "firstname": "admin2",
        "lastname": "admin2",
        "location": "admin2",
        "role": "admin"
    }
    response = requests.put(f"http://localhost:15001/account_api/accounts/{username}", json=json)
    assert response.status_code == 409


def test_for_update_customer_without_exist_username():
    username = "gotFired:("
    json = {
        "credit_no": "2",
        "firstname": "admin2",
        "lastname": "admin2",
        "location": "admin2",
        "role": "admin"
    }
    response = requests.put(f"http://localhost:15001/account_api/accounts/{username}", json=json)
    assert response.status_code == 404


def test_for_update_customer_without_jsonbody():
    username = "admin2"
    response = requests.put(f"http://localhost:15001/account_api/accounts/{username}", json={})
    assert response.status_code == 422


def test_for_update_customer_without_json():
    username = "admin2"
    response = requests.put(f"http://localhost:15001/account_api/accounts/{username}")
    assert response.status_code == 400


def test_for_update_customer_without_credit_no():
    username = "admin2"
    json = {
        "firstname": "admin2",
        "lastname": "admin2",
        "location": "home",
        "role": "admin"
    }
    response = requests.put(f"http://localhost:15001/account_api/accounts/{username}", json=json)
    assert response.status_code == 422


def test_for_update_customer_without_firstname():
    username = "admin2"
    json = {
        "credit_no": "2",
        "lastname": "admin2",
        "location": "home",
        "role": "admin"
    }
    response = requests.put(f"http://localhost:15001/account_api/accounts/{username}", json=json)
    assert response.status_code == 422


def test_for_update_customer_without_lastname():
    username = "admin2"
    json = {
        "credit_no": "2555",
        "firstname": "admin2",
        "location": "admin2",
        "role": "admin"
    }
    response = requests.put(f"http://localhost:15001/account_api/accounts/{username}", json=json)
    assert response.status_code == 422


def test_for_update_customer_without_location():
    username = "gotFired:("
    json = {
        "credit_no": "2",
        "firstname": "admin2",
        "lastname": "minadd",
        "role": "admin"
    }
    response = requests.put(f"http://localhost:15001/account_api/accounts/{username}", json=json)
    assert response.status_code == 422


def test_for_update_customer_without_role():
    username = "gotFired:("
    json = {
        "credit_no": "25455151515",
        "firstname": "admin2",
        "lastname": "admin2",
        "location": "admin2",
    }
    response = requests.put(f"http://localhost:15001/account_api/accounts/{username}", json=json)
    assert response.status_code == 422

