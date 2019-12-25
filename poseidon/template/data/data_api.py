# coding=utf-8

"""
@author:songmengyun
@file: data_api.py
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
                Env.qa: 'https://api.apiopen.top/searchMusic',
                Env.yz: 'https://api.apiopen.top/searchMusic',
                Env.prod: 'https://api.apiopen.top/searchMusic'
            })






data_base = DataBase()
