# coding=utf-8

"""
@author:songmengyun
@file: data_android.py
@time: 2020/02/28

"""

from poseidon.base.Env import Env
from poseidon.base import CommonBase as cb
from selenium.webdriver.common.by import By

class DataAndroid():

    @property
    def app_path(self):  # 开心词场
        return cb.get_value_from_env_data_dict({
            Env.qa: {'dict': '/Users/songmengyun/Poseidon-master/tests/hjdict2_hujiang_3.4.1.259.241819.apk',
                     'setting': ''
                     },
        })

    @property
    def dict_info(self):  # 帐密登录页面
        return cb.get_value_from_env_data_dict({
            Env.qa: {'app_package':'com.hjwordgames',
                     # 'app_activity':'com.hujiang.browser.view.X5HJWebViewActivity'
                     'app_activity':'.activity.GuideLoginActivity'
                     }
        })

    @property
    def start_immediately(self):   # 点击立即开启
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.ID, 'com.hjwordgames:id/guide_action_sign_in_or_login'), '']
        })


    @property
    def username_pwd_button(self):  # 帐密登录按钮
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.XPATH, "//*[@content-desc='帐号密码登录']"), '']
        })

    @property
    def username_pwd_login(self):  # 用户名+密码+登录按钮
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.XPATH, "//*[@content-desc='手机号／邮箱／用户名']"),
                     (By.XPATH, "//*[@NAF='true']"),
                     (By.XPATH, "//*[@content-desc='登录']")]
        })


data_and = DataAndroid()

