import pytest, os
import time
import logging

logging.basicConfig(level=logging.DEBUG)


def test_1():
    log = logging.getLogger('test_1')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    assert 1, 'should pass'


def test_2():
    log = logging.getLogger('test_2')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    assert 0, 'failing for demo purposes'


logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()


#############################################################################

def setup_module(module):
    ''' Setup for the entire module '''
    mylogger.info('Inside Setup')
    # Do the actual setup stuff here
    pass


def setup_function(func):
    ''' Setup for test functions '''
    if func == test_one:
        mylogger.info(' Hurray !!')


def test_one():
    ''' Test One '''
    mylogger.info('Inside Test 1')
    # assert 0 == 1
    pass


def test_two():
    ''' Test Two '''
    mylogger.info('Inside Test 2')
    pass


if __name__ == '__main__':
    mylogger.info(' About to start the tests ')
    pytest.main(args=[os.path.abspath(__file__)])
    mylogger.info(' Done executing the tests ')
