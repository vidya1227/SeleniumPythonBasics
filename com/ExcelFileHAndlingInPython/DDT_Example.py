import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from com.ExcelFileHAndlingInPython import XLUtils

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
print(driver.title) # Title of the page

path = 'E:\\DDT_testData_DemoTours.xlsx'
rows= XLUtils.getRowCount(path, 'Sheet1')

for r in range(2, rows+1):
    username = XLUtils.readData(path, 'Sheet1', r,1)
    password = XLUtils.readData(path, 'Sheet1', r, 2)

    driver.find_element_by_name('userName').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)

    driver.find_element_by_name('login').click()
    print(driver.title)

    if driver.title == 'Find a Flight: Mercury Tours:':
        print('Test is Passed')
        XLUtils.writeData(path, 'Sheet1', r, 3, 'Test Passed')
    else:
        print('Test is Failed')
        XLUtils.writeData(path, 'Sheet1', r, 3, 'Test Failed')

    driver.find_element_by_link_text('Home').click()
    print('Test Completed')