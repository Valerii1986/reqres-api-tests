LOGIN_URL = "https://the-internet.herokuapp.com/login"
VALID_USER = "tomsmith"
VALID_PASS = "SuperSecretPassword!"


def test_login_success(page):
    page.goto(LOGIN_URL)

    page.locator("#username").fill(VALID_USER)
    page.locator("#password").fill(VALID_PASS)
    page.locator("button[type='submit']").click()

    flash = page.locator("#flash")

    assert flash.is_visible()
    assert "You logged into a secure area!" in flash.inner_text()


def test_login_invalid(page):
    page.goto(LOGIN_URL)

    page.locator("#username").fill("wrong")
    page.locator("#password").fill("wrong")
    page.locator("button[type='submit']").click()

    flash = page.locator("#flash")

    assert flash.is_visible()
    assert "Your username is invalid!" in flash.inner_text() or \
           "Your password is invalid!" in flash.inner_text()
