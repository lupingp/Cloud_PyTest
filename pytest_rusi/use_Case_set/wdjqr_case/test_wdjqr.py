# -*- coding: utf-8 -*-
# @Time    : 2018/11/30  13:05
# @Author  : 陆平！！
# @FileName: test_wdjqr.py
# @Software: PyCharm

import pytest
import time

class Testwdjqr():

    @pytest.fixture(scope="function", autouse=True)
    def startPage(self, driver, host):
        print("---让每个用例都从登录首页开始:---start!---")
        driver.get(host + "/user/login")
        driver.delete_all_cookies()
        driver.refresh()
        time.sleep(2)

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_1(self,login_wdjqr_1):
        '''测试用例1：进入我的机器人页面 并截图'''
        login_wdjqr_1

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_2(self,login_wdjqr_2):
        '''测试用例2：进入我的机器人页面-查看参数 并截图'''
        login_wdjqr_2

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_3(self,login_wdjqr_3):
       '''测试用例3：进入我的机器人页面-查看短信 并截图'''
       login_wdjqr_3

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_4(self,login_wdjqr_4):
        '''测试用例4：在我的机器人页面-正常外呼'''
        login_wdjqr_4


    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_5(self,login_wdjqr_5):
        '''测试用例5：复制机器人ID'''
        login_wdjqr_5

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_6(self,login_wdjqr_6):
        '''测试用例6：批量外呼-查看详情-录音播放-导出明细'''
        login_wdjqr_6

    @pytest.mark.usefixtures("login_One")
    def test_wdjqr_7(self,login_wdjqr_7):
        '''测试用例7：进入我的机器人页面-复制版本 '''
        login_wdjqr_7

if __name__ == "__main__":
    pytest.main(["-s","test_wdjqr.py"])
