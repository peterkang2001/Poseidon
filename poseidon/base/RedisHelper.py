#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-08
"""

import logging
import redis
from pytest_testconfig import config as pyconfig
from poseidon.base.Env import Env
import json
from enum import Enum
from poseidon.base import CommonBase as cb

class Redis:
    """
    此类兼容老的通过传递channel方式获取redis 服务器连接字符串
    注意事项
    需要自定义一个类作为Redis类的一个子类，并且重写 getRedisConfig 方法
    """

    def getRedisConfig(self, channel):
        """
        根据传入的channel获取redis配置信息
        :param channel:
        :return:
        """
        logging.debug("开始读取redis配置信息")
        return None

    def delRedisValue(self, key, channel="uc"):
        """
        删除redis中的key
        :param key:
        :param channel:uc 用户中心 、nc消息中心
        :return:
        """
        try:
            if cb.can_not_do_byEnv() : return
        except:
            logging.error("无法读取Env环境参数")


        redisConfig = self.getRedisConfig(channel=channel)

        redisHost = redisConfig["host"]
        redisPort = redisConfig["port"]
        redisDb = redisConfig["db"]
        r = redis.Redis(host=redisHost, port=redisPort, db=redisDb)
        try:
            return r.delete(key)
        except Exception as e:
            logging.error(e)

    def setRedisValue(self, key, value, valueType=None, channel="uc", ttl=None):
        """
        设置redis值和value
        :param key:
        :param value:
        :param valueType: set string list hash
        :param channel: uc 用户中心 、nc消息中心
        :return:
        """
        try:
            if cb.can_not_do_byEnv() : return
        except:
            logging.error("无法读取Env环境参数")

        r = self.getRedisInstance(channel=channel)

        try:
            if valueType is None or valueType.lower() == "string":
                result = r.set(key, str(value), ex=ttl)

            elif valueType.lower() == "json":
                result = r.set(key, json.dumps(value), ex=ttl)

            elif valueType.lower() == "hash":
                for iKey, iValue in value.items():
                    result = r.hset(key, iKey, iValue)
                    logging.info("redis设置hset操作：key={0}成功{1},返回{2}".format(key, iKey, result))
                if ttl != None:
                    result = r.expire(key, ttl)
                    logging.info("redis设置hset的expire操作：key={0}成功,返回{1}".format(key, result))
                return

            elif valueType.lower() == "list":
                for iValue in value:
                    result = r.lpush(key, iValue)
                    logging.info("redis设置lpush操作：key={0}成功{1},返回{2}".format(key, iValue, result))
                if ttl != None:
                    result = r.expire(key, ttl)
                    logging.info("redis设置lpush的expire操作：key={0}成功,返回{1}".format(key, result))
                return
            logging.info("redis设置value操作：key={0}成功,返回{1}".format(key, result))
        except Exception as e:
            logging.error(e)

    def getRedisInstance(self , channel="uc"):
        logging.info("开始处理redis配置信息")
        redisConfig = self.getRedisConfig(channel=channel)
        redisHost = redisConfig["host"]
        redisPort = redisConfig["port"]
        redisDb = redisConfig["db"]
        redisPwd = redisConfig['pwd'] if 'pwd' in redisConfig.keys() else None
        r = redis.Redis(host=redisHost , port=redisPort , db=redisDb, password=redisPwd,decode_responses=True)
        #存进去的是字符串类型的数据，取出来却是字节类型的
        #由于python3的与redis交互的驱动的问题，Python2取出来的就是字符串类型的。
        #连接Redis的时候加上decode_responses=True即可
        return r

    def getRedisValue(self, key, valueType=None, channel="uc"):

        """
        获取redis存储的值
        :param key:
        :param channel:uc 用户中心 、nc消息中心
        :param type: 获取的消息类型 默认为None, string, json, hash,list
        :return:
        """
        try:
            if cb.can_not_do_byEnv() : return
        except:
            logging.error("无法读取Env环境参数")

        r = self.getRedisInstance(channel=channel)
        logging.info("开始操作redis")
        try:
            logging.info("读取key={0},valueType={1}, channel={2}".format(key, valueType, channel))
            if valueType == None or valueType.lower() == "string":
                result = str(r.get(key))

            elif valueType.lower() == "json":
                result = json.loads(r.get(key))

            elif valueType.lower() == "hash":
                result = dict(r.hgetall(key))

            elif valueType.lower() == "list":
                result = list(r.lrange(key, 0, -1))

            elif valueType.lower() == "zset":
                result = list(r.zrange(key, 0, -1))

            elif valueType.lower() == "nset":  # 普通set
                result = list(r.smembers(key))

            else:
                result = None
            logging.info("读取redis的值={0}".format(result))
            return result

        except Exception as e:
            logging.error(e)

class Redis_v2():
    """
    作为Redis的另一种实现，初始化的时候只需要传递host port db passwd等参数
    无需事先准备配置文件，用户可以在Redis类和Redis_v2类两个选择自己喜欢的方式
    """
    def __init__(self, **kwargs):
        _host = kwargs.get("host")
        _port = kwargs.get("port")
        _db = kwargs.get("db")
        _password = kwargs.get("password")
        if _password is None:
            pool = redis.ConnectionPool(host=_host, port=_port, db=_db)
        else:
            pool = redis.ConnectionPool(host=_host, port=_port, db=_db, password=_password)
        self.client = redis.Redis(connection_pool=pool)


    def getRedisValue(self, key,valueType=None):
        """
        获取redis存储的值
        :param key:
        :param channel:uc 用户中心 、nc消息中心
        :param type: 获取的消息类型 默认为None, string, json, hash,list
        """
        try:
            if cb.can_not_do_byEnv() : return
        except:
            logging.error("无法读取Env环境参数")

        logging.info("开始操作redis")
        try:
            logging.info("读取key={0},valueType={1}".format(key, valueType))
            if valueType == None or valueType.strip().lower() == "string":
                result = str(self.client.get(key))

            elif valueType.strip().lower() == "json":
                result = json.loads(self.client.get(key))

            elif valueType.strip().lower() == "hash":
                result = dict(self.client.hgetall(key))

            elif valueType.strip().lower() == "list":
                result = list(self.client.lrange(key , 0 , -1))

            elif valueType.strip().lower() == "zset":
                result = list(self.client.zrange(key , 0 , -1))

            elif valueType.strip().lower() == "nset":  # 普通set
                result = list(self.client.smembers(key))

            else:
                result = None

            logging.info("读取redis的值={0}".format(result))
            return result

        except Exception as e:
            logging.error(e)

    def delRedisValue(self, key):
        try:
            if cb.can_not_do_byEnv() : return
        except:
            logging.error("无法读取Env环境参数")

        try:
            _key = key.strip()
            _resp_code = self.client.delete(_key)
            resp = "成功!!" if _resp_code == 1 else "失败!!"
            logging.debug("redis 删除key={0}, 结果{1}".format(_key,resp))
        except Exception as e:
            logging.error(e)

    def setRedisValue(self, key, value, valueType=None, ttl=None):
        """
         设置redis值和value
         :param key:
         :param value:
         :param valueType: set string list hash
         """
        try:
            if cb.can_not_do_byEnv() : return
        except:
            logging.error("无法读取Env环境参数")

        try:
            if valueType is None or valueType.strip().lower() == "string":
                result = self.client.set(key, str(value), ex=ttl)
            elif valueType.strip().lower() == "json":
                result = self.client.set(key, json.dumps(value), ex=ttl)
            elif valueType.strip().lower() == "hash":
                for iKey, iValue in value.items():
                    result = self.client.hset(key, iKey, iValue)
                    logging.info("redis设置hset操作：key={0}成功{1},返回{2}".format(key, iKey, result))
                if ttl != None:
                    result = self.client.expire(key, ttl)
                    logging.info("redis设置hset的expire操作：key={0}成功,返回{1}".format(key, result))
            elif valueType.strip().lower() == "list":
                for iValue in value:
                    result = self.client.lpush(key, iValue)
                    logging.info("redis设置lpush操作：key={0}成功{1},返回{2}".format(key, iValue, result))
                if ttl != None:
                    result = self.client.expire(key, ttl)
                    logging.info("redis设置lpush的expire操作：key={0}成功,返回{1}".format(key, result))
                return
            logging.info("redis设置value操作：key={0}成功,返回{1}".format(key, result))

        except Exception as e:
            logging.error(e)


    def bytes_to_str(self,data):
        """
        redis resp转码辅助方法
        python3 从redis中取值会得到bytes类型结果
        可以用该方法将结果从bytes-> string
        """

        if isinstance(data, bytes):
            return data.decode()

        if isinstance(data, dict):
            return dict(map(self.bytes_to_str, data.items()))

        if isinstance(data, tuple):
            return map(self.bytes_to_str, data)

        return data

    def str_to_bytes(self, data):
        if isinstance(data, str):
            return bytes(str, encoding='utf8')

        if isinstance(data, dict):
            return dict(map(self.str_to_bytes, data.items()))

        if isinstance(data, tuple):
            return map(self.str_to_bytes, data)

        if isinstance(data, list):
            return [self.str_to_bytes(i) for i in data]
