import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
print(driver.title)

ele_Txt_Inputboxes = driver.find_elements(By.CLASS_NAME,'text_field')
print(len(ele_Txt_Inputboxes)) # Count of text fileds in websites


#Provide data to the text box
ele_Txt_FirstName = driver.find_element(By.ID,'RESULT_TextField-1').send_keys('vidya')


#Status of text fields
ele_Txt_LastName_status = driver.find_element(By.ID,'RESULT_TextField-2').is_enabled()
ele_Txt_LastName_status1 = driver.find_element(By.ID,'RESULT_TextField-2').is_displayed()
print('Enabled or Not: ', ele_Txt_LastName_status1)
print('Displayed or Not: ',ele_Txt_LastName_status) # status true or false


driver.quit()