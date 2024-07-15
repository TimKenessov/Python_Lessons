from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Con

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/entry_ad')

wait = WebDriverWait(driver, 10)
button = wait.until(Con.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer")))
sleep(2)
button.click()
sleep(2)