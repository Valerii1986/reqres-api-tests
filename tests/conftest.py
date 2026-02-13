import os
import logging
import pytest
import requests

API_KEY = "reqres_e0ae22ab65e2426b953c5dec93d890bd"

log = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def client():
    logging.basicConfig(level=logging.INFO)

    key = os.getenv("REQRES_API_KEY", API_KEY)

    s = requests.Session()
    s.headers.update({
        "Content-Type": "application/json",
        "x-api-key": key,
        "Authorization": "Bearer fake-session-token",
    })

    yield s
    s.close()
