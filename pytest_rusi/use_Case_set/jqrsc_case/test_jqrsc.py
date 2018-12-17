# -*- coding: utf-8 -*-
# @Time    : 2018/11/27  13:08
# @Author  : 陆平！！
# @FileName: test_jqrsc.py
# @Software: PyCharm

import pytest
import time
from Cloud_PyTest.pytest_rusi.page.jqrsc_page import _login_jqrsc_1,_login_jqrsc_2,_login_jqrsc_3,_login_jqrsc_4,_login_jqrsc_5

class Testjqrsc():

    @pytest.fixture(scope="function", autouse=True)
    def startPage(self, driver, host):
        print("---让每个用例都从登录首页开始:---start!---")
        driver.get(host + "/user/login")
        driver.delete_all_cookies()
        driver.refresh()

    def test_jqrsc_1_pass(self,driver,host):
        _login_jqrsc_1(driver,host,"test0012","111111")
        time.sleep(2)

    def test_jqrsc_2_pass(self,driver,host):
        _login_jqrsc_2(driver,host,"test0012","111111")
        time.sleep(2)

    def test_jqrsc_3_pass(self,driver,host):
        _login_jqrsc_3(driver,host,"test0012","111111")
        time.sleep(2)

    def test_jqrsc_4_xfail(self,driver,host):
        _login_jqrsc_4(driver,host,"test0012","111111")
        time.sleep(2)

    def test_jqrsc_5_xfail(self,driver,host):
        _login_jqrsc_5(driver,host,"test0012","111111")
        time.sleep(2)

if __name__ == "__main__":
    pytest.main(['-v','test_jqrsc.py'])
