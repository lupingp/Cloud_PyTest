# coding:utf-8
import pytest
import time
from Cloud_PyTest.pytest_rusi.page.login_page import _login,_login_user_result_error,_login_pwd_result_error,_login_submit_result_error

class TestLogin():

    @pytest.fixture(scope="function",  autouse=True)
    def startPage(self, driver, host):
        print("---让每个用例都从登录首页开始:---start!---")
        driver.get(host+"/user/login")
        driver.delete_all_cookies()
        driver.refresh()

    def test_login_1_fail(self, driver, host):
        """测试用例1：用户名空，密码正确"""
        _login(driver, host, "", "111111")
        # time.sleep(2)
        result1 = _login_user_result_error(driver)
        if  result1 == "请输入用户名":
            print("断言失败")
        else:
            print("断言成功")

    def test_login_2_fail(self, driver, host):
        '''测试用例2：用户名正确，密码为空'''
        _login(driver, host, "test0012", "")
        # time.sleep(2)
        result2 = _login_pwd_result_error(driver)
        if  result2 == "请输入密码":
            print("断言失败")
        else:
            print("断言成功")

    def test_login_3_fail(self, driver, host):
        '''测试用例3：用户名 密码都为空'''
        _login(driver, host, "", "")
        # time.sleep(2)
        result3 = _login_user_result_error(driver)
        result3_1 = _login_pwd_result_error(driver)

        if  result3 == "请输入用户名":
            print("断言失败")
        else:
            print("断言成功")
        if  result3_1 == "请输入密码":
            print("断言失败")
        else:
            print("断言成功")

    def test_login_4_fail(self, driver, host):
        '''测试用例4：用户名为特殊字符(*- $%^&./';l)+数字 密码正确'''
        _login(driver, host, "*- $%^&./';l12", "111111")
        # time.sleep(1)
        result4 = _login_submit_result_error(driver)
        if  result4 == "用户名不存在":
            print("断言失败")
        else:
            print("断言成功")

    def test_login_5_fail(self, driver, host):
        '''测试用例5：用户名正确 密码为特殊字符(*- $%^&./';l)+数字'''
        _login(driver, host, "test0012", "*- $%^&./';l12")
        # time.sleep(1)
        result5 = _login_submit_result_error(driver)
        if  result5 == "用户密码错误，请重试！":
            print("断言失败")
        else:
            print("断言成功")

    def test_login_6_fail(self, driver, host):
        '''测试用例6：用户名输入超长(数字+字母) 密码为特殊字符(*- $%^&./';l)+数字'''
        _login(driver, host, "test0012", "*- $%^&./';l12")
        # time.sleep(1)
        result6 = _login_submit_result_error(driver)
        if  result6 == "用户密码错误，请重试！":
            print("断言失败")
        else:
            print("断言成功")

    def test_login_7_fail(self, driver, host):
        '''测试用例7：用户名输入特殊字符(*- $%^&./';l)+数字 密码为超长(数字+字母)'''
        _login(driver, host, "*- $%^&./';l456", "123456zxcasdwrew")
        # time.sleep(1)
        result7 = _login_submit_result_error(driver)
        if  result7 == "用户名不存在":
            print("断言失败")
        else:
            print("断言成功")

    def test_login_8_fail(self, driver, host):
        '''测试用例8：用户名输入1位数字 密码输入1位数字'''
        _login(driver, host, "1", "1")
        # time.sleep(1)
        result8 = _login_submit_result_error(driver)
        if  result8 == "用户密码错误，请重试！":
            print("断言失败")
        else:
            print("断言成功")

    def test_login_9_fail(self, driver, host):
        '''测试用例9：用户名输入1位字母(不区分大小写) 密码输入1位字母(不区分大小写)'''
        _login(driver, host, "a", "D")
        # time.sleep(1)
        result9 = _login_submit_result_error(driver)
        if  result9 == "用户密码错误，请重试！":
            print("断言失败")
        else:
            print("断言成功")

    def test_login_10_fail(self, driver, host):
        '''测试用例9：用户名输入1位特殊字符 密码输入1位特殊字符'''
        _login(driver, host, "#", "%")
        # time.sleep(1)
        result10 = _login_submit_result_error(driver)
        if  result10 == "用户密码错误，请重试！":
            print("断言失败")
        else:
            print("断言成功")

    def test_login_11_pass(self, driver, host):
        '''测试用例9：用户名正确 密码正确'''
        _login(driver, host, "test0012", "111111")

if __name__ == "__main__":
    pytest.main(["-s","-v", "test_login.py","--html=report.html"])