import pytest
from fastapi.testclient import TestClient
from ...data import SeedData
from ....app.api.entity1.category_enum import Category
from ...conftest import data as test_data


@pytest.fixture
def add_new_product(client: TestClient, seed_data: SeedData):
    res = client.post(
        url="/product/add",
        json={"name": "clean code",
              "category": Category.BOOK,
              "added_user_id": test_data.users_id[0],
              "price": 100.25,
              "quantity": 10,
              },
        headers={"Authorization": f"Bearer {test_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
    test_data.product_id.append(res.json()["id"])

    res = client.post(
        url="/product/add",
        json={"name": "jacket",
              "category": Category.CLOTHING,
              "added_user_id": test_data.users_id[0],
              "price": 21.50,
              "quantity": 50,
              },
        headers={"Authorization": f"Bearer {test_data.users_tokens[1]}"},
    )
    assert res.status_code == 200
    test_data.product_id.append(res.json()["id"])




def test_user_product(client: TestClient, seed_data: SeedData, add_new_product):

    res = client.get(
        url="/product/user/list",
        headers={"Authorization": f"Bearer {test_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
    assert len(res.json()) == 2


def test_update_product(client: TestClient, seed_data: SeedData, add_new_product):
    res = client.patch(
        url="/product/update",
        json={
              "id": {test_data.product_id[0]},
              "price": 125.50,
              "quantity": 5,
              },
        headers={"Authorization": f"Bearer {test_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
    assert res.json() == True


def test_get_product(client: TestClient, seed_data: SeedData, add_new_product):
    res = client.get(
        url="/product/"+test_data.product_id[0],
        headers={"Authorization": f"Bearer {test_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
    assert res.json()["name"] == "clean code"


def test_remove_product(client: TestClient, seed_data: SeedData, add_new_product):
    res = client.delete(
        url="/product/remove/"+test_data.product_id[0],
        headers={"Authorization": f"Bearer {test_data.users_tokens[0]}"},
    )
    assert res.status_code == 200

