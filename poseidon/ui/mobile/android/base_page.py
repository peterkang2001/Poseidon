# coding=utf-8

"""
@author:songmengyun
@file: base_page.py
@time: 2020/01/03

"""
import time
import logging
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.connectiontype import ConnectionType

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def launch_app(self):
        pass

    def open_app(self, app_package, app_activity):
        '''
        :param app_package: 需要打开第应用名
        :param app_activity: 需要打开的界面
        :return:
        '''
        logging.info(f'打开app{app_package}中{app_activity}')
        self.driver.start_activity(app_package, app_activity)

    def get_app_package_info(self):
        """
        公共等待方法
        :param wait_seconds:
        :return:
        """
        pass

    def close_app(self):
        pass

    def quit_app(self):
        pass

    def install_uninstall_app(self):
        pass

    def get_element(self, locator):
        pass

    def get_elements(self, locator):
        pass

    def element_text(self):
        pass

    def wait(self, implicitly_wait, ):
        pass

    def scroll_screen(self):
        pass

    def touch_screen(self):
        pass


    def click_element(self, locator, is_button=True):
        """
        点击
        :param locator:
        :param is_button:
        :return:
        """
        pass

    def set_text(self, locator, values):
        """
        为输入框 输入字符内容
        :param locator:
        :param values:
        :return:
        """
        try:
            text_field = self.get_web_element(locator)
            text_field.clear()
            text_field.send_keys(values)
        except Exception as msg:
            logging.error(msg)

    def get_web_element(self, locator):
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

    def is_displayed(self, locator, mark=True):
        """
        判断某个元素是否存在
        :param locator:
        :return:
        """
        element = self.get_web_element(locator)
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
                self.wait(wait_seconds=seconds)
        except Exception as e:
            logging.error(e)
