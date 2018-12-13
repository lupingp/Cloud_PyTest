# -*- coding: utf-8 -*-
# @Time    : 2018/12/12  16:01
# @Author  : 陆平！！
# @FileName: whrw_page.py
# @Software: PyCharm
'''
     ================================定义基本元素,元祖=================================
'''
#定义进入外呼任务页面 元素
task = ("xpath","//*[@id='views']/aside/ul/li[3]/span[2]")
#定义 外呼任务的title
task_title = ("xpath","//*[@id='scroll']/div/div/div[1]/div/span")
#定义导出明细按钮 元素
task_dcmx = ("xpath","//*[@id='scroll']/div/div/div[2]/div/div/div/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span")
#定义任务详情Title
task_rwxq_title = ("xpath","//*[@id='scroll']/div/div[1]/div/span")
#定义查看详情按钮 元素
task_ckxq = ("xpath","//*[@id='scroll']/div/div/div[2]/div/div/div/div[3]/table/tbody/tr[1]/td[8]/div/button[1]/span")
#定义查看详情-查看详情按钮 元素
task_ckxq_ckxq = ("xpath","//*[@id='scroll']/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[10]/div/div/button[1]/span")
#定义查看详情-查看详情-播放录音按钮 元素
task_ckxq_ckxq_bfly = ("xpath","//*[@id='scroll']/div/div[4]/div/div[2]/div/div[1]/div/div[2]/button[2]/span/i")
# #定义查看详情-查看详情-关闭 元素
# task_ckxq_ckxq_gb = (By.XPATH,"//*[@class='el-icon-close']")
#定义查看详情-导出录音按钮 元素
task_ckxq_dcly = ("xpath","//*[@id='scroll']/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[10]/div/div/button[2]/span")
#定义批量导出明细 元素
task_pldc_mx = ("xpath","//*[@id='scroll']/div/div/div[2]/div/div/div/div[2]/table/thead/tr/th[1]/div/label/span/span")
#定义批量导出-点击选中导出 元素
task_pldc_mx_xzdc = ("xpath","//*[@id='scroll']/div/div/div[2]/div/div/form/div[6]/div/button[3]/span")
#定义 外呼任务(任务状态)元素
task_whrw_rwzt = ("xpath","//*[@autocomplete='off']")
#定义 外呼任务(选择任务)元素
task_whrw_rwzt_xz = ("xpath","//*[@x-placement='bottom-start']/div/div/ul/li[2]")
#定义 重置按钮 元素
task_cz = ("xpath","//*[@id='scroll']/div/div/div[2]/div/div/form/div[6]/div/button[2]/span")
#定义 查询 元素
task_cx = ("xpath","//*[@id='scroll']/div/div/div[2]/div/div/form/div[6]/div/button[1]/span")