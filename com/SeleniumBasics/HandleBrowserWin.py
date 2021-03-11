import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
print(driver.title)

#-----------Working with handle browser in windows in pyhton
# driver.current_window_handle
# driver.window_handles

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

print(driver.current_window_handle) # gives windows in name - parent

handles = driver.window_handles # returns all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.quit()
print('completed')
