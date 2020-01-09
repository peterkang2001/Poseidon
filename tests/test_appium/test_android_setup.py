# coding=utf-8

"""
@author:songmengyun
@file: test_android_setup.py
@time: 2020/01/07

"""


import pytest
import time
import logging
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.connectiontype import ConnectionType

from collections import namedtuple
from poseidon.ui.mobile.android.init_driver import init_driver



'''
Android 6.0 
包名和界面名
设置：com.android.settings/.Settings
短信：com.android.messaging/.ui.conversationlist.ConversationListActivity
系统浏览器：com.android.browser/.BrowserActivity
联系人：com.android.contacts/.activities.PeopleActivity
英语口语700句：com.hj.kouyu700/com.hujiang.browser.JSWebViewActivity
cctalk登录页面：com.hujiang.cctalk/com.hujiang.browser.view.X5HJWebViewActivity
安智市场：cn.goapk.market/com.anzhi.market.ui.MainActivity
京东：com.jingdong.app.mall/.main.MainActivity


'''

App = namedtuple('app_info', ['appPackage', 'appActivity'])
class TestAndroid:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which usually contains tests).
        """
        logging.info('setup_class'.center(50, "*"))
        cls.app_mis = App('com.android.messaging', '.ui.conversationlist.ConversationListActivity')  # 设备的名称，随便写，但不能为空

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to setup_class.
        """
        logging.info('teardown_class'.center(50, "*"))

    def setup_method(self, method):
        """ 所有case初始化操作 """
        logging.info('setup_method'.center(50, '*'))
        self.driver = init_driver('Android',
                                  '6.0',
                                  '192.168.57.103:5555',
                                  'com.android.settings',
                                  '.Settings',
                                  command_executor='http://localhost:4723/wd/hub')

    def teardown_method(self, method):
        logging.info('teardown_method'.center(50, '*'))
        self.driver.quit()

    def test_start_activity(self):
        '''打开其他app：setup/teardown'''

        time.sleep(3)
        self.driver.start_activity(self.app_mis.appPackage, self.app_mis.appActivity)

