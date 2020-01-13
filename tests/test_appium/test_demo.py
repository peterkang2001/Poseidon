# coding=utf-8

"""
@author:songmengyun
@file: test_demo.py
@time: 2020/01/10

"""

import pytest
import logging
from poseidon.ui.mobile.android.init_driver import init_driver
from tests.data.data_and import data_and
from tests.business.pages.search_page import SearchPage

@pytest.fixture(scope='function')
def driver_dict(request):
    logging.info('setup case'.center(50, "*"))
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '192.168.57.103:5555',
        'platformVersion': '6.0',
        # 'appPackage': 'com.android.settings',
        # 'appActivity': '.Settings',
        'newCommandTimeout':120,
        'noReset': True  # 启动app时不要清除app里的原有的数据
    }
    driver = init_driver(desired_caps, command_executor='http://localhost:4723/wd/hub')
    def fin():
        logging.info("teardown case".center(50, "*"))
        driver.quit()
    request.addfinalizer(fin)
    return driver

class TestAndroidDemo():

    @classmethod
    def setup_method(cls):
        cls.app_path = data_and.app_path
        cls.dict_path = cls.app_path['dict']


    def test_touch_action(self, driver_dict):
        search_page = SearchPage(driver_dict)
        logging.info('测试打开百度-搜索用户信息')
        search_page.check_and_install_app(self.dict_path, describe='判断百度app是否安装，若未安装，执行安装')



