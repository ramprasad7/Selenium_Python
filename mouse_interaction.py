from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver: webdriver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)
#action.double_click()
#action.click_and_hold()
#action.context_click() right click
action.move_to_element(driver.find_element(By.CSS_SELECTOR,".mouse-hover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top").click()).perform()
action.click(driver.find_element(By.LINK_TEXT,"Reload").click()).perform()

time.sleep(2)