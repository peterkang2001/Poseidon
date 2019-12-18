#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-13
"""
import random
def get_version():
    return f'v1-{random.choice(range(10000))}'

__version__ = f'0.0.{random.choice(range(10000))}'

