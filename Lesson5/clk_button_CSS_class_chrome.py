from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()


driver.get('https://uitestingplayground.com/classattr')

for x in range(3):
        button = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        button.click()
        sleep(5)
        driver.switch_to.alert.accept()