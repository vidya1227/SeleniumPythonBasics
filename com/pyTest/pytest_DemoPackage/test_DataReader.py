import pytest
from com.pyTest.pytest_FrameworkDemo.conftest import dataLoad


@pytest.mark.usefixtures("dataLoad")
class TestDataReaders:


    def test_MethodDemos(self, dataLoad):
        print(dataLoad)
        print('its a data reader method')
        print(dataLoad[0])
        print(dataLoad[-1])

