# coding=utf-8

"""
@author:songmengyun
@file: test_example.py
@time: 2019/12/24

"""

import pytest
from datetime import datetime, timedelta
from tests.business.bus_api import bus_base as biz
from tests.data.data_api import data_base as base
from poseidon.base import CommonBase as cb
from poseidon.base.Env import Env
from poseidon.base.Frequency import Frequency


class TestAPIDemo:

    testdata = [
        (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
        (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
    ]

    @classmethod
    def setup_class(self):
        """ 所有case初始化操作 """
        self.music_name = '好久不见'
        self.url = biz.get_url(f"?name={self.music_name}", base.url)
        self.headers = {'Content-Type':'application/json'}

    @classmethod
    def teardown_class(cls):
        """ 所有case执行完后操作 """

    def setup_method(self):
        """ 每个case初始化操作 """
        print('')

    def teardown_method(self, method):
        """ 每个case执行完后操作"""


    @pytest.mark.run([Env.qa, Env.yz, Env.prod], [Frequency.five_min])
    def test_api_get_music_info(self):
        '''验证获取歌曲API成功'''
        send_data = {"method":'get', "url":self.url, "headers":self.headers}
        check_point = {"code":200, "message":"成功!"}
        biz.send_music_and_respnse(send_data, check_point)

    @pytest.mark.run([Env.qa, Env.yz, Env.prod], [Frequency.five_min])
    def test_commonbase(self):
        """验证commonbase中比较参数"""
        cb.checkEqual(1, 1)    # 比较n=expected
        cb.checkResultIsNotNone(2)    # 验证n不为空
        cb.checkDictionary({'a':1},{'a':1})   # 字典比较
        '''
        其他比较请查看 poseidon.base.Commonbase模块
        '''

    @pytest.mark.parametrize("a,b,expected", testdata)
    def test_parametrize(self, a, b, expected):
        ''' 验证parametrize'''
        diff = a - b
        cb.checkEqual(diff, expected)
