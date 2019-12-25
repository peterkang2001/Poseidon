#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-13
"""

# python setup.py sdist
# python setup.py bdist_wheel   # 官方推荐的打包方式


from setuptools import setup, find_packages
from poseidon.core.version import update_set_cfg_version

update_set_cfg_version()
setup()


