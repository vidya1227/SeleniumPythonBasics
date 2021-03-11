import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("https://www.expedia.com/")
driver.maximize_window()
print(driver.title)

#Explicit Wait
#Explicit will waits on condition
wait = WebDriverWait(driver, 10)

ele_Btn_Flights = driver.find_element(By.ID,'tab-flight-tab-hp')
wait.until(EC.element_to_be_clickable(ele_Btn_Flights))



# Flights button
#ele_Btn_Flights = driver.find_element_by_id('tab-flight-tab-hp').click() #or
#ele_Btn_Flights = driver.find_element(By.ID,'tab-flight-tab-hp').click()

ele_Origin = driver.find_element(By.ID,'flight-origin-hp-flight').send_keys('SFO') # origin

time.sleep(2)

ele_Destination = driver.find_element(By.ID,'flight-destination-hp-flight').send_keys('NYC') # destination

ele_Departing = driver.find_element(By.ID,'flight-departing-hp-flight').clear()
ele_Departing.send_keys('07/12/2020')

ele_Returning = driver.find_element(By.ID,'flight-returning-hp-flight').clear()
ele_Returning.send_keys('07/27/2020')


ele_Flights = driver.find_element(By.XPATH,'//*[@id="gcw-flights-form-hp-flight"]/div[7]/label/button').click()

time.sleep(3)


driver.close()