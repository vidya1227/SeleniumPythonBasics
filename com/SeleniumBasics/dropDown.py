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

#Dropdown Selection in python selenium
ele_dropDown_bestTime = driver.find_element_by_id('RESULT_RadioButton-9')
dropDown = Select(ele_dropDown_bestTime)

#Select by visible text
#dropDown.select_by_visible_text('Morning')

#select by index
#dropDown.select_by_index(2)

#Select by using value
dropDown.select_by_value('Radio-1')

#Count number of options in drop down
print(len(dropDown.options))

# Capture all the options and print them as output
all_options = dropDown.options

for option in all_options:
    print(option.text)

print('Completed')





