import pytest


# you can skip tests with @pytest.mark.skip
# @pytest.mark.xfail
@pytest.mark.regression
#@pytest.mark.skip
def test_secondProgram():
    msg = 'Hello'
    assert msg == 'Hello', ' Test failed because strings do not match'
    print('Good morning')


@pytest.mark.xfail
def test_firstProgram():  # test case name is represents the method name
    a = 4
    b = 6
    assert a + 2 == 6, 'Addition do not match'
    print('Hello first program')
    print('Hi pytest method')

# py.test -k first -v -s  -----> to run test which are contains the  first in test method names
# py.test -m regression -v -s
