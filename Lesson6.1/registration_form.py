from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

first_name = driver.find_element(By.NAME, "first-name").send_keys("Иван")
last_name = driver.find_element(By.NAME, "last-name").send_keys("Петров")
address = driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
e_mail = driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
phone = driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
city = driver.find_element(By.NAME, "city").send_keys("Москва")
country = driver.find_element(By.NAME, "country").send_keys("Россия")
job_position = driver.find_element(By.NAME, "job-position").send_keys("QA")
company = driver.find_element(By.NAME, "company").send_keys("SkyPro")


driver.find_element(By.XPATH, "//button[text()='Submit']").click()
sleep(2)


zip_code_field = driver.find_element(By.CLASS_NAME, "alert-danger")
zip_code_color = zip_code_field.value_of_css_property("background-color")
assert zip_code_color == zip_code_color 
print(zip_code_color)


green_fields_ids = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country', 'job-position', 'company']
for field_id in green_fields_ids:
        field = driver.find_element(By.ID, field_id)
        field_color = field.value_of_css_property("background-color")
        assert field_color == field_color 
        print(field_color)

driver.quit()
