# coding:utf-8
from selenium import webdriver
from pytest_rusi.common.base import Base
import time

# -------------定位元素信息------------ #
#输入用户名
username = ("xpath", "//*[@id='views']/div[2]/div/form/div[1]/div/div/input")
#输入密码
password_loc = ("xpath", "//*[@id='views']/div[2]/div/form/div[2]/div/div/input")
#点击登录
submit_loc = ("xpath", "//*[@id='views']/div[2]/div/form/div[4]/div/button")
#登录成功后获取Welcome
welcome_1 = ("xpath","//*[@id='scroll']/div/div/h1")
#登录成功后获取主页面（睿思智能客服平台）
welcome = ("xpath","//*[@id='scroll']/div/div/p")
# 打开退出元素
tuichu_denglu = ("class", "el-dropdown-selfdefine")
# 点击退出登陆元素
quit_log = ("xpath", "/html/body/ul/li[2]")
# 点击确定,退出成功
quit_queding = ("xpath", "/html/body/div[2]/div/div[3]/button[2]/span")

# ---------------定位器：错误提示------------#
# 用户名为空
username_error = ("xpath", "//*[@id='views']/div[2]/div/form/div[1]/div/div[2]")
# 密码为空
password_error = ("xpath", "//*[@id='views']/div[2]/div/form/div[2]/div/div[2]")
# 错误登陆提示语
denglu_tishi_error = ("xpath", "/html/body/div[2]/p")

def _login(driver, host, user="test0012", psw="111111"):
    '''
    登录函数
    '''
    zen = Base(driver)
    driver.get(host+"/user/login")
    zen.window_max()
    zen.sendKeys(username, user)
    zen.sendKeys(password_loc, psw)
    zen.click(submit_loc)
    #判断登录是否成功,如果成功 就判断首页是否存在Welcome 然后在判断是否存在 睿思智能客服云平台
    result_1 = zen.get_text(welcome_1)
    if result_1 == "Welcome":
        result = zen.get_text(welcome)
        if result == "睿思智能客服云平台":
            zen.click(tuichu_denglu)
            time.sleep(1)
            zen.click(quit_log)
            time.sleep(1)
            zen.click(quit_queding)
        else:
            print("获取睿思智能客服云平台失败")
    else:
        print("获取Welcome失败")
    time.sleep(2)

def _login_One(driver, host, user="test0012", psw="111111"):
    '''
    登录函数
    '''
    zen = Base(driver)
    driver.get(host+"/user/login")
    zen.window_max()
    time.sleep(1)
    zen.sendKeys(username, user)
    zen.sendKeys(password_loc, psw)
    zen.click(submit_loc)
    time.sleep(2)

def _login_user_result_error(driver):
    '''
    获取用户名为空
    :param driver:
    '''
    zen = Base(driver)
    result_username_error = zen.get_text(username_error)

def _login_pwd_result_error(driver):
    '''
    获取登录密码为空
    :param driver:
    '''
    zen = Base(driver)
    result_password_error = zen.get_text(password_error)

def _login_submit_result_error(driver):
    '''
    获取登录失败
    :param driver:
    '''
    zen = Base(driver)
    result_login_error = zen.get_attribute(denglu_tishi_error)

if __name__ == "__main__":
    webdriver_chrome = "E:\SoftwareTesting\guge\chrome64_55.0.2883.75\chromedriver.exe"
    driver = webdriver.Chrome(webdriver_chrome)
    _login(driver,"http://10.0.0.13:3005")