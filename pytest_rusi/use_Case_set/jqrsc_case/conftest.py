# -*- coding: utf-8 -*-
# @Time    : 2018/11/27  15:18
# @Author  : 陆平！！
# @FileName: conftest.py
# @Software: PyCharm

import pytest
from pytest_rusi.page.jqrsc_page import _login_jqrsc_1,_login_jqrsc_2,_login_jqrsc_3,_login_jqrsc_4,_login_jqrsc_5

@pytest.fixture(scope="session")
def login_jqrsc_1(driver,host):
    _login_jqrsc_1(driver,host)

@pytest.fixture(scope="session")
def login_jqrsc_2(driver,host):
    _login_jqrsc_2(driver,host)

@pytest.fixture(scope="session")
def login_jqrsc_3(driver,host):
    _login_jqrsc_3(driver,host)

@pytest.fixture(scope="session")
def login_jqrsc_4(driver,host):
    _login_jqrsc_4(driver,host)

@pytest.fixture(scope="session")
def login_jqrsc_5(driver,host):
    _login_jqrsc_5(driver,host)

