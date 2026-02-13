import requests

HOST = "https://reqres.in"
USER = 2

def test_get_user(client: requests.Session):
    r = client.get(f"{HOST}/api/users/{USER}")
    assert r.status_code == 200

    data = r.json().get("data")
    assert data
    assert data["id"] == USER
    assert data["email"]
    assert data["first_name"]
    assert data["last_name"]


def test_create_user(client: requests.Session):
    payload = {"name": "morpheus", "job": "leader"}
    r = client.post(f"{HOST}/api/users", json=payload)

    assert r.status_code in (200, 201)

    body = r.json()
    assert body.get("name") == payload["name"]
    assert body.get("job") == payload["job"]
    assert body.get("id") or body.get("createdAt")


def test_update_user(client: requests.Session):
    payload = {"name": "morpheus", "job": "zion resident"}
    r = client.put(f"{HOST}/api/users/{USER}", json=payload)

    assert r.status_code in (200, 204)

    if r.status_code == 200 and r.text.strip():
        body = r.json()
        assert body.get("name") == payload["name"]
        assert body.get("job") == payload["job"]
        assert body.get("updatedAt")


def test_delete_user(client: requests.Session):
    r = client.delete(f"{HOST}/api/users/{USER}")
    assert r.status_code in (200, 202, 204)

    if r.status_code == 204:
        assert r.text == ""
