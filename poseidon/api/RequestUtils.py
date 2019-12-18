#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import inspect
import json
import os
import re
import threading
import time

import urllib.request, urllib.parse, urllib.error
# import urllib.request, urllib.error, urllib.parse
import requests
from multiprocessing import Pool
# from lxml import etree
# from hjAuto.api.conf.commonConf import comConf
# from hjAuto.base import commonBase
# from hjAuto.base.logLib import logLib
# from hjAuto.base import globalVariables
from requests_toolbelt import MultipartEncoder
import codecs
import logging

# try:
#     import urllib3
#     from urllib3.exceptions import InsecureRequestWarning
#
#     urllib3.disable_warnings(InsecureRequestWarning)
# except:
#     pass


class RequestUtils:
    """
    对http请求的辅助方法，如对url进行encode
    """

    def encodeUrlParams(self, params, needencode=True):
        """
        encode request parameters dict to query string, like: param1=value1&param2=value2
        eg: {"param1": "value1", "param2": None, "param3": ""} => param1=value1&param3=
        :param params: dict, request query parameters.
        :return string, like "param1=&param3=value3"
        """
        if params is not None:
            for (key, value) in list(params.items()):
                if value is None:
                    params.pop(key)

            if len(params) > 0:
                if not needencode:
                    params_str_list = []
                    for (key, value) in list(params.items()):
                        params_str_list.append(key + "=" + str(value))
                    return '&'.join(params_str_list)
                return urllib.parse.urlencode(params)

        return ''



    def composeUrl(self, base_url, sub_url, para_dict=None, needencode=True):
        url = base_url.rstrip('/') + '/' + sub_url.lstrip('/')
        paraValue = self.encodeUrlParams(para_dict, needencode) if para_dict and isinstance(para_dict, dict) else ''
        paraStr = ('?' + paraValue) if paraValue else ''
        url += paraStr

        return url


    def replace_domain_to_hostip(self, url):
        try:
            host_ips = eval(os.environ['hosts_to_ip'])
            for domain, ip_port in list(host_ips.items()):
                if url.find(domain) > 0:
                    logging('Replace domain from {0} to {1}'.format(domain, ip_port))
                    url = url.replace(domain, ip_port)
                    return url
        except:
            return url
        return url

    def rebuildurl(self, url, parameter):
        if not parameter:
            return url
        return url + "?" + urllib.parse.urlencode(parameter)


    def checkUrlStartWith(self, url, keyword):
        """
        check the URl is start with special keyword
        :param url: str
        :return flag: bool, return True if url start with keyword, otherwise return False
        """
        url = url.split(r"//")[1]
        keyword = keyword.lower()
        flag = True if url.startswith(keyword) else False
        return flag



