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
    def app_path(self):  # 开心词场
        return cb.get_value_from_env_data_dict({
            Env.qa: {'dict': '/Users/songmengyun/automation/poseidon/tests/hjwordgames_hujiang_6.9.5.530.071802.apk',
                     'setting': ''
                     },
        })

    @property
    def dict_info(self):  # 帐密登录页面
        return cb.get_value_from_env_data_dict({
            Env.qa: {'app_package':'com.hjwordgames',
                     'activity_login':'.activity.GuideLoginActivity',
                     'activity_limit': '.Splash',
                     }
        })

    @property
    def start_immediately(self):   # 点击立即开启
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.ID, "com.hjwordgames:id/guide_action_sign_in_or_login"), '']
        })

    @property
    def username_pwd_button(self):  # 帐密登录按钮
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.XPATH, "//*[@content-desc='帐号密码登录']"), '']
        })

    @property
    def username_pwd_login(self):  # 用户名+密码+登录按钮
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.XPATH, "//*[@text='手机号／邮箱／用户名']"),
                     (By.XPATH, "//*[@text='•••••']"),
                     (By.XPATH, "//*[@content-desc='登录']")]
        })

    @property
    def user(self):  # 登录用户
        return cb.get_value_from_env_data_dict({
            Env.qa: ['SMY0509', 'hujiang1234'],
        })

    @property
    def limit(self):  # 开启手机/电话/存储权限
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.ID, "com.hjwordgames:id/btn_start"),   # 开启按钮
                     (By.ID, "com.android.packageinstaller:id/permission_allow_button"),   # 存储权限允许
                     (By.ID, "com.android.packageinstaller:id/permission_allow_button")   # 电话权限允许

            ],
        })

    @property
    def cichang_my(self): # 我的
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.ID, "com.hjwordgames:id/tab_text"), '']
        })

    @property
    def cichang_setting(self): # 设置
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.ID, "com.hjwordgames:id/v_setting_img"), '']
        })

    @property
    def cichang_setting_account(self): # 设置-账号
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.ID, "com.hjwordgames:id/setting_user"), '']
        })

    @property
    def cichang_setting_account_logout(self): # 设置-账号-退出按钮
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.ID, "com.hjwordgames:id/logout_bt"), '']
        })

    @property
    def cichang_setting_account_logout_right_button(self): # 设置-账号-退出按钮-退出确认
        return cb.get_value_from_env_data_dict({
            Env.qa: [(By.ID, "com.hjwordgames:id/right_button"), '']
        })



data_and = DataAndroid()
