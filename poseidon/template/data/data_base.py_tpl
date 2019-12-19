# coding=utf-8

"""
@author:songmengyun
@file: data_base.py
@time: 2019/12/17

"""

import random
from poseidon.base.Env import Env
from poseidon.base import CommonBase as cb


class DataBase():

    @property
    def url(self):
        return cb.get_value_from_env_data_dict(
            {
                Env.qa: 'http://qa.wwww.demo.com',
                Env.yz: 'http://yz.wwww.demo.com',
                Env.prod: 'http://wwww.demo.com'
            })

data_base = DataBase()
