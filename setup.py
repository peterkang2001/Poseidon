#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-13
"""

# python setup.py sdist
# python setup.py bdist_wheel   # 官方推荐的打包方式
# python setup.py sdist upload -r http://qa.pip.yeshj.com


from setuptools import setup, find_packages

# setup()


with open('README.md', 'r', encoding='utf-8') as rd:
    long_description = rd.read()


setup(
    name="Poseidon-test",  # 项目名称，保证它的唯一性，不要跟已存在的包名冲突即可
    version="0.0.1",  # 版本
    author="Poseidon Software Foundation", # 项目作者
    author_email="foundation@poseidon.com",
    description="基于Python技术栈的自动化测试框架", # 项目的一句话描述
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="PSF",
    keywords="poseidon, pytest, appium, selenium, node",
    url="https://github.com/peterkang2001/Poseidon",# 项目地址
    project_urls={   # 项目其他地址
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
    },
    packages=find_packages(exclude=['scripts', 'tests']),
    package_data = {
        '': ['*.ini', '*.py_tpl'],
    },
    install_requires=[
        "Click>=7.0",
        # "pytest>=5.3.1",
        # "pytest-html>=2.0.1",
        # "pytest-testconfig",
        # "request",
        # "pytest-json",
        # "pytest-selenium",
        # "SQLAlchemy",
        # "pyDes",
        # "pymemcache",
        # "redis",
        # "requests_toolbelt"
    ],

    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
