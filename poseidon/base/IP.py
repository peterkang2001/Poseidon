#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-08
"""
import socket
import getpass

class IP:
    @staticmethod
    def get_host_name():
        """
        查询本机hostname
        :return:
        """
        user_name = getpass.getuser()  # 获取当前用户名
        hostname = socket.gethostname()  # 获取当前主机名
        return (user_name, hostname)


    @staticmethod
    def get_host_ip():
        """
        查询本机ip地址
        :return:
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        return ip
