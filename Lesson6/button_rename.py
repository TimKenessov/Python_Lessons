from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://uitestingplayground.com/textinput')

input_text = driver.find_element(By.CSS_SELECTOR, '#newButtonName')

input_text.send_keys('SkyPro')

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
button.click()

new_text = button.text

print(new_text)