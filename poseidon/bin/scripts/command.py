#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-16
"""
from poseidon.core.files import utils
from poseidon.core import output


def command_start(project_name):
    _work_path = utils.get_workpath()
    _project_path = utils.get_project_path(project_name)


    if not utils.dir_is_exists(project_name):
        # 创建项目目录
        if utils.mkdirs(project_name):
            output.info("创建目录 {} 成功".format(project_name))

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
        output.err("创建目录 {} 失败: 该目录已存在".format(project_name))
        return 1
