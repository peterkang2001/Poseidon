#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-16
"""
import os
from poseidon.core.files import utils


def command_start(name):
    # 暂时将工作目录设置为project_path
    _home = utils.get_project_path_info().get("project_path")
    utils.chdir_to_project()
    # if utils.dir_is_exists(name):
    #     print("yes")
    # else:
    #     print("no")
