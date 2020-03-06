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
from tests.business.pages.login_page import LoginPage
from poseidon.base.Env import Env
from poseidon.base.Frequency import Frequency

@pytest.fixture(scope='function')
def driver_dict(request):
    logging.info('setup case'.center(50, "*"))
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '192.168.57.104:5555',
        'platformVersion': '7.1',
        # 'automationName': 'uiautomator2',
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


    @pytest.mark.run([Env.qa], [Frequency.five_min])
    def test_touch_action(self, driver_dict):
        login_page = LoginPage(driver_dict)
        logging.info('测试安装词场app并登录')
        login_page.check_and_install_app(self.dict_path, describe='安装app')
        login_page.open_cichang_app(describe='打开词场登录页面')
        login_page.click_start_immediately(describe='点击立即开启')
        login_page.click_uname_pwd_login(describe='点击帐号+密码登录')
        login_page.login_pass(describe='帐号+密码登录，H5页面')
        login_page.logout_pass(describe='登出词场app')
        login_page.check_and_uninstall_app(describe='卸载app')




