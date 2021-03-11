import logging
from DemoPjt_Pytest.Pages.test_LoginPage import TestLoginPage
from DemoPjt_Pytest.Pages.test_MainPage import TestMainPage
from DemoPjt_Pytest.Pages.test_MainPage import *
from DemoPjt_Pytest.Baseclass.conftest import *
import pytest
import time
import pytest_html
import datetime
import pytest_html_reporter

@pytest.mark.usefixtures('setup')
class TestDemo1(TestBase):

    def test_DemoMethod(self):
        # Step-1
        print('Navigate to login page')
        mainPage = TestMainPage(self.driver)
        mainPage.test_NavigateToLoginPage()
        print('Login page is displayed')

        # Step-2
        print('add values to the username and password')
        loginPage = TestLoginPage(self.driver)
        loginPage.test_LoginToApplication('John Doe', 'ThisIsNotPassword')
        print('Login is successful')