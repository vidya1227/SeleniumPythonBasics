import os
import time
import pytest
import logging
from selenium import webdriver
import selenium.webdriver
# Import Report Portal logger and handler to the test module.
from com.pyTest.pytest_FrameworkDemo.rp_logging import RPLogger, RPLogHandler


# Setting up a logging.

@pytest.fixture()
def setup():
    print('I will be executing first')
    yield
    print('I executed at last')


driver = None
browser = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    # 失败截图
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = "screenshots" + os.sep + time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(self, name):
    self.driver.get_screenshot_as_file(name)


@pytest.fixture(scope='class')
def setup1():
    print('I will be executing first -- setup1')
    yield
    print('I executed at last -- setup1')


@pytest.fixture(scope="session")
def rp_logger(request):
    logging.setLoggerClass(RPLogger)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # Create handler for Report Portal.
    rp_handler = RPLogHandler(request.node.config.py_test_service)
    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.INFO)
    return logger


@pytest.fixture()
def dataLoad():
    print('user names data is being created')
    return ['vidya', 'pavani', 'hema', 'chandana', 'krutika']


@pytest.fixture(params=[('chrome', 'URL', 'Username', 'password'), ('firefox', 'URL'), 'IE'])
def crossBrowser(request):
    print('cross browser method')
    return request.param
