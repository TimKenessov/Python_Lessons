from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/inputs')

field = driver.find_element(By.TAG_NAME, 'input')

field.send_keys(1000)
sleep(1)

field.clear()
sleep(1)

field.send_keys(999)
sleep(1)