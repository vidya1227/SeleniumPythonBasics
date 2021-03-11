import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


class TestBase:

    # def __init__(self, driver):
    #     self.driver = driver

    @pytest.fixture()
    def setup(self):
        print('Launching Browser')
        self.driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
        self.driver.get("http://demoaut.katalon.com/")
        self.driver.maximize_window()
        print('Browser launched')
        print(self.driver.title)  # Title of the page
        yield
        self.driver.close()
        print('Browser is closed')

    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(self,item):
        """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                file_name =os.path.join(os.path.abspath(os.pardir), 'Screenshots\\Snapshots12.png')
                self.driver.save_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra