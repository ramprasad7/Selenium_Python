from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver: webdriver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(f"url = {driver.current_url}")
print(f"Title = {driver.title}")

#locators are used to identify the input boxes on a web page
#to get the locators info we can do inspect elements on the webpage
#typical locators are NAME, ID , Xpath, CSSSelector, Classname, LinkText

driver.find_element(By.NAME,"email").send_keys("bandiramprasad7@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("hello123")
driver.find_element(By.ID,"exampleCheck1").click()

#XPath syntax: //tagname[@attribute='value']
#CSSSelector syntax: tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR,"input[name='name']").clear()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Ram Prasad")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success!" in message

#select class is used for static drop down menus
static_dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
static_dropdown.select_by_index(0)
time.sleep(1)
static_dropdown.select_by_visible_text("Female")

time.sleep(2)