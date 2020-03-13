# coding=utf-8

"""
@author:songmengyun
@file: test_1.py
@time: 2020/03/13

"""



import pytest
from datetime import datetime, timedelta
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
        print('setup_class')

    @classmethod
    def teardown_class(cls):
        """ 所有case执行完后操作 """
        print('teardown_class')

    def setup_method(self):
        """ 每个case初始化操作 """
        print('setup_method')

    def teardown_method(self, method):
        """ 每个case执行完后操作"""
        print('teardown_method')


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

    def test_assert(self):
        assert 1==1

    def test_match(self):
        with pytest.raises(ValueError, match=r".* 123 .*"):
            raise ValueError("Exception 123 raised")

    # def test_set_comparison(self):
    #     set1 = set("1308")
    #     set2 = set("8035")
    #     assert set1 == set2

    def test_skip(self):
        pytest.skip('暂时不处理')


