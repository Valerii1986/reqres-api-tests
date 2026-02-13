import os
import logging

import pytest
import requests
from playwright.sync_api import sync_playwright

API_KEY = "reqres_e0ae22ab65e2426b953c5dec93d890bd"

log = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def api_client():
    logging.basicConfig(level=logging.INFO)

    key = os.getenv("REQRES_API_KEY", API_KEY)

    s = requests.Session()
    s.headers.update(
        {
            "Content-Type": "application/json",
            "x-api-key": key,
            "Authorization": "Bearer fake-session-token",
        }
    )

    yield s
    s.close()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        br = p.chromium.launch(headless=True)
        yield br
        br.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    p = context.new_page()
    yield p
    context.close()

