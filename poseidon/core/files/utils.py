#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-17
"""
import os
import sys
from poseidon.core.files import utils

def dir_is_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False

def file_is_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False


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


def chdir_to_project():
    """切换工作目录到git项目根目录"""
    try:
        _home = utils.get_project_path_info().get("project_path")
        os.chdir(_home)
        sys.stdout.write("切换工作目录到{}\n".format(_home))
        return True
    except Exception as e:
        sys.stderr.write("{}\n".format(e))
        return False
