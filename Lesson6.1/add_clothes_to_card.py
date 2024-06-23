from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from faker import Faker


fake = Faker('en_US')

first_name = fake.first_name()
last_name = fake.last_name()
postalcode = fake.postalcode()

driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')

user = driver.find_element(By.CSS_SELECTOR, '#user-name')
password = driver.find_element(By.CSS_SELECTOR, '#password')

user.send_keys('standard_user')
password.send_keys('secret_sauce')
# password.send_keys(Keys.RETURN)
sleep(2)

driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

backpack = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
backpack.click()
sleep(1)

tshirt = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
tshirt.click()
sleep(1)

onesie = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
onesie.click()
sleep(1)

driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]').click()
sleep(2)

driver.find_element(By.ID, 'checkout').click()
sleep(2)

first_name_input = driver.find_element(By.ID, 'first-name')
last_name_input = driver.find_element(By.ID, 'last-name')
postal_code_input = driver.find_element(By.ID, 'postal-code')

first_name_input.send_keys('first_name')
last_name_input.send_keys('last_name')
postal_code_input.send_keys('postal_code')
sleep(1)

driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
sleep(2)

test_comparison = driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]')
assert test_comparison.text == "Total: $58.29" 
print(test_comparison.text)

driver.quit()


    