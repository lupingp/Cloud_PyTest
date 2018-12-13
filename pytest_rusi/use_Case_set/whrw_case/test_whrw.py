# -*- coding: utf-8 -*-
# @Time    : 2018/12/13  14:55
# @Author  : 陆平！！
# @FileName: test_whrw.py
# @Software: PyCharm

import pytest


class TestWhrw():

    @pytest.fixture(scope="function", autouse=True)
    def startPage(self, driver, host):
        print("---让每个用例都从登录首页开始:---start!---")
        driver.get(host + "/user/login")
        driver.delete_all_cookies()
        driver.refresh()

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_1(self,driver,login_whrw_1):
        login_whrw_1

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_2(self,driver,login_whrw_2):
        login_whrw_2
        sdsdsdsdsdaa

if __name__ == "__main__":
    pytest.main(["-s","test_whrw.py"])