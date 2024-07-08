from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.NAME, "first-name")
        self.last_name_input = (By.NAME, "last-name")
        self.address_input = (By.NAME, "address")
        self.e_mail_input = (By.NAME, "e-mail")
        self.phone_input = (By.NAME, "phone")
        self.city_input = (By.NAME, "city")
        self.country_input = (By.NAME, "country")
        self.job_position_input = (By.NAME, "job-position")
        self.company_input = (By.NAME, "company")
        self.button = (By.XPATH, "//button[text()='Submit']")

    def first_name(self, term):
        self.driver.find_element(*self.first_name_input).send_keys(term)

    def last_name(self, term):
        self.driver.find_element(*self.last_name_input).send_keys(term)

    def address(self, term):
        self.driver.find_element(*self.address_input).send_keys(term)

    def e_mail(self, term):
        self.driver.find_element(*self.e_mail_input).send_keys(term)

    def phone(self, term):
        self.driver.find_element(*self.phone_input).send_keys(term)

    def city(self, term):
        self.driver.find_element(*self.city_input).send_keys(term)

    def country(self, term):
        self.driver.find_element(*self.country_input).send_keys(term)

    def job_position(self, term):
        self.driver.find_element(*self.job_position_input).send_keys(term)

    def company(self, term):
        self.driver.find_element(*self.company_input).send_keys(term)

    def button_submit(self):
        self.driver.find_element(*self.button).click()
