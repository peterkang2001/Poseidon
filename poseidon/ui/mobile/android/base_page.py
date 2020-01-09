# coding=utf-8

"""
@author:songmengyun
@file: base_page.py
@time: 2020/01/03

"""

import time
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from poseidon.ui.util.location import *
from poseidon.base import CommonBase as cb

class Swipe:

    def __init__(self, driver):
        self.driver = driver

    def swipe_up(self, width, height, n=5):
        '''定义向上滑动方法'''
        logging.info("定义向上滑动方法")
        x1 = width * 0.5
        y1 = height * 0.9
        y2 = height * 0.25
        time.sleep(3)
        logging.info("滑动前")
        for i in range(n):
            logging.info("第%d次滑屏" % i)
            time.sleep(3)
            self.driver.swipe(x1, y1, x1, y2)

    def swipe_down(self, width, height, n=5):
        '''定义向下滑动方法'''
        logging.info("定义向下滑动方法")
        x1 = width * 0.5
        y1 = height * 0.25
        y2 = height * 0.9
        time.sleep(3)
        logging.info("滑动前")
        for i in range(n):
            logging.info("第%d次滑屏" % i)
            time.sleep(3)
            self.driver.swipe(x1, y1, x1, y2)

    def swipe_left(self, width, height, n=5):
        '''定义向左滑动方法'''
        logging.info("定义向左滑动方法")
        x1 = width * 0.8
        x2 = width * 0.2
        y1 = height * 0.5

        time.sleep(3)
        logging.info("滑动前")
        for i in range(n):
            logging.info("第%d次滑屏" % i)
            time.sleep(3)
            self.driver.swipe(x1, y1, x2, y1)

    def swipe_right(self, width, height, n=5):
        '''定义向右滑动方法'''
        logging.info("定义向右滑动方法")
        x1 = width * 0.2
        x2 = width * 0.8
        y1 = height * 0.5

        time.sleep(3)
        logging.info("滑动前")
        for i in range(n):
            logging.info("第%d次滑屏" % i)
            time.sleep(3)
            self.driver.swipe(x1, y1, x2, y1)

