from pages.base_page import BasePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from selenium import webdriver
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


fake = Faker('en_US')
first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.postalcode()


def test_add_clothes(driver):
    base_page = BasePage(driver)
    base_page.open('https://www.saucedemo.com/')
    base_page.login('standard_user', 'secret_sauce')
    products_page = ProductsPage(driver)
    products_page.add_items_to_cart('backpack', 'tshirt', 'onesie')
    products_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout_button()
    cart_page.enter_customer_info(first_name, last_name, postal_code)
    cart_page.submit_customer_info()

    WebDriverWait(
        driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div.summary_total_label')))
    total_label = driver.find_element(
        By.CSS_SELECTOR, 'div.summary_total_label')
    assert total_label.text == "Total: $58.29"
