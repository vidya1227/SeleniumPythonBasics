import pytest


# fixtures are used as setup and teardown methods for test cases- conftest file to generalize fixtures
# and make it available to all test cases

# @pytest.mark.usefixtures('setup1')
@pytest.mark.usefixtures('setup')
class TestExample:

    def test_fixtureDemo(self):
        print('I will execute steps in fixture demo method')

    def test_fixtureDemo1(self):
        print('I will execute steps in fixture demo 1 method')

    def test_fixtureDemo2(self):
        print('I will execute steps in fixture demo 2 method')

    def test_fixtureDemo3(self):
        print('I will execute steps in fixture demo 3 method')

    def test_fixtureDemo4(self):
        print('I will execute steps in fixture demo 4 method')

    def test_fixtureDemo5(self):
        print('I will execute steps in fixture demo 5 method')
