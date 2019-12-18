#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-17
"""
from poseidon.core.files.utils import file_is_exists, dir_is_exists
from poseidon.core.exceptions import *
import pytest
import os
class Test_file_exists:
    def test_file_is_exists(self):
        """
        目标文件存在
        """
        current_dir = os.getcwd()
        _target_file = os.path.join(current_dir, 'test_file_is_exists.py')
        assert file_is_exists(_target_file)

    def test_file_is_not_exists(self):
        """
        目标文件不存在
        """
        current_dir = os.getcwd()
        _target_file = os.path.join(current_dir, 'not_exists.py')
        assert not file_is_exists(_target_file)


    def test_directory_is_exists(self):
        """
        目标目录存在
        """
        current_dir = os.getcwd()
        assert dir_is_exists(current_dir)

    def test_directory_is_not_exists(self):
        """
        目标目录不存在
        """
        current_dir = os.getcwd()
        _target_dir = os.path.join(current_dir, "hello")
        assert not dir_is_exists(_target_dir)
