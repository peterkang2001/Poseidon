#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-06
"""

from enum import Enum

class Frequency(Enum):
    """
    用例执行评率枚举
    """
    one_min = "1分钟"
    five_min = "5分钟"
    one_hour = "1小时"
    one_day = "1天"
    one_week = "1周"


