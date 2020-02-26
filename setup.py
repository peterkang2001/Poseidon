#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-13
"""

# python setup.py sdist
# python setup.py bdist_wheel   # 官方推荐的打包方式


import sys

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

# check Python version.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================

This version of Poseidon requires Python {}.{}, but you're trying to
install it on Python {}.{}.

This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:

    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install Poseidon-test

This will install the latest version of Poseidon which works on your
version of Python. If you can't upgrade your pip (or Python), request
an older version of Poseidon.

""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)


from setuptools import setup, find_packages
# from poseidon.core.version import update_set_cfg_version

# update_set_cfg_version()
setup(
    setup_requires=['setuptools_scm'],
    use_scm_version=True
)


