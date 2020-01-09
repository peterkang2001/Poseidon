#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-06-04
"""
import logging
from selenium.webdriver.common.by import By
from poseidon.ui.util.location import *
import time
# from poseidon.base.log_level import Level

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # def write(self, msg, level=Level.info):
    #     """
    #     该方法统一日志记录的方式，未来可以在这里补充除了记录log之外的记录
    #     如 往db中插入操作日志，这样只需要修改一个地方即可完成所有的改动
    #     :param msg:
    #     :param level:
    #     :return:
    #     """
    #     if level == Level.info:
    #         logging.info(msg)
    #     elif level == Level.debug:
    #         logging.debug(msg)
    #     elif level == Level.warning:
    #         logging.warning(msg)
    #     elif level == Level.error:
    #         logging.error(msg)
    #     elif level == Level.critical:
    #         logging.critical(msg)
    #     else:
    #         logging.error("输入错误的level请确认")

    def open(self,url):
        logging.info("执行open方法，打开网页:{}".format(url))
        self.driver.get(url)

    def click_element(self, locator, is_button=True):
        """
        点击
        :param locator:
        :param is_button:
        :return:
        """
        element = self.get_web_element(locator)
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
            text_field = self.get_web_element(locator)
            text_field.clear()
            text_field.send_keys(values)
        except Exception as msg:
            logging.error(msg)

    def wait(self, wait_seconds=5):
        """
        公共等待方法
        :param wait_seconds:
        :return:
        """
        time.sleep(wait_seconds)

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

