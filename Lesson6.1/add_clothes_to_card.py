from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep




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


driver.find_element(By.CSS_SELECTOR, 'button[id="checkout').click()
sleep(2)


first_name = driver.find_element(By.CSS_SELECTOR, 'input[id="first-name"]')
last_name = driver.find_element(By.CSS_SELECTOR, 'input[id="last-name"]')
postal_code = driver.find_element(By.CSS_SELECTOR, 'input[id="postal-code"]')

first_name.send_keys('Tim')
last_name.send_keys('Kenessov')
postal_code.send_keys('9379992')
sleep(1)


driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
sleep(2)


test_comparison = driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]')
assert test_comparison.text == "Total: $58.29" 
print(test_comparison.text)

driver.quit()