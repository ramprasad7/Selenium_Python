from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver: webdriver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
print(f"url = {driver.current_url}")
print(f"Title = {driver.title}")

time.sleep(2)
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries: driver = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

assert "India" == driver.find_element(By.ID,"autosuggest").get_attribute("value")



time.sleep(2)