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
        if utils.mkdirs(project_name):
            output.info("创建目录 {} 成功".format(project_name))
        # utils.copy_tpl_tree(project_name, 'business')
    #     # utils.copy_tpl_tree('data')
    #     # utils.copy_tpl_tree('testcase')
    else:
        output.err("创建目录 {} 失败: 该目录已存在".format(project_name))
        return 1
