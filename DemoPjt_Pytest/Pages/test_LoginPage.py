

class TestLoginPage:
    ele_Txt_Username_xpath = '//*[@id="txt-username"]'
    ele_Txt_Password_xpath = '//*[@id="txt-password"]'
    ele_Btn_Login_xpath = '//*[@id="btn-login"]'
    # self.iWait_time_out = 5


    def __init__(self, driver):
        self.driver = driver
        # self.wait_variable = wait(self.driver, self.iWait_time_out)

    def test_LoginToApplication(self, sUsername, sPassword):
        self.driver.find_element_by_xpath(self.ele_Txt_Username_xpath).send_keys(sUsername)
        self.driver.find_element_by_xpath(self.ele_Txt_Password_xpath).send_keys(sPassword)
        self.driver.find_element_by_xpath(self.ele_Btn_Login_xpath).click()