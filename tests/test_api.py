import allure
import logging
import requests
from allure_commons._allure import step
from tests.conftest import LOGIN, PASSWORD, API_URL
from selene import browser, have, be
from utils_api.utils import post_reqres


def test_login(setup_browser):
    with step("Authorization with API"):
        response = post_reqres("/login", json={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    logging.info(cookie)
    assert response.status_code == 302
    with step("Open main page with authorized user"):
        browser.open(API_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.element('.ico-login').click()
        browser.element(".page-title").should(have.text('Welcome, Please Sign In!'))


def test_add_product():
    response = post_reqres("/login", json={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    logging.info(cookie)
    browser.open(API_URL)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    with step("Open main page with authorized user"):
        post_reqres("/addproducttocart/details/74/1",
                    data={
                        "addtocart_74.EnteredQuantity": 1})
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    logging.info(cookie)
    assert response.status_code == 302
    with step("Add product in card UI"):
        browser.open(f"{API_URL}/desktops")
        browser.element('.product-box-add-to-cart-button').click()
        browser.element(".product-name").should(have.text('Build your own cheap computer'))

