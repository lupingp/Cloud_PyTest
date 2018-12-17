# -*- coding: utf-8 -*-
# @Time    : 2018/11/30  13:05
# @Author  : 陆平！！
# @FileName: conftest.py.py
# @Software: PyCharm

import pytest
from Cloud_PyTest.pytest_rusi.page.login_page import _login_One
from Cloud_PyTest.pytest_rusi.page.wdjqr_page import _login_wdjqr_1,_login_wdjqr_2,_login_wdjqr_3,_login_wdjqr_4,_login_wdjqr_5,\
    _login_wdjqr_6,_login_wdjqr_7

@pytest.fixture(scope="function")
def login_wdjqr_1(driver):
    _login_wdjqr_1(driver)

@pytest.fixture(scope="function")
def login_wdjqr_2(driver):
    _login_wdjqr_2(driver)

@pytest.fixture(scope="function")
def login_wdjqr_3(driver):
    _login_wdjqr_3(driver)

@pytest.fixture(scope="function")
def login_wdjqr_4(driver):
    _login_wdjqr_4(driver)

@pytest.fixture(scope="function")
def login_wdjqr_5(driver):
    _login_wdjqr_5(driver)

@pytest.fixture(scope="function")
def login_wdjqr_6(driver):
    _login_wdjqr_6(driver)

@pytest.fixture(scope="function")
def login_wdjqr_7(driver):
    _login_wdjqr_7(driver)

@pytest.fixture(scope="function")
def login_One(driver,host):
    _login_One(driver,host)