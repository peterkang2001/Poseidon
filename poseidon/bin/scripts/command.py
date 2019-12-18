#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-16
"""
# import shutil
# import os
from poseidon.core.file import *

def start(name):
    _project_name = None
    if name is None:
        _project_name = "mytest"
    else:
        _project_name = name


    directory_is_exists("aa")

# def create_empty_test_directory(name):



