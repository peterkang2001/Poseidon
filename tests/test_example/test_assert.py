#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Author:       songmengyun
   date:         2019-05-17
"""

import pytest
import time
from poseidon.base.Env import Env
from poseidon.base.Frequency import Frequency

class Test_assert:

    #region string类型
    @pytest.mark.parametrize(
        ("n", "expected"),
        [
            (1,2),
            (2,3)
        ],
        ids=('aa测试1', 'bb测试2')
        # ids=('aa', 'bb')
    )
    @pytest.mark.run([Env.qa],[Frequency.five_min])
    def test_string_one(self, n, expected):
        """
        英文字符相等比较，其中一个大另外一个小
        """
        assert "pytest" == "pytest"
        import logging
        logging.info("dodododod")
        logging.error("dodododod")
        print("dodododo")
        time.sleep(1)


    @pytest.mark.run([Env.qa],[Frequency.five_min])
    def test_string_two(self):
        """
        失败：英文字符不等比较

        """
        time.sleep(2)
        assert "pytest" == "pytest1", "error info"

    @pytest.mark.run([Env.qa],[Frequency.five_min])
    def test_string_three(self):
        """
        英文字符相等比较，错误后捕获预计异常
        """

        with pytest.raises(AssertionError) as excinfo:
            assert "pytest" == "pytest1", "error info"
        assert 'error info' in str(excinfo.value)
        print("value: {}".format(excinfo.value))
        print("type: {}".format(excinfo.type))
        print("traceback: {}".format(excinfo.traceback))

    @pytest.mark.run([Env.qa,Env.yz, Env.prod],[Frequency.one_min])
    def test_string_four(self):
        # 中文字符相等比较
        assert "pytest测试框架" == "pytest测试框架", "error info"

    @pytest.mark.run([Env.qa,Env.yz, Env.prod],[Frequency.five_min])
    def test_string_five(self):
        '''中文字符不等比较'''
        assert "pytest测试框架" != "pytest测试框架1", "error info"
    # endregion

    # region set类型
    @pytest.mark.run([Env.qa,Env.yz, Env.prod],[Frequency.one_min])
    def test_set_one(self):
        '''预计set相等比较'''
        a = set("pytest")
        b = set("pytest")
        assert a == b

    @pytest.mark.run([Env.qa,Env.yz, Env.prod],[Frequency.five_min])
    def test_set_two(self):
        '''预计set不等比较'''
        a = set("pytest1")
        b = set("pytest")
        assert a != b

    @pytest.mark.run([Env.qa,Env.yz, Env.prod],[Frequency.one_min])
    def test_set_three(self):
        '''set子集判断'''
        a = set("pytest1")
        b = set("pytest")
        assert b <= a
        assert b < a

        #中文子集判断
        c = set("测试框架我")
        d = set("测试框架")
        assert  c > d

        e = set()
        assert e < d
        assert d > e



    #endregion

    #region list类型
    @pytest.mark.run([Env.qa,Env.yz, Env.prod],[Frequency.five_min])
    def test_list_one(self):
        '''验证2个list相等'''
        a = list(set("测试框架"))
        b = list(set("测试框架"))
        c = list(set("测试框架我"))
        d = list()

        assert a == b
        assert a != c
        assert a != d
        assert d < a
        assert d <= a

        #顺序不同
        e = ["测", "测试", "框架"]
        f = ["测试","测",  "框架"]
        assert e != f
        assert e.sort() == f.sort()
    #endregion

    # region dict类型
    @pytest.mark.run([Env.qa,Env.yz, Env.prod],[Frequency.five_min])
    def test_dict_one(self):
        '''验证2个dict相等'''
        a = {"name":"测试框架", "value": "value1"}
        b = {"name":"测试框架", "value": "value1"}
        c = { "value": "value1","name":"测试框架"}
        d =  {"name":"测试框架"}

        # assert a == b
        # assert a == c
        # assert d != a


    # endregion
