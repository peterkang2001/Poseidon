#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-06
"""

from enum import Enum
from pytest_testconfig import config as pyconfig

class Env(Enum):
    """
    测试环境枚举
    """
    qa = "qa环境"
    yz = "yz环境"
    prod = "生产环境"

    @staticmethod
    def curEnv():
        if 'qa' in pyconfig['env']:
            return Env.qa
        elif 'yz' in pyconfig['env']:
            return Env.yz
        elif 'prod' in pyconfig['env']:
            return Env.prod
        else:
            return Env.qa


