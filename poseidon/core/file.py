#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-16
"""
import os
import sys
from poseidon.core.exceptions import *

def directory_is_exists(path):
    """判断目录是否存在"""
    if os.path.exists(path):
        return True
    else:
        raise DirectoryNotFoundException


def file_is_exists(path):
    """判断文件是否存在"""
    if os.path.exists(path):
        return True
    else:
        raise FileNotFoundException
