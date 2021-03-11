import pytest


@pytest.mark.smoke
def test_secondProgram():
    msg = 'Hello'
    assert msg == 'Hello', ' Test failed because strings do not match'
    print('Good morning')


def test_firstProgram(): # test case name is represents the method name
    a = 4
    b = 6
    assert a+2 == 6, 'Addition do not match'
    print('Hello first program')
    print('Hi pytest method')

# Run using command ---->> py.test -m smoke -v -s test_Demo3 (or) py.test -m smoke -v -s
# you can mark (tag) tests @pytest.mark.smoke and run with -m