class Action:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        """
        通过传入的locator获取selenium webelement对象
        :param locator:
        :return:
        """
        locator_type = locator[0]
        element = None
        if locator_type == By.ID:
            element = findId(self.driver, locator[1])
            logging.debug("使用 id 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.XPATH:
            element = findXpath(self.driver, locator[1])
            logging.debug("使用 xpath 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.LINK_TEXT:
            element = findLinkText(self.driver, locator[1])
            logging.debug("使用 link text 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.PARTIAL_LINK_TEXT:
            element = findPLinkText(self.driver, locator[1])
            logging.debug("使用 partial link text 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.NAME:
            element = findName(self.driver, locator[1])
            logging.debug("使用 name 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.TAG_NAME:
            element = findTagName(self.driver, locator[1])
            logging.debug("使用 tag name 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.CLASS_NAME:
            element = findClassName(self.driver, locator[1])
            logging.debug("使用 class name 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.CSS_SELECTOR:
            element = findCss(self.driver, locator[1])
            logging.debug("使用 css selector 定位元素 ==> {0}".format(locator[1]))

        else:
            logging.error("错误的locator_type，请确认")

        return element

    def get_elements(self, locator):
        """
        通过传入的locator获取selenium webelements对象
        :param locator:
        :return:
        """
        locator_type = locator[0]
        elements = None
        if locator_type == By.ID:
            elements = findsId(self.driver, locator[1])
            logging.debug("使用 id 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.XPATH:
            elements = findsXpath(self.driver, locator[1])
            logging.debug("使用 xpath 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.LINK_TEXT:
            elements = findsLinkText(self.driver, locator[1])
            logging.debug("使用 link text 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.PARTIAL_LINK_TEXT:
            elements = findsPLinkText(self.driver, locator[1])
            logging.debug("使用 partial link text 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.NAME:
            elements = findsName(self.driver, locator[1])
            logging.debug("使用 name 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.TAG_NAME:
            elements = findsTagName(self.driver, locator[1])
            logging.debug("使用 tag name 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.CLASS_NAME:
            elements = findsClassName(self.driver, locator[1])
            logging.debug("使用 class name 定位元素 ==> {0}".format(locator[1]))

        elif locator_type == By.CSS_SELECTOR:
            elements = findsCss(self.driver, locator[1])
            logging.debug("使用 css selector 定位元素 ==> {0}".format(locator[1]))
        else:
            logging.error("错误的locator_type，请确认")

        return elements

class AssertBase:
    def __init__(self, driver):
        self.driver = driver

    @cb.com_try_catch
    def check_current_activity(self, app_activity):
        '''验证当前activity是否登录传入app_activity'''
        current_activity = self.driver.current_activity()
        if current_activity:
            cb.checkEqual(current_activity, app_activity)
        else:
            logging.error('当前没有app_activity')




class BasePage(Swipe, Action, AssertBase):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver=self.driver)

    @cb.com_try_catch
    def install_app(self, app_path, appPackage):
        '''
        :param app_path: 安装包路径
        :param appPackage: 安装包包名
        :return: 先判断是否安装: 如果未安装，则执行安装
        '''
        if self.driver.is_app_installed(appPackage):
            logging.info(f'{appPackage}已安装')
        else:
            self.driver.install_app(app_path)
            logging.info(f'{appPackage}安装成功')

    @cb.com_try_catch
    def uninstall_app(self, appPackage):
        '''
        :param appPackage: 安装包包名
        :return: 先判断是否安装: 如果已安装，执行卸载
        '''
        if self.driver.is_app_installed(appPackage):
            self.driver.remove_app(appPackage)
            logging.info(f'{appPackage}卸载成功')
        else:
            logging.info(f'{appPackage}已卸载')

    @cb.com_try_catch
    def open_app(self, app_package, app_activity):
        '''
        :param app_package: 需要打开第应用名
        :param app_activity: 需要打开的界面
        :return: 在当前应用中打开一个activity或者启动一个新应用并打开一个 activity
        '''
        current_activity = self.driver.current_activity()
        logging.info(f'当前已启动activity： {current_activity}')
        self.driver.start_activity(app_package, app_activity)
        logging.info(f'当前已启动activity： {current_activity}')

    def app_strings(self):
        '''返回应用程序的字符串'''
        string = self.driver.app_strings(language='en')
        return string

    @cb.com_try_catch
    def get_app_package_info(self):
        """
        :return: 输出短信程序包名和界面名
        """
        return [self.driver.current_package, self.driver.current_activity]

    @cb.com_try_catch
    def get_window_info(self):
        '''获取屏幕宽度和高度'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return [width, height]

    def lock_app(self):
        '''锁定屏幕'''
        self.driver.lock(5)

    def hide_keyboard(self):
        '''收起键盘'''
        self.driver.hide_keyboard()

    @cb.com_try_catch
    def backgroup_app(self, seconds, restart=True):
        if restart == True:
            self.driver.background_app(seconds)
        else:
            pass

    @cb.com_try_catch
    def wait(self, fun, timeout=10, fre=1):
        '''

        :param : 显示等待
        :return:
        '''
        wait = WebDriverWait(self.driver, timeout, fre)
        wait.until(fun)

    def click_element(self, locator, is_button=True):
        """
        点击
        :param locator:
        :param is_button:
        :return:
        """
        element = self.get_element(locator)
        if is_button:
            element.click()
        else:
            # f = self.driver.find_element(*locator)
            ActionChains(self.driver).click(element).perform()

    def set_text(self, locator, values):
        """
        为输入框 输入字符内容
        :param locator:
        :param values:
        :return:
        """
        try:
            text_field = self.get_element(locator)
            text_field.clear()
            text_field.send_keys(values)
        except Exception as msg:
            logging.error(msg)


    def element_text(self):
        pass

    def scroll_screen(self):
        pass

    def touch_screen(self):
        pass

    def is_displayed(self, locator, mark=True):
        """
        判断某个元素是否存在
        :param locator:
        :return:
        """
        element = self.get_element(locator)
        if mark:
            self.hight_light(element)
        return element.is_displayed()

    def hight_light(self, element, times=2, seconds=2, color="red", border=2):
        """
        传入selenium webelement对象如果能找到就高亮显示
        :param element:
        :param times:
        :param seconds:
        :return:
        """
        js = "element = arguments[0]; " \
                  "original_style = element.getAttribute('style'); " \
                  "element.setAttribute('style', original_style + \";" \
                  "border: %spx solid %s;\");" \
                  "setTimeout(function(){element.setAttribute('style', original_style);}, 1000);" %(border,color)


        try:
            for i in range(0, times):
                self.driver.execute_script(js, element)
        except Exception as e:
            logging.error(e)




