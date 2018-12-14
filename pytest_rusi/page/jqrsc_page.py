# -*- coding: utf-8 -*-
# @Time    : 2018/11/27  13:14
# @Author  : 陆平！！
# @FileName: jqrsc_page.py
# @Software: PyCharm


import time
import datetime
from pytest_rusi.common.base import Base
from pytest_rusi.page import login_page
from pytest_rusi.page import xtjk_page

# -------------定位元素信息------------ #
#点击机器人市场
jqr_maiker = ("xpath", "//*[@id='views']/aside/ul/li[1]/span[2]")
# 点击复制我的机器人
copy_jqr = ("xpath", "//*[@id='scroll']/div/div/div[1]/div[3]/div[1]/div/div[7]/button[2]/span")
# 输入机器人名称
jqrsc_name = ("xpath", "//*[@id='scroll']/div/div/div[2]/div/div[2]/form/div[2]/div/div/input")
# 输入机器人介绍
jqrsc_jieshao = ("xpath", '//*[@id="scroll"]/div/div/div[2]/div/div[2]/form/div[3]/div/div/textarea')
# 点击确定,
jqrsc_determine = ("xpath", '//*[@id="scroll"]/div/div/div[2]/div/div[2]/form/div[4]/div/button[1]/span')
# 点击取消
jqrsc_quxiao = ("xpath", "//*[@id='scroll']/div/div/div[2]/div/div[2]/form/div[4]/div/button[2]/span")
# 只输入用户名点击登陆
denglu_error = ("class", 'el-form-item__error')
# 点击电话体验
phone_number = ("xpath", '//*[@id="scroll"]/div/div/div[1]/div[3]/div[1]/div/div[7]/button[1]/span')
# 输入电话号码
shuru_phone = ("xpath", '//*[@id="scroll"]/div/div/div[3]/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[1]/div[2]/div/input')
# 输入任务名称
jqr_rw = ("xpath", "//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[2]/div/div/input")
# #选择主叫号码
# shuru_number = (By.XPATH,"//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[3]/div/div/div/input")
# # 选择号码028
# shuru_number_zero = (By.XPATH,"/html/body/div[14]/div[1]/div[1]/ul/li/span")
# #展开高级设置
# zhankai_shezhi = (By.CLASS_NAME,'el-icon-arrow-down')
# # 设置等待时常
# shezhi_time = (By.XPATH,"//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[4]/div[2]/div/div/input")
# 点击发起外呼
waihu = ("xpath", "//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[6]/div/button[1]")
# 点击取消
waihu_quxiao = ("xpath", "//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[6]/div/button[2]")

# ---------------定位器：错误提示------------#
jqrsc_z = ("css","#scroll > div > div > div.wrap-rows.robot-market.el-row > div.header.el-row > div > span")
#判断机器人市场
jqrsc_name_error = ("xpath","//*[@id='scroll']/div/div/div[2]/div/div[2]/form/div[4]/div/button[1]")
#输入错误的任务名称点击发起外呼 断言验证
jqrsc_rw_name_error = ("xpath","//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[2]/div/div[2]")
#输入错误的手机号点击发起外呼 断言验证
jqrsc_shuru_phone_log_error = ("xpath","/html/body/div[14]")
#不输入手机号、任务名称、点击发起外呼 断言验证
jqrsc_null_error = ("class","el-message__content")
#发送外呼成功后 断言验证
jqrsc_waihu_log_error = ("class","el-message__content")


def _login_jqrsc_1(driver, host, user="test0012", psw="111111"):
    zen = Base(driver)
    driver.get(host+"/user/login")
    zen.window_max()
    zen.sendKeys(login_page.username, user)
    zen.sendKeys(login_page.password_loc, psw)
    zen.click(login_page.submit_loc)
    time.sleep(1)
    zen.click(jqr_maiker)
    time.sleep(1)
    result = zen.get_text(jqrsc_z)
    if result == "机器人市场":
        print("判断成功")
        zen.click(login_page.tuichu_denglu)
        time.sleep(1)
        zen.click(login_page.quit_log)
        time.sleep(1)
        zen.click(login_page.quit_queding)
    else:
        print("失败")

