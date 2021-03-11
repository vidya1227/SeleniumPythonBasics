import pytest

@pytest.fixture()
def setup():
    print('setup: method once before every test method')


def test_method1(setup):
    print('This is test method 1...')


def test_method2(setup):
    print('This is test method 2...')

