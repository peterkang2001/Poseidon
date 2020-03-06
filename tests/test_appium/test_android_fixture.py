# coding=utf-8

"""
@author:songmengyun
@file: test_android_fixture.py
@time: 2020/01/07

"""


import pytest
import time
import logging
from collections import namedtuple
from poseidon.ui.mobile.android.init_driver import init_driver


@pytest.fixture(scope='function')
def driver_base(request):
    logging.info('setup case'.center(50, "*"))
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '192.168.57.103:5555',
        'platformVersion': '6.0',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'newCommandTimeout':120,
        'noReset': "True"  # 启动app时不要清除app里的原有的数据
    }
    driver = init_driver(desired_caps, command_executor='http://localhost:4723/wd/hub')
    def fin():
        logging.info("teardown case".center(50, "*"))
        driver.quit()
    request.addfinalizer(fin)

    return driver

App = namedtuple('app_info', ['appPackage', 'appActivity'])
class TestAndroid:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which usually contains tests).
        """
        cls.app_mis = App('com.android.messaging', '.ui.conversationlist.ConversationListActivity')   # 设备的名称，随便写，但不能为空

    @classmethod
    def teardown_class(cls):
        pass

    def test_start_activity(self, driver_base):
        '''打开app：使用自定义fixture: driver_base'''

        time.sleep(3)
        driver_base.start_activity(self.app_mis.appPackage, self.app_mis.appActivity)

    def test_start_activity2(self, driver_android):
        '''打开app：使用默认fixture：driver_android，默认获取pytest.ini中配置'''

        time.sleep(3)
        driver_android.start_activity(self.app_mis.appPackage, self.app_mis.appActivity)
