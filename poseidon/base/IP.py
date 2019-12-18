#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-08
"""
import socket
class IP:
    @staticmethod
    def get_host_name():
        """
        查询本机hostname
        :return:
        """
        return socket.gethostname()


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
