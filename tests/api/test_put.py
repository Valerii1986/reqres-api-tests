import requests

BASE_URL = "https://reqres.in"
USER_ID = 2


def test_update_user(api_client: requests.Session):
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = api_client.put(f"{BASE_URL}/api/users/{USER_ID}", json=payload)

    assert response.status_code in (200, 204)

    if response.status_code == 200:
        body = response.json()
        assert body["name"] == payload["name"]
        assert body["job"] == payload["job"]
        assert "updatedAt" in body
