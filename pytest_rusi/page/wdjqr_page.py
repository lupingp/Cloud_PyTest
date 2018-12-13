# -*- coding: utf-8 -*-
# @Time    : 2018/11/30  13:05
# @Author  : 陆平！！
# @FileName: wdjqr_page.py
# @Software: PyCharm

import pytest
import time
import datetime
import os
from pytest_rusi.common.base import Base
from pytest_rusi.page import login_page
from pytest_rusi.page import xtjk_page
from pytest_rusi.page import whrw_page

'''
     ================================定义基本元素,元祖=================================
    '''
#定义我的机器人 元素
wdjqr_robot = ("xpath","//*[@id='views']/aside/ul/li[2]/span[2]")
#我的机器人文本元素
wdjqr_text = ("xpath","//*[@id='scroll']/div/div[2]/div[1]/div[1]/div/span")
#定义机器人姓名 元素
wdjqr_name = ("xpath","//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[1]/div/p[1]/span")
#定义复制复制机器人ID 元素
wdjqr_ID = ("xpath","//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[1]/div/p[2]/i[1]")
#定义批量发起外呼 元素
wdjqr_pl_wh = ("xpath","//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/button[2]/span")
#定义批量发起外呼-选取文件 元素
wdjqr_pl_wh_xqwj = ("xpath","//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/div/div/div[1]/button")
#定义批量发起外呼-选取文件-输入任务名 元素
wdjqr_pl_wh_xqwj_rwm = ("xpath","//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[2]/div/div/input")
#定义批量发起外呼-选取文件-输入任务名-发起外呼 元素
wdjqr_pl_wh_xqwj_rwm_fqwh = ("xpath","//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[6]/div/button[1]/span")
#定义 正常外呼 元素
wdjqr_zcwh = ("xpath","//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/button[1]/span")
#定义 正常外呼-输入手机号 元素
wdjqr_phone = ("xpath","//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[1]/div/div[2]/div/div[1]/div[2]/div/input")
#定义 正常外呼-任务名称 元素
wdjqr_rw_name = ("xpath","//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[2]/div/div/input")
#定义 正常外呼-发起外呼 元素
wdjqr_fqwh = ("xpath","//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[6]/div/button[1]/span")
#定义 查看参数 元素
wdjqr_ckcs = ("xpath","//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[1]/div[2]/button[4]")
#定义 查看参数-关闭查看参数
wdjqr_ckcs_gb = ("class","el-dialog__headerbtn")
#定义 查看短信 元素
wdjqr_ckdx = ("xpath","//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[1]/div[2]/button[5]/i")
#定义 复制新版本 元素
wdjqr_fzbb = ("xpath","//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[1]/div[2]/button[1]")
#定义 复制新版本-确定 元素
wdjqr_fzbb_qd = ("css","body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span")
'''
================================定义错误元素,元祖=================================
'''
# 定义进入机器人页面title 元素
# wdjqr_title = ("xpath", "//*[@id='scroll']/div/div[2]/div[1]/div[1]/div/span")
# 定义复制复制机器人ID返回元素
wdjqr_ID_return = ("class", "el-message__content")
# 定义 判断查看短信 文本 元素
wdjqr_ckdx_title = ("xpath", "//*[@id='scroll']/div/div/div[1]/div/span")
# 定义 复制版成功后的 元素
wdjqr_fzbb_asser = ("class", "el-message__content")

def _login_wdjqr_1(driver):
    '''对照：测试用例1：进入我的机器人页面 并截图'''
    zen = Base(driver)
    zen.click(wdjqr_robot)
    time.sleep(2)
    result = zen.get_text(wdjqr_text)
    time.sleep(0.5)
    if result == "我的机器人":
        zen.click(login_page.tuichu_denglu)
        time.sleep(0.5)
        zen.click(login_page.quit_log)
        time.sleep(0.5)
        zen.click(login_page.quit_queding)
    else:
        print("判断失败")
    time.sleep(1)

def _login_wdjqr_2(driver):
    '''对照：测试用例2：进入我的机器人页面-查看参数 并截图'''
    zen = Base(driver)
    # driver.get(host + "/user/login")
    zen.click(wdjqr_robot)
    time.sleep(2)
    zen.click(wdjqr_ckcs)
    time.sleep(1)
    zen.F5()
    time.sleep(2)
    result = zen.get_text(wdjqr_text)
    time.sleep(0.5)
    if result == "我的机器人":
        zen.click(login_page.tuichu_denglu)
        time.sleep(0.5)
        zen.click(login_page.quit_log)
        time.sleep(0.5)
        zen.click(login_page.quit_queding)
    else:
        print("判断失败")
    time.sleep(1)

