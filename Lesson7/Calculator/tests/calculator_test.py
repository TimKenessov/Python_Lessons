from pages.base_page import BasePage
from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator_page = BasePage(driver)
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    calculator_page.set_time('45')
    calculator_page.test_addition()
    assert '15' in calculator_page.result()
