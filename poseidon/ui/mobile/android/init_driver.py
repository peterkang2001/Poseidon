# coding=utf-8

"""
@author:songmengyun
@file: init_driver.py
@time: 2020/01/06

"""

from appium import webdriver


def init_driver(platformName, platformVersion, deviceName, appPackage, appActivity,
                command_executor='http://localhost:4723/wd/hub',
                *args, **kwargs):
    '''
    手机驱动对象初始化
    :return:
    '''
    desired_caps = {}
    desired_caps['platformName'] = platformName
    desired_caps['platformVersion'] = platformVersion   # 设备号
    desired_caps['deviceName'] = deviceName   # 包名
    desired_caps['appPackage'] = appPackage    # Activity
    desired_caps['appActivity'] = appActivity

    driver = webdriver.Remote(command_executor, desired_caps,
                              browser_profile=None, proxy=None,
                              keep_alive=True, direct_connection=False)

    # 将driver对象返回
    return driver
