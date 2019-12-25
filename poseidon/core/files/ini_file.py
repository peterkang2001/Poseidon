#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-25
"""
import configparser
from poseidon.core.output import *


def get_ini_info(file, section, key):
    config = configparser.ConfigParser()
    config.read(file, encoding="utf-8")
    _value = config.get(section, key)
    return _value


def update_ini_info(file, section, key, value):
    try:
        config = configparser.ConfigParser()
        config.read(file, encoding="utf-8")
        config.set(section, key, value)
        config.write(open(file, "w"))

    except Exception as e:
        err(e)
