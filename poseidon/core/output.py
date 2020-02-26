#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-18
"""
import sys


def info(msg):
    sys.stdout.write(f"{msg}\n".center(10, '#'))


def err(msg):
    sys.stderr.write(f"{msg}\n".center(10, '#'))
