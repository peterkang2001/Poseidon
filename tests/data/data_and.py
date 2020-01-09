# coding=utf-8

"""
@author:songmengyun
@file: data_and.py
@time: 2020/01/07

"""
from poseidon.base.Env import Env
from poseidon.base import CommonBase as cb
from selenium.webdriver.common.by import By

class DataAndroid():

    @property
    def url(self):  # 百度首页
        return cb.get_value_from_env_data_dict({
            Env.qa: ['https://www.baidu.com','百度一下，你就知道']
        })

    @property
    def search_box(self):  # 百度首页
        return cb.get_value_from_env_data_dict({
            Env.qa: (By.XPATH, '//*[@id="kw"]')
        })

    @property
    def search_button(self):  # 百度首页
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.XPATH, '//*[@id="su"]'),'poseidon_百度搜索']
        })
