# coding=utf-8

"""
@author:songmengyun
@file: test_case1.py
@time: 2019/12/18

"""

import pytest
from poseidon.base.Env import Env
from poseidon.base.Frequency import Frequency

class Test_demo:

    @classmethod
    def setup_class(self):
        pass

    def setup_method(self):
        pass

    @pytest.fixture(scope='function')
    def get_url(self, url):
        return url

    @pytest.mark.run([Env.qa, Env.yz, Env.prod], [Frequency.five_min])
    def test_001(self):
        print('running test success')
