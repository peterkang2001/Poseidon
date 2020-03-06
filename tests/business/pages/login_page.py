# coding=utf-8

"""
@author:songmengyun
@file: login_page.py
@time: 2020/01/07

"""

from poseidon.ui.mobile.android.base_page import BasePage
from tests.data.data_and import data_and
from poseidon.base import CommonBase as cb

import time
import logging

class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.dict_info = data_and.dict_info
        super().__init__(driver=self.driver)

    def check_and_install_app(self, app_path:str, describe:str) -> None:
        if describe: logging.info(describe)
        self.uninstall_app(self.dict_info['app_package'])
        self.install_app(app_path, self.dict_info['app_package'])

    def check_and_uninstall_app(self, describe:str) -> None:
        if describe: logging.info(describe)
        self.uninstall_app(self.dict_info['app_package'])

    def open_cichang_app(self, describe:str) -> None:
        if describe: logging.info(describe)
        self.open_app(self.dict_info['app_package'], self.dict_info['activity_limit'])
        time.sleep(5)
        if self.find_item('沪江开心词场需要以下权限 才可正常使用'):
            self.open_cichang_limit()


    def open_login_page(self, describe:str) -> None:
        if describe: logging.info(describe)
        self.open_app(self.dict_info['app_package'], self.dict_info['activity_login'])

    def open_cichang_limit(self):
        '''开启手机/电话/存储权限'''
        self.click_element(data_and.limit[0])
        time.sleep(2)
        self.click_element(data_and.limit[1])
        time.sleep(2)
        self.click_element(data_and.limit[2])
        time.sleep(4)

    def click_start_immediately(self, describe:str) -> None:
        if describe: logging.info(describe)
        time.sleep(2)
        self.click_element(data_and.start_immediately[0])
        time.sleep(10)

    def click_uname_pwd_login(self, describe:str) -> None:
        if describe: logging.info(describe)
        self.click_username_pwd_login()
        time.sleep(3)

    def login_pass(self, describe:str=None) -> None:
        if describe: logging.info(describe)

        # logging.info('第1步：进入H5页面')
        # cons = self.driver.contexts  # 获取全部上下文
        # logging.info(cons)
        # self.switch_h5_app(cons[1])
        # logging.info(self.current_content())
        # logging.info(self.driver.page_source)

        logging.info('第1步：输入用户名')
        self.set_text(data_and.username_pwd_login[0], data_and.user[0])
        time.sleep(1)

        logging.info('第2步：输入密码')
        self.set_text(data_and.username_pwd_login[1], data_and.user[1])
        time.sleep(1)

        logging.info('第3步：点击登录按钮')
        self.click_element(data_and.username_pwd_login[2])
        time.sleep(10)

    def logout_pass(self, describe:str=None) -> None:
        if describe: logging.info(describe)
        logging.info('点击我的')
        self.click_element(data_and.cichang_my[0])
        time.sleep(2)
        logging.info('点击设置')
        self.click_element(data_and.cichang_setting[0])
        time.sleep(2)
        logging.info('点击设置-账号')
        self.click_element(data_and.cichang_setting_account[0])
        time.sleep(2)
        logging.info('点击设置-账号-退出')
        self.click_element(data_and.cichang_setting_account_logout[0])
        time.sleep(2)
        logging.info('点击设置-账号-退出-确定')
        self.click_element(data_and.cichang_setting_account_logout_right_button[0])
        time.sleep(10)


    @cb.com_try_catch
    def click_username_pwd_login(self):
        self.click_element(data_and.username_pwd_button[0])

