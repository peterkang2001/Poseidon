#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-17
"""

import os
import shutil
from poseidon.core import output

def work_path():
    '''获取当前目录'''
    return os.getcwd()

def project_path(project_name):
    '''获取项目目录'''
    _work_path = work_path()
    return os.path.join(_work_path, project_name)

def dir_is_exists(path):
    '''判断路径是否存在'''
    if os.path.exists(path):
        return True
    else:
        return False

def file_is_exists(path):
    '''判断文件是否存在'''
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

def mkdirs(path, model=None):
    '''更具path创建目录'''
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
    '''复制目录'''
    _pip_local_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    _src = os.path.join(_pip_local_path, 'template', target_dir)

    dest_path = os.path.join(dest_path, target_dir)
    # print("来源地址{}".format(_src))
    # print("目的地址{}".format(dest_path))
    try:
        shutil.copytree(_src, dest_path, ignore=shutil.ignore_patterns('__pycache__'))
        output.info(f"脚手架创建 {target_dir} 完毕")
    except Exception as e:
        output.err(f"脚手架创建 {target_dir} 失败")
        output.err(e)

def copy_tpl_file(dest_path, file):
    '''复制文件'''
    _pip_local_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    _src_file = os.path.join(_pip_local_path, 'template', file)
    _dest_file = os.path.join(dest_path, file)

    # print("来源文件地址{}".format(_src_file))
    # print("目标文件地址{}".format(_dest_file))
    try:
        shutil.copyfile(_src_file, _dest_file)
        output.info(f"脚手架创建 {_dest_file} 完毕")
    except Exception as e:
        output.err(f"脚手架创建 {_dest_file} 失败")
        output.err(e)
