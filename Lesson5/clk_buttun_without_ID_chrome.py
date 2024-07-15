from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

click = 0
driver.get('https://uitestingplayground.com/dynamicid')


button = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()

for x in range(3):
    button = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    click = click + 1
    sleep(5)
    print(click)

