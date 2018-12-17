# -*- coding: utf-8 -*-
# @Time    : 2018/12/17  22:56
# @Author  : 陆平！！
# @FileName: conftest.py.py
# @Software: PyCharm

import pytest
from Cloud_PyTest.pytest_rusi.page import xtjk_page
from Cloud_PyTest.pytest_rusi.page import login_page

@pytest.fixture("function")
def login_xtjk(driver):
    xtjk_page._login_xtjk_1(driver)

@pytest.fixture("function")
def login(driver,host):
    login_page._login_One(driver,host)

