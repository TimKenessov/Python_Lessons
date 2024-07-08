from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.number_seven = (By.XPATH, "//span[text()='7']")
        self.plus = (By.XPATH, "//span[text()='+']")
        self.number_eight = (By.XPATH, "//span[text()='8']")
        self.equal = (By.XPATH, "//span[text()='=']")
        self.outcome = (By.CSS_SELECTOR, ".screen")

    def set_time(self, delay_input):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(delay_input)

    def test_addition(self):
        self.driver.find_element(*self.number_seven).click()
        self.driver.find_element(*self.plus).click()
        self.driver.find_element(*self.number_eight).click()
        self.driver.find_element(*self.equal).click()

    def result(self):
        WebDriverWait(
            self.driver, 46).until(
            EC.text_to_be_present_in_element(
                self.outcome, '15'))
        return self.driver.find_element(*self.outcome).text
