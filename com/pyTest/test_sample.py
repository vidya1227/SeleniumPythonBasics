import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
    driver.maximize_window()
    print(driver.title)  # Title of the page
    yield
    driver.quit()


def test_validLogin(test_setup):
    driver.get("http://demoaut.katalon.com/")
    # ---------->>Home page Click on make appointment button , it ll navigate to login page
    print('Navigate to the login page')
    ele_Btn_MakeAppointment = driver.find_element_by_xpath('//*[@id="btn-make-appointment"]').click()
    print('Navigation is successfull')
    # Login to the website ------>>> Login page --->> LOgin with username and password
    print('Login as User to the application')
    ele_Txt_Username = driver.find_element_by_xpath('//*[@id="txt-username"]').send_keys('John Doe')
    ele_Txt_Password = driver.find_element_by_xpath('//*[@id="txt-password"]').send_keys('ThisIsNotAPassword')
    ele_Btn_Login = driver.find_element_by_xpath('//*[@id="btn-login"]').click()
    print('Login is successfull!')


# def test_teardown():
#     driver.close() # Close the  cureently  focused browser
#     driver.quit() # closes all the browser

print('Test completed Successfully')
