from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


    
driver = webdriver.Chrome()  
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    
        
delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
delay_input.clear()
delay_input.send_keys("45")
        
        
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

        
sleep(45)

        
result = driver.find_element(By.CSS_SELECTOR, ".screen").text
assert result == "15" 
print(result)
  
driver.quit()

