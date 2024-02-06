import pytest
from selene import browser

LOGIN = "e_nikolaevnaya@mail.ru"
PASSWORD = "e_nikolaevnaya"
WEB_URL = "https://demowebshop.tricentis.com"
API_URL = "https://demowebshop.tricentis.com"


@pytest.fixture(scope='function')
def setup_browser():
    browser.config.window_width = 1080
    browser.config.window_height = 1920
    browser.config.timeout = 10
    browser.config.base_url = 'https://demowebshop.tricentis.com'

    yield browser

    browser.quit()