def _login_wdjqr_3(driver):
    '''对照：测试用例3：进入我的机器人页面-查看短信 并截图'''
    zen = Base(driver)
    zen.click(wdjqr_robot)
    time.sleep(2)
    zen.click(wdjqr_ckdx)
    time.sleep(1)
    zen.back()
    time.sleep(1)
    result = zen.get_text(wdjqr_text)
    time.sleep(0.5)
    if result == "我的机器人":
        zen.click(login_page.tuichu_denglu)
        time.sleep(0.5)
        zen.click(login_page.quit_log)
        time.sleep(0.5)
        zen.click(login_page.quit_queding)
    else:
        print("判断失败")
    time.sleep(1)

def _login_wdjqr_4(driver):
    '''对照：测试用例4：在我的机器人页面-正常外呼'''
    zen = Base(driver)
    zen.click(wdjqr_robot)
    time.sleep(2)
    zen.click(wdjqr_zcwh)
    time.sleep(1)
    zen.sendKeys(wdjqr_phone,"18811730879")
    time.sleep(2)
    now_time = datetime.datetime.now()
    a = ("当前是%r"%now_time.second)
    zen.sendKeys(wdjqr_rw_name,a)
    time.sleep(1)
    zen.click(wdjqr_fqwh)
    time.sleep(2)
    zen.click(xtjk_page.xitong_jiankong)
    time.sleep(15)
    result = zen.get_text(xtjk_page.xitong_jiankong_title)
    if result == "系统监控":
        zen.click(login_page.tuichu_denglu)
        time.sleep(0.5)
        zen.click(login_page.quit_log)
        time.sleep(0.5)
        zen.click(login_page.quit_queding)
    else:
        print("退出失败")

def _login_wdjqr_5(driver):
    '''对照:测试用例5：复制机器人ID'''
    zen = Base(driver)
    zen.click(wdjqr_robot)
    time.sleep(2)
    zen.click(wdjqr_ID)
    time.sleep(1)
    result = zen.get_text(wdjqr_text)
    time.sleep(0.5)
    if result == "我的机器人":
        zen.click(login_page.tuichu_denglu)
        time.sleep(0.5)
        zen.click(login_page.quit_log)
        time.sleep(0.5)
        zen.click(login_page.quit_queding)
    else:
        print("退出失败")
    time.sleep(1)

def _login_wdjqr_6(driver):
    '''对照：测试用例6：批量外呼-查看详情-录音播放-导出明细'''
    zen = Base(driver)
    zen.click(wdjqr_robot)
    time.sleep(2)
    zen.click(wdjqr_pl_wh)
    time.sleep(1)
    zen.click(wdjqr_pl_wh_xqwj)
    os.system("E:\\SoftwareTesting\\Projectpath\\AICC\\aicc_Cloud\\aicc_BatchUpload\\Plsc.exe")
    time.sleep(2)
    now_time = datetime.datetime.now()
    s_time = ("当前秒是%s" % now_time.second)
    zen.sendKeys(wdjqr_pl_wh_xqwj_rwm,s_time)
    time.sleep(0.5)
    zen.click(wdjqr_pl_wh_xqwj_rwm_fqwh)
    time.sleep(3)
    zen.click(xtjk_page.xitong_jiankong)
    time.sleep(20)
    zen.click(whrw_page.task)
    time.sleep(2)
    zen.F5()
    time.sleep(2)
    zen.click(whrw_page.task_ckxq)
    time.sleep(1)
    zen.click(whrw_page.task_ckxq_ckxq)
    time.sleep(1)
    zen.click(whrw_page.task_ckxq_ckxq_bfly)
    time.sleep(13)
    zen.F5()
    time.sleep(2)
    zen.click(whrw_page.task_ckxq_dcly)
    os.system("E:\\SoftwareTesting\\Projectpath\\AICC\\aicc_Cloud\\aicc_BatchUpload\\Dcly.exe")
    time.sleep(8)
    result = zen.get_text(whrw_page.task_rwxq_title)
    if result == "任务详情":
        zen.click(login_page.tuichu_denglu)
        time.sleep(0.5)
        zen.click(login_page.quit_log)
        time.sleep(0.5)
        zen.click(login_page.quit_queding)
    else:
        print("退出失败")

def _login_wdjqr_7(driver):
    '''对照:测试用例7：进入我的机器人页面-复制版本 '''
    zen = Base(driver)
    zen.click(wdjqr_robot)
    time.sleep(1)
    zen.click(wdjqr_fzbb)
    time.sleep(0.5)
    zen.click(wdjqr_fzbb_qd)
    time.sleep(3)
    result = zen.get_text(wdjqr_text)
    time.sleep(0.5)
    if result == "我的机器人":
        zen.click(login_page.tuichu_denglu)
        time.sleep(0.5)
        zen.click(login_page.quit_log)
        time.sleep(1)
        zen.click(login_page.quit_queding)
    else:
        print("退出失败")
    time.sleep(1)




# if __name__ == "__main__":
#     webdriver_chrome = "E:\SoftwareTesting\guge\chrome64_55.0.2883.75\chromedriver.exe"
#     driver = webdriver.Chrome(webdriver_chrome)
#     _login_wdjqr_1(driver,"http://10.0.0.13:3005")
