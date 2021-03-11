import time
from selenium.webdriver.remote.webdriver import WebDriver
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
print(driver.title)

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()

time.sleep(3)

#driver.switch_to_alert().accept() # close alert window using OK button
driver.switch_to_alert().dismiss() #closes alert by using cancel button
driver.quit()
print('completed')