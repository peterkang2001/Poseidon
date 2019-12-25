#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-25
"""

import time


def get_timestamp(type=None):
    _localtime = time.localtime(time.time())
    if type is None or type == 1:
        _year = "{}".format(_localtime.tm_year)[2:]
        _month = "{:0>2d}".format(_localtime.tm_mon)
        _day = "{:0>2d}".format(_localtime.tm_mday)
        _hour = "{:0>2d}".format(_localtime.tm_hour)
        return "{year}{month}{day}{hour}".format(year=_year,
                                                 month=_month,
                                                 day=_day,
                                                 hour=_hour)
    else:
        return _localtime
