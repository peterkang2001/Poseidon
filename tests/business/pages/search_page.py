# coding=utf-8

"""
@author:songmengyun
@file: search_page.py
@time: 2020/01/07

"""

from poseidon.ui.mobile.android.base_page import BasePage
from tests.data.data_and import data_and
from poseidon.base import CommonBase as cb

import time
import logging

class SearchPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.dict_info = data_and.dict_info
        super().__init__(driver=self.driver)

    def check_and_install_app(self, app_path:str, describe:str) -> None:
        if describe: logging.info(describe)
        self.install_app(app_path, self.dict_info['app_package'])

    def open_login_page(self, describe:str) -> None:
        if describe: logging.info(describe)
        self.open_app(self.dict_info['app_package'], self.dict_info['app_activity'])

    def click_start_immediately(self, describe:str) -> None:
        if describe: logging.info(describe)
        self.click_element(data_and.start_immediately[0])
        time.sleep(20)

    def click_uname_pwd_login(self, describe:str) -> None:
        if describe: logging.info(describe)
        self.click_username_pwd_login()
        time.sleep(3)

    def login_pass(self, describe:str=None) -> None:
        if describe: logging.info(describe)
        logging.info('第1步：输入用户名')
        self.set_text(data_and.username_pwd_login[0], 'SMY0509')
        logging.info('第2步：输入密码')
        time.sleep(1)
        self.set_text(data_and.username_pwd_login[1], 'hujiang1234')
        logging.info('第3步：点击登录按钮')
        time.sleep(1)
        self.click_element(data_and.username_pwd_login[2])

    @cb.com_try_catch
    def click_username_pwd_login(self):
        self.click_element(data_and.username_pwd_button[0])







