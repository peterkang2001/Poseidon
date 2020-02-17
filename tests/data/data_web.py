# coding=utf-8

"""
@author:songmengyun
@file: data_web.py
@time: 2019/12/25

"""


from poseidon.base.Env import Env
from poseidon.base import CommonBase as cb
from selenium.webdriver.common.by import By


class DataWeb():

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






data_web = DataWeb()

