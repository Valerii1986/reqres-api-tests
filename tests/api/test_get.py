import requests

BASE_URL = "https://reqres.in"
USER_ID = 2


def test_get_user(api_client: requests.Session):
    response = api_client.get(f"{BASE_URL}/api/users/{USER_ID}")

    assert response.status_code == 200

    data = response.json().get("data")
    assert data is not None
    assert data["id"] == USER_ID
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
