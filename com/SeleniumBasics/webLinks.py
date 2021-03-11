import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
print(driver.title)

links = driver.find_elements(By.TAG_NAME, 'a')
print('Number of links present: ', len(links)) # print how many links present in a page

for link in links:
    print(link.text)

#Click on the link
#driver.find_element(By.LINK_TEXT,'REGISTER').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'REG').click()

driver.quit()
print('Completed')





