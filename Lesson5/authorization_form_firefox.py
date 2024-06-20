from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/login")

login = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

login.send_keys('tomsmith')
sleep(1)

password.send_keys('SuperSecretPassword!')
sleep(1)

button = driver.find_element(By.XPATH, '//button[@type="submit"]')
button.click()
sleep(2)

driver.quit()