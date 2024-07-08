from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, 'checkout')
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.postal_code_input = (By.ID, 'postal-code')
        self.submit_button = (By.CSS_SELECTOR, 'input[type="submit"]')

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_customer_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_input).send_keys(postal_code)

    def submit_customer_info(self):
        self.driver.find_element(*self.submit_button).click()
