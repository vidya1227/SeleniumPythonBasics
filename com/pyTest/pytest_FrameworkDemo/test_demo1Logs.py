# Any pytest file should start with test_---name---.py
# pytest method names should start with test
# pytest methods will wrapped by pytest plugins -- Any code should be wrapped in method only
# configure in pytest and run the pytest scripts
import logging
import pytest
import pytest_html
import logging as L


LOGGER = logging.getLogger(__name__)

def test_firstProgram():
    print('Hello first program')
    print('Hi pytest method')
    # U.log('INFO', 'pass message')


def test_secondProgram():
    msg = 'Hello'
    assert msg == 'Hello', ' Test failed because strings do not match'
    print('Good morning')


def test_thirdProgramForLogs():
    logging.info(' hi info')
    logging.warning('hi warning')
    logging.debug('hi debug')
    logging.error('hi error')
    logging.critical('hi critical')
    logging.exception('hi exception')


def test_fourthProgramsForConfigLogs():
    filename = 'E:\\text.txt'
    L.basicConfig(level=L.DEBUG)
    L.debug('hi debug after config')
    L.info('hi info after config')
    L.warning('hi warning after config')
    L.error('hi error after config')
    L.critical('hi critical after config')
    L.exception('hi exception after config')
    test_Logs('INFO', 'pass info', filename)

    test_Logs('DEBUG', 'pass debug', filename)


def test_Logs(level, message, file):
    L.basicConfig(level=L.DEBUG, filename=file, filemode='a',
                  format='%(asctime)-12s%(lelvelname)s%(message)s',
                  datefmt='%d-%m-%y %H:%M:%S')
    if level == 'INFO': L.info(message)
    if level == 'WARNING': L.warning(message)
    if level == 'ERROR': L.error(message)
    if level == 'CRITICAL': L.critical(message)
    if level == 'DEBUG': L.debug(message)


def test_logsdemo():
    print('Hi logs')
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    LOGGER.critical('eggs critical')
    assert True

# def test_launch_success(rp_logger):
#     rp_logger.info("A GUI test. Launch Qxf2.com")

# >>> py.test -k first -v -s  (-k stands for method names execution, -s gives logs in output, -v stands for more info meta data)
# >> py.test test_Demo1.py::test_firstProgram
# >> pytest -v -s -path of package-     -----------------> For complete package execution
# >> pytest -v -s test_Demo1.py >>>>>>> you can run specific file with py.test <filename>
