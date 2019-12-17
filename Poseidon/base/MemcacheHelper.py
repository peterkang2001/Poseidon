#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-08
"""

import logging
from pymemcache.client.base import Client

class Memcache:
    def getMemcacheConfig(self , configkey):
        """
        根据传入的channel获取memcache配置信息
        :param channel:
        :return:
        """
        pass

    def getMemcache(self, configkey, key, MessagePack=False, **kwargs):
        try:
            result = None
            clients = self.getMemcacheConfig(configkey)
            for client_conf in clients:
                client = Client(client_conf)
                result = client.get(key=key)
                if result is not None:
                    break
            logging.info("读取memcache的key={0},value={1}".format(key,result))
            return result
        except Exception as e:
            logging.error(e)

    def delMemcache(self, configkey, key, **kwargs):
        try:
            clients = self.getMemcacheConfig(configkey)
            for client_conf in clients:
                client = Client(client_conf)
                result = client.get(key=key)
                if result is not None:
                    result = client.delete(key=key)
            logging.info("删除memcache的key={0}，操作结果={1}".format(key, result))
        except Exception as e:
            logging.error(e)
