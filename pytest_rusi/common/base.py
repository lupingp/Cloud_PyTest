from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class Base():
    '''基于原生的selenium做二次封装'''

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.t = 1

    def find_element(self, locator):
        """
        driver.find_element  此为元组(id,kw)，此方法为PageObject模式准备方法
        """
        by = locator[0]
        value = locator[1]
        print("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))

        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "text":
            return self.driver.find_element_by_link_text(value)
        elif by == "text_part":
            return self.driver.find_element_by_partial_link_text(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")

    def wait_element(self, locator):
        """
        等待元素在指定的时间类出现
        :param element:      元素的定位表达式
        :param seconds:      等待的时间
        :return:
        """
        by = locator[0]
        value = locator[1]
        print("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
        if by == "id":
            a = WebDriverWait(self.driver, self.timeout,self.t).until(EC.presence_of_element_located(locator))
            return a
        elif by == "name":
            b = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return b
        elif by == "class":
            c = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return c
        elif by == "text":
            d = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return d
        elif by == "xpath":
            e = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return e
        elif by == "css":
            f = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return f
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

    # def findElement(self, locator):
    #     '''定位到元素，返回元素对象，没定位到，Timeout异常'''
    #     if not isinstance(locator, tuple):
    #         print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
    #     else:
    #         print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
    #         ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
    #         return ele
    #
    # def findElements(self, locator):
    #     if not isinstance(locator, tuple):
    #         print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
    #     else:
    #         try:
    #             print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
    #             eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
    #             return eles
    #         except:
    #             return []

    #
    def sendKeys(self, locator, text=''):
        '''使用强制等待'''
        ele = self.find_element(locator)
        ele.send_keys(text)

    # def sendKeys_timeout(self, locator, text=''):
    #     '''使用显性等待'''
    #     ele = self.wait_element(locator)
    #     ele.send_keys(text)

    # def click(self, locator):
    #     '''使用显性等待'''
    #     ele = self.wait_element(locator)
    #     ele.click()

    def click(self, locator):
        '''使用强制等待'''
        ele = self.find_element(locator)
        ele.click()


    def clear(self, locator):
        ele = self.wait_element(locator)
        ele.clear()

    # def isSelected(self, locator):
    #     '''判断元素是否被选中，返回bool值'''
    #     ele = self.findElement(locator)
    #     r = ele.is_selected()
    #     return r
    #
    # def isElementExist(self, locator):
    #     try:
    #         self.findElement(locator)
    #         return True
    #     except:
    #         return False
    #
    # def is_title(self, _title=''):
    #     '''返回bool值'''
    #     try:
    #         result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
    #         return result
    #     except:
    #         return False
    #
    # def is_title_contains(self, _title=''):
    #     '''返回bool值'''
    #     try:
    #         result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
    #         return result
    #     except:
    #         return False
    #
    def is_text_in_element(self, locator, _text=''):
        '''返回bool值'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False
    #
    # def is_value_in_element(self, locator, _value=''):
    #     '''返回bool值, value为空字符串，返回Fasle'''
    #     if not isinstance(locator, tuple):
    #         print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
    #     try:
    #         result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
    #         return result
    #     except:
    #         return False
    #
    # def is_alert(self, timeout=3):
    #     '''判断alert,存在返回alert实例，不存在，返回false'''
    #     try:
    #         result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
    #         return result
    #     except:
    #         return False
    #
    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self, locator):
        '''获取文本'''
        try:
            t = self.find_element(locator).text
            return t
        except:
            print("获取text失败，返回'' ")
            return ""

    def get_attribute(self, locator):
        '''获取属性'''
        ele = self.find_element(locator).get_attribute("textContent")
        return ele

    def js_focus_element(self, locator):
        '''聚焦元素'''
        target = self.wait_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self,x=0):
        '''滚动到底部'''
        js = "window.scrollTo(%s,document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        '''通过索引,index是索引第几个，从0开始，默认选第一个'''
        element = self.wait_element(locator)  # 定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性'''
        element = self.wait_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.wait_element(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        '''切换iframe'''
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.findElement(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
             print("iframe切换异常")

    def switch_handle(self, window_name):
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            return r

    def move_to_element(self, locator):
        '''鼠标悬停操作'''
        ele = self.wait_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def window_max(self):
        self.driver.maximize_window()


    def wait(self, locator):
        '''
        :param seconds:    等待时间
        :return:
        '''
        self.driver.implicitly_wait(locator)

    def Close(self):
        '''
        :return:  关闭窗口
        '''
        self.driver.close()

    def Quit(self):
        '''
        :return:  退出浏览器
        '''
        self.driver.quit()

    def Click(self, element):
        '''
        功能：点击
        :param element: 元素的定位表达式
        :return:
        '''
        self.wait_element(element)
        self.wait_element(element).click()

    def Right_Click(self, locator):
        '''
        功能：右击
        :param element: 元素的定位表达式
        :return:
        '''
        self.wait_element(locator)
        ActionChains.context_click(self.find_element(locator)).perform()

    def MoveToElement(self, locator):
        '''
        功能：移动到元素
        :param element: 元素的定位表达式
        :return:
        '''
        self.wait_element(locator)
        ActionChains.move_to_element(self.find_element(locator)).perform()

    def double_click(self, locator):
        '''
        功能：双击元素
        :param element: 元素的定位表达式
        :return:
        '''
        self.wait_element(locator)
        ActionChains.double_click(self.find_element(locator)).perform()

    def drag_and_drop(self, locator):
        '''
        功能：拖拽元素
        :param element: 元素的表达式
        :return:
        '''
        self.wait_element(locator)
        ActionChains.drag_and_drop(self.find_element(locator)).perform()

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        self.wait_element(locator)
        ActionChains.move_to_element(self.find_element(locator)).perform()

    def back(self):
        '''
        功能：返回
        :return:
        '''
        self.driver.back()

    def back_2(self,locator):
        '''获取文本'''
        try:
            element = self.wait_element(locator).back()
            return element
        except:
            print("退回失败，返回'' ")
            return ""

    def forward(self, element):
        '''
        :param element:  元素的表达式
        :return:
        '''
        self.driver.forward()

    def get_display(self, locator):
        """
        功能：判断元素是否显示
        :param element: 元素表达式
        :return:
        """

        self.wait_element(locator)
        return self.wait_element(locator).is_displayed()

    def get_title(self):
        """
        功能:得到浏览器的标题
        :return:
        """
        return self.driver.title

    def get_screenshot(self, locator):
        """
        功能：截图并保存
        :param file_path:  文件路径
        :return:
        """
        self.driver.get_screenshot_as_file(locator)

    def submit(self, locator):
        """
        功能：提交特定的表单
        :param element:   元素表达式
        :return:
        """
        self.wait_element(locator)
        self.wait_element(locator).submit()

    def switch_to_frame(self, locator):
        """
        功能：切换到特定的frame
        :param element: 元素的表达式
        :return:
        """
        self.wait_element(locator)
        self.driver._switch_to_frame(self.wait_element(locator))

    def switch_to_frame_out(self):
        """
        功能：切换道默认的上下文
        :return:
        """
        self.driver.switch_to.default_content()

    def F5(self):
        '''
        功能：刷新页面
        :return:
        '''
        self.driver.refresh()

    def accept_alert(self):
        """
        功能：确认按钮
        :return:
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        功能：对话框取消
        :return:
        """
        self.driver.switch_to.alert.dismiss()

    def get(self,url):
        """
        功能：对话框取消
        :return:
        """
        self.driver.get(url)

    def implicitly(self,timeout):

        self.driver.implicitly_wait(timeout)


