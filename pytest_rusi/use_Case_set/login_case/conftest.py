import pytest
from pytest_rusi.page.login_page import _login,_login_submit_result_error,_login_pwd_result_error,_login_user_result_error

"""
登录功能调用
"""

@pytest.fixture(scope='session')
def login(driver, host):
    """登录功能fixture"""
    _login(driver, host)

@pytest.fixture(scope='session')
def login_user_result_error(driver):
    '''
    :param driver: 调用登录函数里定义的login_user_result_error方法
    :return:
    '''
    _login_user_result_error(driver)

@pytest.fixture(scope='session')
def login_pwd_result_error(driver):
    '''
    :param driver: 调用登录函数里定义的_login_pwd_result_error方法
    :return:
    '''
    _login_pwd_result_error(driver)

@pytest.fixture(scope='session')
def login_submit_result_error(driver):
    '''
    :param driver: 调用登录函数里定义的_login_submit_result_error方法
    :return:
    '''
    _login_submit_result_error(driver)