import pytest
from conftest import ScopedSession, base_db  # type: ignore
from fastapi.testclient import TestClient
from .data import SeedData

data = SeedData()

@pytest.fixture()
def seed_data(client: TestClient):
    print('<=======> scope="session" <=======>')

    for user in data.users:
        client.base_url="http://localhost:3001"
        response = client.post("/user/signup", json=user)
        print(response.request.url)
        assert response.status_code == 200
        data.users_id.append(response.json()["id"])

        response = client.post("/user/login",
            json={
            "username": user.get("username"),
            "password": user.get("password")
        })
        assert response.status_code == 200
        data.users_tokens.append(response.json()["access_token"])

    print(f"{len(data.users)} users has been created")

    print('<=======> scope="session" <=======>')

