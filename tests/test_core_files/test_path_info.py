#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-18
"""
from poseidon.core.files.utils import *
import os


class TestPathInfo:
    def test_project_path(self):
        _project_path = get_project_path_info().get("project_path")
        _dir_list = _project_path.split(os.sep)
        assert "Poseidon" == _dir_list[-1]

    def test_poseidon_path(self):
        _poseidon_path = get_project_path_info().get("poseidon_path")
        _dir_list = _poseidon_path.split(os.sep)
        assert "poseidon" == _dir_list[-1]
