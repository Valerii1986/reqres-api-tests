import requests

BASE_URL = "https://reqres.in"


def test_create_user(api_client: requests.Session):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = api_client.post(f"{BASE_URL}/api/users", json=payload)

    assert response.status_code in (200, 201)

    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body
    assert "createdAt" in body
