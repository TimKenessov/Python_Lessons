from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_filling_fields(driver):
    base_page = BasePage(driver)
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    base_page.first_name('Иван')
    base_page.last_name('Петров')
    base_page.address('Ленина, 55-3')
    base_page.e_mail('test@skypro.com')
    base_page.phone('+7985899998787')
    base_page.city('Москва')
    base_page.country('Россия')
    base_page.job_position('QA')
    base_page.company('SkyPro')
    base_page.button_submit()

    zip_code_field = driver.find_element(By.CLASS_NAME, "alert-danger")
    zip_code_color = zip_code_field.value_of_css_property("background-color")
    assert zip_code_color == zip_code_color
    print(zip_code_color)

    green_fields_ids = [
        'first-name',
        'last-name',
        'address',
        'e-mail',
        'phone',
        'city',
        'country',
        'job-position',
        'company']
    for field_id in green_fields_ids:
        field = driver.find_element(By.ID, field_id)
        field_color = field.value_of_css_property("background-color")
        assert field_color == field_color
        print(field_color)
