#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-16
"""

from poseidon.core.files import utils
from poseidon.core import output


def command_start(project_name):
    '''在当前目录下创建脚手架'''
    _project_path = utils.project_path(project_name)   # 项目目录

    if not utils.dir_is_exists(project_name):
        # 创建项目目录
        if utils.mkdirs(project_name):
            output.info(f"创建目录 {project_name} 成功")

        # 复制模板目录及目录下文件
        utils.copy_tpl_tree(dest_path=_project_path, target_dir='business')
        utils.copy_tpl_tree(dest_path=_project_path, target_dir='data')
        utils.copy_tpl_tree(dest_path=_project_path, target_dir='testcase')
        # 复制模板文件
        utils.copy_tpl_file(dest_path=_project_path, file='pytest.ini')
        utils.copy_tpl_file(dest_path=_project_path, file='.editorconfig')
        utils.copy_tpl_file(dest_path=_project_path, file='.gitignore')
        utils.copy_tpl_file(dest_path=_project_path, file='requirements.txt')
    else:
        output.err(f"创建目录 {project_name} 失败: 该目录已存在")
        return 1
