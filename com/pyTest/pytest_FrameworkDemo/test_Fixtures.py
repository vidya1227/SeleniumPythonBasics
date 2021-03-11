import pytest

# fixtures are used as setup and teardown methods for test cases- conftest file to generalize fixtures
# and make it available to all test cases

def test_method1(setup):
    a=4
    b=5
    assert a+2 == 6, "addition do not match"

def test_fixtureDemo(setup):
    print('I will execute steps in fixture demo method')