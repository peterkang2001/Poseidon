# coding=utf-8

"""
@author:songmengyun
@file: search_page.py
@time: 2020/01/07

"""

from poseidon.ui.mobile.android.base_page import BasePage
from tests.data.data_and import data_and

import time
import logging

class SearchPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.dict_info = data_and.dict_info
        super().__init__(driver=self.driver)

    def check_and_install_app(self, app_path:str, describe:str):
        logging.info(describe)
        self.install_app(app_path, self.dict_info['app_package'])

