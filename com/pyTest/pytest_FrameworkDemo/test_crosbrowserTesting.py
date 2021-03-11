import pytest

## data driven and parameterizition can be done with the return staetments in list and tuple formats,
# When you define fixture scope to class only , it will run once before class is intiated and at the end

def test_method1(setup):
    print('This is test method 1...')


def test_method2(setup):
    print('This is test method 2...')


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])



