import os
import pathlib
import datetime
from datetime import datetime


class TestMainPage:
    def __init__(self, driver):
        self.driver = driver

    ele_Btn_MakeAppointment_xpath = '//*[@id="btn-make-appointment"]'
    ele_MenuItem_xpath = '//*[@id="menu-toggle"]'
    ele_LoginOption_xpath = '//*[@id="sidebar-wrapper"]/ul/li[3]/a'

    def test_ClickOnMakeAppointment(self):
        try:
            now = datetime.now()
            print(now)
            self.driver.find_element_by_xpath(self.ele_Btn_MakeAppointment_xpath).click()
            self.driver.save_screenshot(os.path.join(os.path.abspath(os.pardir), 'Screenshots\\Snapshots9.png'))
            files = os.path.join(os.path.abspath(os.pardir), 'Screenshots')
            print(files + '--->>>>hello my path is')
        except:
            print('Catch')

        # print('hi hello')
        # self.driver.find_element(By.XPATH(self.ele_Btn_MakeAppointment_xpath)).click()
        # self.driver.find_element(By.XPATH('//*[@id="btn-make-appointment"]')).click()
        # self.driver.find_element_by_xpath('//*[@id="btn-make-appointment"]').click()

    def test_NavigateToLoginPage(self):
        # self.driver.find_element(By.XPATH(self.ele_MenuItem_xpath)).click()
        # self.driver.find_element(By.XPATH(self.ele_LoginOption_xpath)).click()
        self.driver.find_element_by_xpath(self.ele_MenuItem_xpath).click()
        self.driver.find_element_by_xpath(self.ele_LoginOption_xpath).click()
