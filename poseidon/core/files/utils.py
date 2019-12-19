#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-17
"""
import os
from poseidon.core.files import utils
from poseidon.core import output
import shutil

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


def get_workpath():
    return os.getcwd()


def get_project_path(project_name):
    _workpath = get_workpath()
    return os.path.join(_workpath, project_name)

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


def chdir_to_project_home_path():
    """切换工作目录到git项目根目录"""
    try:
        _home = utils.get_project_path_info().get("project_path")
        os.chdir(_home)
        # output.info("切换工作目录到{}".format(_home))
        return True
    except Exception as e:
        output.err(e)
        return False


def mkdirs(path, model=None):
    try:
        if model is None:
            os.makedirs(path)
        else:
            os.makedirs(path, model)
        # 创建完毕进行校验
        if dir_is_exists(path):
            return True
        else:
            output.err("创建目录失败")
            return False
    except Exception as e:
        output.err(e)
        return False


def copy_tpl_tree(dest_path, target_dir):
    _pip_local_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    _src = os.path.join(_pip_local_path, 'template', target_dir)
    print("来源地址{}".format(_src))
    print("目的地址{}".format(dest_path))
    try:
        shutil.copytree(_src, dest_path)
        output.info("脚手架创建 {} 完毕".format(target_dir))
    except Exception as e:
        output.err("脚手架创建 {} 失败".format(target_dir))
        output.err(e)