def _login_jqrsc_2(driver,host,user="test0012", psw="111111"):
    zen = Base(driver)
    zen.sendKeys(login_page.username, user)
    zen.sendKeys(login_page.password_loc, psw)
    zen.click(login_page.submit_loc)
    time.sleep(1)
    zen.click(jqr_maiker)
    time.sleep(1)
    zen.click(copy_jqr)
    time.sleep(0.5)
    time_now = time.strftime('%Y-%m-%d %H:%M:%S')
    zen.sendKeys(jqrsc_name,time_now)
    zen.sendKeys(jqrsc_jieshao,time_now)
    zen.click(jqrsc_determine)
    time.sleep(1)
    result = zen.get_text(jqrsc_z)
    time.sleep(1)
    if result == "机器人市场":
        zen.click(login_page.tuichu_denglu)
        time.sleep(1)
        zen.click(login_page.quit_log)
        time.sleep(1)
        zen.click(login_page.quit_queding)
    else:
        print("失败")

def _login_jqrsc_3(driver,host,user="test0012", psw="111111"):
    zen = Base(driver)
    zen.sendKeys(login_page.username, user)
    zen.sendKeys(login_page.password_loc, psw)
    zen.click(login_page.submit_loc)
    time.sleep(1)
    zen.click(jqr_maiker)
    time.sleep(1)
    zen.click(phone_number)
    time.sleep(1)
    zen.sendKeys(shuru_phone,"18811730879")
    time.sleep(1)
    now_time = datetime.datetime.now()
    c_time = ('当前时间是%r' % now_time.second)
    zen.sendKeys(jqr_rw,c_time)
    time.sleep(1)
    zen.click(waihu)
    time.sleep(2)
    zen.click(xtjk_page.xitong_jiankong)
    time.sleep(15)
    zen.click(login_page.tuichu_denglu)
    time.sleep(1)
    zen.click(login_page.quit_log)
    time.sleep(1)
    zen.click(login_page.quit_queding)
    time.sleep(2)

def _login_jqrsc_4(driver,host,user="test0012", psw="111111"):
    zen = Base(driver)
    zen.sendKeys(login_page.username, user)
    zen.sendKeys(login_page.password_loc, psw)
    zen.click(login_page.submit_loc)
    time.sleep(1)
    zen.click(jqr_maiker)
    time.sleep(1)
    zen.click(copy_jqr)
    time.sleep(1)
    zen.sendKeys(jqrsc_name,"")
    time.sleep(1)
    now_time = datetime.datetime.now()
    c_time = ("%r" %now_time)
    zen.sendKeys(jqrsc_jieshao,c_time)
    time.sleep(1)
    zen.click(jqrsc_determine)
    time.sleep(1.5)
    zen.click(jqrsc_quxiao)
    time.sleep(1)
    zen.click(login_page.tuichu_denglu)
    time.sleep(1)
    zen.click(login_page.quit_log)
    time.sleep(1)
    zen.click(login_page.quit_queding)
    time.sleep(2)

def _login_jqrsc_5(driver,host,user="test0012", psw="111111"):
    zen = Base(driver)
    zen.sendKeys(login_page.username, user)
    zen.sendKeys(login_page.password_loc, psw)
    zen.click(login_page.submit_loc)
    time.sleep(1)
    zen.click(jqr_maiker)
    time.sleep(1)
    zen.click(phone_number)
    time.sleep(1)
    now_time = datetime.datetime.now()
    c_time = ("%r" %now_time)
    zen.sendKeys(shuru_phone,c_time)
    time.sleep(1)
    zen.sendKeys(jqr_rw,c_time)
    time.sleep(1)
    zen.click(waihu)
    time.sleep(1.5)
    zen.click(waihu_quxiao)
    time.sleep(1)
    zen.click(login_page.tuichu_denglu)
    time.sleep(1)
    zen.click(login_page.quit_log)
    time.sleep(1)
    zen.click(login_page.quit_queding)
    time.sleep(2)

# if __name__ == "__main__":
#     webdriver_chrome = "E:\SoftwareTesting\guge\chrome64_55.0.2883.75\chromedriver.exe"
#     driver = webdriver.Chrome(webdriver_chrome)
#     _login_jqrsc_1(driver,"http://10.0.0.13:3005")
#     _login_jqrsc_2(driver,"http://10.0.0.13:3005")
