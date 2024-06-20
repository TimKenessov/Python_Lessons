from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
   
wait = WebDriverWait(driver, 10, 0.1)
wait.until(EC.text_to_be_present_in_element((By.ID, 'text'), 'Done!'))
    

image = driver.find_element(By.ID, 'award')

src = image.get_attribute("src")

print(src)