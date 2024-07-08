from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.CSS_SELECTOR, '#user-name')
        self.password_input = (By.CSS_SELECTOR, '#password')
        self.login_button = (By.CSS_SELECTOR, 'input[type=submit]')

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        user = self.driver.find_element(*self.username_input)
        password_element = self.driver.find_element(*self.password_input)
        user.send_keys(username)
        password_element.send_keys(password)
        self.driver.find_element(*self.login_button).click()
