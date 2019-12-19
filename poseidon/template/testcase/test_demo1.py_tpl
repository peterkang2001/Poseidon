# coding=utf-8

"""
@author:songmengyun
@file: test_demo1.py
@time: 2019/12/17

"""

import pytest
from poseidon.template.data.data_base import data_base as base
from poseidon.template.business.bus_base import bus_base as biz
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
