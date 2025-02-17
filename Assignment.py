from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import re

driver: webdriver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".blinkingText").click()

windows: list = driver.window_handles

driver.switch_to.window(windows[1])
#phrase: str = driver.find_element(By.CSS_SELECTOR,".red").text
mail: str = driver.find_element(By.CSS_SELECTOR,"strong a").text
password: str = "12345"
#mail = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", phrase)
#print(mail)
#mail: str = phrase.split("at")[1].strip().split()[0]
print(mail)

driver.close()

driver.switch_to.window(windows[0])
driver.find_element(By.CSS_SELECTOR,"input[name='username']").send_keys(mail)
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys(password)
#driver.find_element(By.CSS_SELECTOR,"//input[@value='admin']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()

driver.find_element(By.XPATH,"//input[@type='submit']").click()

wait = WebDriverWait(driver,12) #explicit wait
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
print(driver.find_element(By.CSS_SELECTOR,".alert").text)


