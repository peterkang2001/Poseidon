#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-16
"""
import os
import sys

def directory_is_exists(path):
    """判断目录是否存在"""
    if os.path.exists(path):
        sys.stdout.write("目录不存在")
    else:
        sys.stdout.write("目录不存在")


