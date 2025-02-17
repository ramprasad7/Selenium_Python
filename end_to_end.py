import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver: webdriver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Shop").click()

products = driver.find_elements(By.XPATH,"//div/div/app-card-list/app-card")

#print(products)

for product in products:
    item = product.find_element(By.XPATH,"div/div/h4/a").text
    if item == "Blackberry":
        product.find_element(By.XPATH,"div/div/button").click()
        break

driver.find_element(By.CSS_SELECTOR,".btn-primary").click()
driver.find_element(By.CSS_SELECTOR,".btn-success").click()
driver.find_element(By.CSS_SELECTOR,".validate").send_keys("Ind")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"label[for='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()

output: str = driver.find_element(By.CSS_SELECTOR,".alert").text

assert "Success!" in output
print(output)

driver.close()
#time.sleep(2)
