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

try:
    # Working with radio buttons-------------------------------------------------------------
    rBtn_Satus_male = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
    print(rBtn_Satus_male)  # True/False

    driver.find_element_by_id('RESULT_RadioButton-7_0').click()

    rBtn_Satus_male1 = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
    print(rBtn_Satus_male1)  # True/False
except:
    print("Not Worked")

try:
    # ----------Working with Check boxes -------------------------------------------------------------
    driver.find_element_by_id('RESULT_CheckBox-8_0').click()  # sunday
    Chk_status = driver.find_element_by_id('RESULT_CheckBox-8_6').is_selected()  # saturday
    print(Chk_status)
except:
    print('Not worked')


driver.quit()