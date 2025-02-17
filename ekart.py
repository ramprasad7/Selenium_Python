from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver: webdriver = webdriver.Chrome()
driver.implicitly_wait(2) #implicit wait
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
#time.sleep(2)
actualCart: list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
products: list = driver.find_elements(By.CSS_SELECTOR, "div[class='product']")
assert len(products) > 0

receivedCart: list = []
for product in products:
    #print(product.find_element(By.CSS_SELECTOR,".product-name").text)
    receivedCart.append(product.find_element(By.CSS_SELECTOR,".product-name").text)
    product.find_element(By.CSS_SELECTOR,"button[type='button']").click()

#print(receivedCart)
assert actualCart == receivedCart

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#total amount validation
prices: webdriver = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
#print(len(prices))
totalAmount: int = 0
for price in prices:
    totalAmount += int(price.text)

#print(totalAmount)
totalCartValue: int = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert totalAmount == totalCartValue


#time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#time.sleep(5)
wait = WebDriverWait(driver,10) #explicit wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

result: str = driver.find_element(By.CSS_SELECTOR,".promoInfo").text

print(result)
assert result == "Code applied ..!"

#checking total after promo applied
discountAmount: float = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
#print(discountAmount)
assert discountAmount < totalCartValue


#time.sleep(2)
