# coding=utf-8

"""
@author:songmengyun
@file: test_web.py
@time: 2019/12/17

"""

import pytest
import time
from poseidon.base.Env import Env
from poseidon.base.Frequency import Frequency
from selenium import webdriver
from tests.business.bus_web import page

'''
前提条件：
1. 下载对应chromedriver
2. mac电脑把chromedriver放在/usr/local/bin，会默认读取
3. 安装pytest-selenium, 默认安装poseidon会包含

'''



class TestBaidu():

    @pytest.mark.run([Env.qa, Env.yz, Env.prod], [Frequency.five_min])
    def test_baidu_search(self, driver):
        '''验证百度搜索'''

        baidu = page("baidu", driver)
        baidu.open_baidu_url('【step1】打开百度页面')
        baidu.input_text_and_search('【step2】输入poseidon并验证搜索结果')

    @pytest.mark.run([Env.qa, Env.yz, Env.prod], [Frequency.five_min])
    def test_headless(self):
        options = webdriver.ChromeOptions()   # option对象
        options.add_argument('headless')    # 给option添加属性
        driver = webdriver.Chrome(options=options)
        driver.get('http://www.baidu.com')
        time.sleep(3)
        driver.close()
