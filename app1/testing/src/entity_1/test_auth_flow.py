from fastapi.testclient import TestClient
from ...conftest import data as test_data
from ...data import SeedData


def test_user_info(client: TestClient, seed_data: SeedData):
    res = client.get(
        url="/user/me",
        headers={"Authorization": f"Bearer {test_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
    assert res.json()["first_name"] == "hana"

    res = client.get(
        url="/user/me",
        headers={"Authorization": f"Bearer {test_data.users_tokens[1]}"},
    )
    assert res.status_code == 200
    assert res.json()["first_name"] == "saad"


def test_list_user_info(client: TestClient, seed_data: SeedData):
    res = client.get(
        url="/user/",
    )
    assert res.status_code == 200
    assert len(res.json()) == 2

def test_update_user_info(client: TestClient, seed_data: SeedData):
    res = client.patch(
        url="/user",
        json={"first_name": "hana",
              "last_name": "saad",
              "nationality": "saudi",
              "bio": "hana@bio.com",
              "email": "hana@hotmail.com",
              },
        headers={"Authorization": f"Bearer {test_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
