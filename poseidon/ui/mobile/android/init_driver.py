# coding=utf-8

"""
@author:songmengyun
@file: init_driver.py
@time: 2020/01/06

"""


from appium import webdriver
from pytest_testconfig import config as pyconfig


def get_desired_caps(desired_caps=None):
    '''判断是否传入desired_caps，如果传入直接返回，如果不传入取pytest.ini中配置'''

    if desired_caps:
        return desired_caps
    else:
        if 'mobile' in pyconfig:
            desired_caps = pyconfig.get('mobile', None)
        else:
            desired_caps = desired_caps
        return desired_caps

def init_driver(desired_caps=None, command_executor='http://localhost:4723/wd/hub',
                browser_profile=None, proxy=None, keep_alive=True, direct_connection=False):
    '''
    手机驱动对象初始化: 如果传入desired_caps，取desired_caps中信息，如果未传入，获取pytest.ini中配置；如果都没有传入，返回None
    :return: 返回driver对象
    '''

    _desired_caps = get_desired_caps(desired_caps)
    if 'command_executor' in _desired_caps:
        _desired_caps.pop('command_executor')
    try:
        driver = webdriver.Remote(command_executor, _desired_caps,
                                  browser_profile=browser_profile, proxy=proxy,
                                  keep_alive=keep_alive, direct_connection=direct_connection)
        return driver
    except Exception as e:
        raise e






