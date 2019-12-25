#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-12-25
"""

from enum import Enum


class Types(Enum):
    # 采取 GNU 风格版本号
    Major = "Major",  # 主版本号
    Minor = "Minor",  # 次版本号
    Revision = "Revision",  # 修订版本号
    Build = "Build",  # 内部版本号

    Alpha = "Alpha",  # 是内部测试版,一般不向外部发布,会有很多Bug.一般只有测试人员使用
    Beta = "Beta",  # 给用户测试的版本，这个阶段的版本会一直加入新的功能，修改用户反馈的bug
    RC = "Release　Candidate",  # 用在软件上就是候选版本。系统平台上就是发行候选版本。RC版不会再加入新的功能了，主要着重于除错。
    GA = "GA",  # 正式发布的版本
    M1 = "Milestone 1",  # 里程碑版本，其中X是一个递增数字
    M2 = "Milestone 2",
    M3 = "Milestone 3",
    SNAPSHOT = "SNAPSHOT",  # 快照版本
    PRE = "预览版",  # 预览版
