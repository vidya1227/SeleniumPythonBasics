import allure
import time
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pytest

@allure.severity(allure.severity_level.MINOR)
class Test_DemoWebsites:
    def test_login(self):
        self.driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        status = self.driver.find_element_by_xpath('//*[@id="divLogo"]/img').is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_UnderImplement(self):
        pytest.skip("skipping test.....Later I'll implement")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_ValidLogin(self):
        self.driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
        self.driver.maximize_window()
        act_title=self.driver.title  # Title of the page
        self.driver.get("http://demoaut.katalon.com/")
        # ---------->>Home page Click on make appointment button , it ll navigate to login page
        print('Navigate to the login page')
        ele_Btn_MakeAppointment = self.driver.find_element_by_xpath('//*[@id="btn-make-appointment"]').click()
        print('Navigation is successfull')
        # Login to the website ------>>> Login page --->> LOgin with username and password
        print('Login as User to the application')
        ele_Txt_Username = self.driver.find_element_by_xpath('//*[@id="txt-username"]').send_keys('John Doe')
        ele_Txt_Password = self.driver.find_element_by_xpath('//*[@id="txt-password"]').send_keys('ThisIsNotAPassword')
        ele_Btn_Login = self.driver.find_element_by_xpath('//*[@id="btn-login"]').click()
        print('Login is successfull!')
        print(act_title)
        if act_title=='act_title':
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='testScreen',attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
