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
    # utils.chdir_to_project_home_path()


    if not utils.dir_is_exists(project_name):
        # 创建项目目录
        if utils.mkdirs(project_name):
            output.info("创建目录 {} 成功".format(project_name))

        # 复制项目文件
        utils.copy_tpl_tree(dest_path=_project_path, target_dir='business')
        utils.copy_tpl_tree(dest_path=_project_path, target_dir='data')
        utils.copy_tpl_tree(dest_path=_project_path, target_dir='testcase')
    else:
        output.err("创建目录 {} 失败: 该目录已存在".format(project_name))
        return 1
