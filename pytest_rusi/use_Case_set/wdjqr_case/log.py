# -*- coding: utf-8 -*-
# @Time    : 2018/12/11  9:44
# @Author  : 陆平！！
# @FileName: log.py
# @Software: PyCharm

import logging, time, os
#这个是日志保存本地的路径
log_path = "E:\\SoftwareTesting\\Projectpath\\pytest_rusi"

class Log():
    def __init__(self):
        #文件的命名
        self.logname = os.path.join (log_path,"%s.log'%time.strftime ('%Y_%m_%d')")
        self.logger = logging.getLogger()
        self.logger.setLevel (logging.DEBUG)
        #日志输出格式
        self.formatter = logging.Formatter ('%(asctime)s]-%(filename)s]-%(levelname)s: %(message)s')
    def console (self, level, message):
        #创建一个FileHandler,用于写到本地
        # fh =logging.FileHandler(self.logname,#追加模式这个是python2的
        # 这个是python 3的
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler (fh)
        #创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        self._console('debug',message)
    def info (self,message):
        self._console('info',message)
    def warning(self, message):
        self._console ('warning',message)
    def error(self, message):
        self. _console ('error',message)
if __name__ =="__main__":
    log = Log()
    log.info("--测试开始----")
    log.info ("输入密码")
    log.warning ("---测试结束----")