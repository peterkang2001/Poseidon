#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-17
"""
import os
import sys
from poseidon.core.exceptions import *

def dir_is_exists(path):
    if os.path.exists(path):
        return True
    else:
        raise DirectoryNotFoundException()

def file_is_exists(path):
    if os.path.exists(path):
        return True
    else:
        raise FileNotFoundException()


def get_project_path_info():
    """
    获取项目路径
    project_path 指整个git项目的目录
    poseidon_path 指git项目中名字叫poseidon的目录
    """
    _poseidon_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    _project_path = os.path.dirname(_poseidon_path)
    return {"project_path": _project_path,
            "poseidon_path": _poseidon_path}
