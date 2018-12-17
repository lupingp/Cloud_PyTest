# -*- coding: utf-8 -*-
# @Time    : 2018/12/13  14:53
# @Author  : 陆平！！
# @FileName: conftest.py
# @Software: PyCharm

import pytest
from Cloud_PyTest.pytest_rusi.page.whrw_page import _login_whrw_1,_login_whrw_2
from Cloud_PyTest.pytest_rusi.page.login_page import _login_One

@pytest.fixture(scope="function")
def login_whrw_1(driver):
    _login_whrw_1(driver)

@pytest.fixture(scope="function")
def login_whrw_2(driver):
    _login_whrw_2(driver)

@pytest.fixture(scope="function")
def login_One(driver,host):
    _login_One(driver,host)
