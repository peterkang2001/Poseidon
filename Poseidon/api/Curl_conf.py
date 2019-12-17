#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-07
"""


class Curl_conf:

    @property
    def default_header_template_1_pycurl(self):
        _header = ["hj_appkey: 8995b7abe8e0a8cb7f673fdc7b94f029",
                 "Content-Type: application/json" ]
        return _header

    @property
    def default_header_template_2_pycurl(self):
        _header = ["monitor-hj: 7BCDB077276BEC8A9D2CE39548B5D57E",
                "Content-Type: application/json"]
        return _header

    @property
    def useragent_firefox_pc(self):
        return "Mozilla/5.2 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50324)"


    @property
    def default_http_template_1(self):
        _tmp = {"CONNECTTIMEOUT": 5,        # 连接等待时间，0则不等待
                "TIMEOUT": 120,             # 超时时间
                "MAXREDIRS": 5,             # 指定HTTP重定向最大次数
                "FORBID_REUSE": 1,          # 完成交互后强制断开连接，不重用
                "DNS_CACHE_TIMEOUT": 60     # 设置DNS信息保存时间，默认为120秒
                }








