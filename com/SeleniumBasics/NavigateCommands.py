import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("https://zeenyx.com/")

time.sleep(3)
driver.get('https://matryxsoft.com/')
time.sleep(5)
print(driver.title) # Title of the page
print(driver.current_url)

#---------Navigating commands--------------
driver.back()
print(driver.title) # Title of the page

driver.forward()
print(driver.title) # Title of the page

#---------------------Conditional Commands in python---------------------------
'''
is_displayed()
is_enabled()
is_slected()

ele = driver.find_element_by_class_name('username')
ele.is_enabled()
ele.is_displayed()
print(ele.is_selected()) ------>>>> U can verify and u can print, it ll give u a boolean value
'''







#print(driver.page_source) # gives the HTML source code
time.sleep(2) # sleep on python
driver.close() # Close the  cureently  focused browser
driver.quit() # closes all the browser
