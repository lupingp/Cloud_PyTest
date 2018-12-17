# -*- coding: utf-8 -*-
# @Time    : 2018/12/17  23:06
# @Author  : 陆平！！
# @FileName: xtjk_case.py
# @Software: PyCharm

import pytest


class TestXtjk():
    @pytest.fixture(scope="function", autouse=True)
    def startPage(self, driver, host):
        print("---让每个用例都从登录首页开始:---start!---")
        driver.get(host + "/user/login")
        driver.delete_all_cookies()
        driver.refresh()

    @pytest.mark.usefixtures("login")
    def test_xtjk_1(diver,login_xtjk):
        login_xtjk

if __name__ == "__main__":
    pytest.main(["-s","xtjk_case.py"])