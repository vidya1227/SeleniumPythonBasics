import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

#Implicit wait
driver.implicitly_wait(10) # seconds
#Implicit wait will consider to all the pages and elements in code or script

print(driver.title)
assert "Welcome: Mercury Tours" in driver.title # Title of the page

#Login to the website ------>>> Login page --->> LOgin with username and password
print('Login as User to the application')
ele_Txt_Username = driver.find_element_by_name('userName').send_keys('mercury')
ele_Txt_Password = driver.find_element_by_name('password').send_keys('mercury')
ele_Btn_Login = driver.find_element_by_name('login').click()
print('Login is successfull!')

driver.close()