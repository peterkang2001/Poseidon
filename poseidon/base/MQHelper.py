#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-08
"""

import logging
import base64
from poseidon.api.RequestsHelper import Requests

class MessageQueue:
    request = Requests()

    def getRabbitMqConfig(self, configKey):
        if True:
            mqConfig = ""
        else:
            mqConfig = None
            logging.error("请输入正确的configKey")
        logging.info("获取mq配置信息:{0}".format(mqConfig))
        return mqConfig

    def cleanRabbitMqQueueMessages(self, configKey):
        """
        删除指定消息队列中的所有数据
        :param configKey: 在base.py中配置文件中关于消息队列的key
        :return:
        """
        configInfo = self.getRabbitMqConfig(configKey)

        userName = configInfo.get("username" , False)
        password = configInfo.get("password" , False)
        server = configInfo.get("server" , False)
        port = configInfo.get("port" , False)
        vhost = configInfo.get("vhost" , False)
        queue = configInfo.get("queue" , False)

        headers = ['authorization:{}'.format(self.getBasicAuth(userName, password))]
        url = "http://{0}:{1}/api/queues/{2}/{3}/contents".format(server, port, vhost, queue)

        # resp = self.request.sendRequest(url=url, method="DELETE", headers=headers,needJson=False, httpStatusExp=204)
        resp = self.request.sendRequest(url=url, method="DELETE", headers=headers,needJson=False)

        # 由于curl暂时不支持status_code 先注释掉
        # if resp.status_code == 204:  # 返回状态为204表示请求成功
        #     logging.info('status_code is 204, 清除RabbitMq消息队列成功')
        #     return True
        # else:
        #     logging.info('status_code is {0}, 清除RabbitMq消息队列失败', resp.status_code)
        #     return False

    def getRabbitMqQueueMessages(self, configKey):
        """
        返回存在消息队列中的数据，
        注意事项：
        1.当消息队列中没有数据会返回一个空list
        2.调用此方法不会影响消息队列中的数据
        :return:list
        """

        configInfo = self.getRabbitMqConfig(configKey)

        userName = configInfo.get("username", False)
        password = configInfo.get("password", False)
        server = configInfo.get("server", False)
        port = configInfo.get("port", False)
        vhost = configInfo.get("vhost", False)
        queue = configInfo.get("queue", False)


        headers = ['authorization:{}'.format(self.getBasicAuth(userName, password))]
        url = "http://{0}:{1}/api/queues/{2}/{3}/get".format(server, port, vhost, queue)
        # data = {"count": 5000, "requeue": True, "encoding": "auto", "truncate": 50000}   # 旧版本MQ
        data = {"count":5,"ackmode":"ack_requeue_true","encoding":"auto","truncate":50000}   # 新版本MQ
        resp = self.request.sendRequest(url=url, method="POST", headers=headers, data=data, needJson=True, httpStatusExp=200)
        return resp

    def getBasicAuth(self, userName, password):
        """
        返回BasicAuth的值
        :param userName:
        :param password:
        :return:
        """
        token = "{0}:{1}".format(userName, password)
        base64string = base64.encodestring(token.encode(encoding="utf-8"))[:-1]

        authheader = "Basic %s" % base64string.decode(encoding="utf-8")
        return authheader
