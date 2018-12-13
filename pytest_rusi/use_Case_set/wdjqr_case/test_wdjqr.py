# -*- coding: utf-8 -*-
# @Time    : 2018/11/30  13:05
# @Author  : 陆平！！
# @FileName: test_wdjqr.py
# @Software: PyCharm

import pytest
import time
from pytest_rusi.use_Case_set.wdjqr_case import conftest

class Testwdjqr():

    @pytest.fixture(scope="function", autouse=True)
    def startPage(self, driver, host):
        print("---让每个用例都从登录首页开始:---start!---")
        driver.get(host + "/user/login")
        driver.delete_all_cookies()
        driver.refresh()
        time.sleep(2)

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_1(self,driver,login_wdjqr_1):
        login_wdjqr_1

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_2(self,driver,login_wdjqr_2):
        login_wdjqr_2

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_3(self,driver,login_wdjqr_3):
        '''测试用例3：进入我的机器人页面-查看短信 并截图'''
        login_wdjqr_3

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_4(self,driver,login_wdjqr_4):
        login_wdjqr_4

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_5(self,driver,login_wdjqr_5):
        login_wdjqr_5

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_6(self,driver,login_wdjqr_6):
        login_wdjqr_6

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_7(self,driver,login_wdjqr_7):
        login_wdjqr_7

if __name__ == "__main__":
    pytest.main(["-s","test_wdjqr.py"])
