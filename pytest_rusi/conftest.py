# coding:utf-8
import pytest
from selenium import webdriver
from datetime import datetime
from py._xmlgen import html
from pytest_rusi.common.base import Base


"""
conftest.py文件
令行参数--browser、--host
"""
#定义全局_driver
_driver = None

def pytest_addoption(parser):
    '''添加命令行参数--browser、--host'''
    #添加browser参数，设置默认浏览器
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser option: firefox or chrome"
             )

    # 添加host参数，设置默认测试环境地址
    parser.addoption(
        "--host", action="store", default="http://10.0.0.13:3005", help="test host->http://10.0.0.13:3005"
    )

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#         report.description = str(item.function.__doc__)
#         report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('Description'))
#     cells.insert(2, html.th('Test_nodeid'))
#     cells.pop(2)
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
#     cells.insert(2, html.td(report.nodeid))
#     cells.pop(2)

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
#
# def _capture_screenshot():
#     '''
#     截图保存为base64
#     :return:
#     '''
#     return _driver.get_screenshot_as_base64()

@pytest.fixture(scope='session')
def driver(request):
    '''定义全局driver参数'''
    global _driver

    if _driver is None:
        name = request.config.getoption("--browser")
        if name == "firefox":
            _driver = webdriver.Firefox()
        elif name == "chrome":
            webdriver_chrome = "E:\SoftwareTesting\guge\chrome64_55.0.2883.75\chromedriver.exe"
            _driver = webdriver.Chrome(webdriver_chrome)
        else:
            _driver = webdriver.Firefox()
        print("正在启动浏览器名称：%s" % name)
    def fn():
        print("当全部用例执行完之后：teardown quit driver！")
        _driver.quit()
    request.addfinalizer(fn) #终止函数
    return _driver

@pytest.fixture(scope='session')
def host(request):
    '''全局host参数'''
    return request.config.getoption("--host")