#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-19
"""
from poseidon.core.version_types import Types
from poseidon.core import datetime
from poseidon.core.files import utils
from pathlib import Path
from poseidon.core.files import ini_file
import configparser


def get_setup_cfg_handler():
    _project_path = utils.get_project_path_info().get("project_path")
    _project_path = Path(_project_path)
    _setup_cfg_path = _project_path.joinpath('setup.cfg')
    return _setup_cfg_path


def get_old_version():
    _setup_cfg_path = get_setup_cfg_handler()
    _old_version = ini_file.get_ini_info(_setup_cfg_path, 'metadata', 'version')
    return _old_version


def get_new_version(version_type=Types.Revision, step=1, suffix=None):
    _major, _minor, _others = get_old_version().split(".")
    _revision = _others.split("_")[0]
    try:
        _build = _others.split("-")[1]
    except Exception as e:
        pass

    if version_type == Types.Major:
        _major = int(_major) + step
    elif version_type == Types.Minor:
        _minor = int(_minor) + step
    elif version_type == Types.Revision:
        _revision = int(_revision) + step

    _build = datetime.get_timestamp(type=1)

    _new_version = "{major}.{minor}.{revision}_build-{build}".format(major=_major,
                                                                     minor=_minor,
                                                                     revision=_revision,
                                                                     build=_build)

    if suffix is not None:
        if suffix == Types.Alpha:
            _new_version = "{0}_{1}".format(_new_version, "Alpha")
        elif suffix == Types.Beta:
            _new_version = "{0}_{1}".format(_new_version, "Beta")
        elif suffix == Types.RC:
            _new_version = "{0}_{1}".format(_new_version, "RC")
        elif suffix == Types.GA:
            _new_version = "{0}_{1}".format(_new_version, "GA")
        elif suffix == Types.M1:
            _new_version = "{0}_{1}".format(_new_version, "M1")
        elif suffix == Types.M2:
            _new_version = "{0}_{1}".format(_new_version, "M2")
        elif suffix == Types.M3:
            _new_version = "{0}_{1}".format(_new_version, "M3")
        elif suffix == Types.SNAPSHOT:
            _new_version = "{0}_{1}".format(_new_version, "SNAPSHOT")
        elif suffix == Types.PRE:
            _new_version = "{0}_{1}".format(_new_version, "PRE")

    return _new_version


def update_init(version):
    _project_path = Path(utils.get_project_path_info().get("poseidon_path"))
    _init_path = _project_path.joinpath('__init__.py')
    with open(_init_path, 'w') as f:
        f.write("__version__ = '{}'".format(version))

def update_set_cfg_version():
    _setup_cfg_path = get_setup_cfg_handler()
    _new_version = get_new_version()
    ini_file.update_ini_info(_setup_cfg_path, "metadata", "version", _new_version)
    # 更新poseidon目录中的__init__.py文件
    update_init(_new_version)
