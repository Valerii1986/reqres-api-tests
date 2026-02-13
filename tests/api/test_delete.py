import requests

BASE_URL = "https://reqres.in"
USER_ID = 2


def test_delete_user(api_client: requests.Session):
    response = api_client.delete(f"{BASE_URL}/api/users/{USER_ID}")

    assert response.status_code in (200, 202, 204)

    if response.status_code == 204:
        assert response.text == ""
