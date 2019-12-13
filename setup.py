#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-13
"""
from setuptools import setup, find_packages


setup(
    name='poseidon-test',
    # 版本信息
    version='0.0.1',
    description='基于Python技术栈的API测试框架',
    keywords = ['Poseidon', 'pytest', 'test', 'testframework'],

    platforms = "any",
    url="https://peterkang2001.github.io/info/",
    author="kangliang",
    author_email="peterkang2001@gmail.com",

    packages=[
        # 'Tetis',
        # 'Tetis.api',
        # 'Tetis.base',
        # 'Tetis.plugins',
        # 'Tetis.ui.android',
        # 'Tetis.ui.ios',
        # 'Tetis.ui.mobile',
        # 'Tetis.ui.pc',
        # 'Tetis.ui.util',
    ],

    include_package_data=True,  # 自动打包文件夹内所有数据
    zip_safe=False,  # 设定项目包为安全，不用每次都检测其安全性

    install_requires = [
        # 'PyYAML',
        # "requests",
        # "pytest",
        # "request",
        # 'pytest-json',
        # 'pytest-testconfig',
        # 'urllib3',
    ],

    entry_points = {
        'pytest11': [
            'Tetis = Tetis.plugins.deathtrap_coral',
            'pc_ui_fixture = Tetis.plugins.light_of_the_mermaid'
        ]
    },
    classifiers = ["Framework :: Pytest"]
)
# python setup.py sdist