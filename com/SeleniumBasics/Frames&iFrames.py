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
from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.maximize_window()
print(driver.title)

driver.switch_to.default_content()

driver.switch_to.frame('packageFrame') # Second Frame
driver.find_element_by_link_text('webDriver').click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.default_frame('classFrame') # third frame
driver.find_element_by_xpath('/html/body/div[1]/ul/li[5]').click()

#----Working with Frames---------
# switch_to_frame(name)
# switch_to_frame(id)

driver.quit()
print('completed')