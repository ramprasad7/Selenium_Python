from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver: webdriver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
#time.sleep(2)
driver.find_element(By.LINK_TEXT,"Click Here").click()

windows = driver.window_handles

driver.switch_to.window(windows[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()

driver.switch_to.window(windows[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text

