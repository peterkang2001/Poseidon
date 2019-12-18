#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-17
"""
import os
import sys
from Poseidon.core.files.files_exception import *

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
