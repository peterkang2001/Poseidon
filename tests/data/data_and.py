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
    def app_path(self):  # 百度首页
        return cb.get_value_from_env_data_dict({
            Env.qa: {'dict': '/Users/songmengyun/Poseidon-master/tests/hjdict2_hujiang_3.4.1.259.241819.apk',
                     'setting': ''
                     },
        })

    @property
    def dict_info(self):  # 百度首页
        return cb.get_value_from_env_data_dict({
            Env.qa: {'app_package':'com.hjwordgames',
                     'app_activity':'com.hujiang.browser.view.X5HJWebViewActivity'}
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


data_and = DataAndroid()
