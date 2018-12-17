# -*- coding: utf-8 -*-
# @Time    : 2018/11/27  15:10
# @Author  : 陆平！！
# @FileName: xtjk_page.py
# @Software: PyCharm

import time
from Cloud_PyTest.pytest_rusi.common.base import Base
from . import login_page
'''
 ================================定义基本元素,元祖=================================
'''

# 定义进入系统监控页面 元素
xitong_jiankong = ("xpath", "//*[@id='views']/aside/ul/li[4]/span[1]")
# 定义系统监控title
xitong_jiankong_title = ("xpath","//*[@id='scroll']/div/div[1]/div/span")
# 定义系统监控多窗口
xitong_chuangkou = ("xpath","//*[@id='pane-second']/div/div[2]/div[1]/i[3]")
# 定义历史通过1
xitong_history_phone_1 = ("xpath","//*[@id='pane-second']/div/div[2]/div[2]/div[1]/div/ul/li[2]")
# 定义历史通过2
xitong_history_phone_2 = ("xpath","//*[@id='pane-second']/div/div[2]/div[2]/div[1]/div/ul/li[3]")
# 定义历史通过3
xitong_history_phone_3 = ("xpath","//*[@id='pane-second']/div/div[2]/div[2]/div[1]/div/ul/li[4]")
# 定义历史通过4
xitong_history_phone_4 = ("xpath","//*[@id='pane-second']/div/div[2]/div[2]/div[1]/div/ul/li[5]")
# 定义历史通过方大
xitong_history_phone_Max = ("xpath","//*[@id='pane-second']/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/ul/li[1]/a")

def _login_xtjk_1(driver):
    zen = Base(driver)
    zen.click(xitong_jiankong)
    time.sleep(2)
    zen.click(xitong_chuangkou)
    zen.click(xitong_history_phone_1)
    zen.click(xitong_history_phone_2)
    zen.click(xitong_history_phone_3)
    zen.click(xitong_history_phone_4)
    time.sleep(2)
    zen.click(xitong_history_phone_Max)
    time.sleep(1)
    zen.click(xitong_history_phone_Max)
    time.sleep(0.5)
    zen.F5()
    time.sleep(1)
    result = zen.get_text(xitong_jiankong_title)
    if result == "系统监控":
        zen.click(login_page.tuichu_denglu)
        time.sleep(0.5)
        zen.click(login_page.quit_log)
        time.sleep(0.5)
        zen.click(login_page.quit_queding)
    else:
        print("断言失败！"
              "退出失败！")

