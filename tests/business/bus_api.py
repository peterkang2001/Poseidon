# coding=utf-8

"""
@author:songmengyun
@file: bus_api.py
@time: 2019/12/17

"""
import logging
from poseidon.api.RequestUtils import RequestUtils
from poseidon.api.RequestsHelper import Requests
from poseidon.base import CommonBase as cb




class BusBase(RequestUtils, Requests):

    def get_url(self, subUrl=None, baseUrl=None, queryDict=None, needencode=False):
        url = self.composeUrl(baseUrl, subUrl, queryDict, needencode)
        logging.info("url:%s" % url)
        return url

    def send_music_and_respnse(self, send_data, check_point, status_exp=0, http_status=200):
        url = send_data.get('url')
        method = send_data.get('method')
        headers = send_data.get('headers')
        logging.info("[APNSUrl] %s" % (url))
        resp_act = super().sendRequest(method=method, url=url, headers=headers, httpStatusExp=http_status,
                                       statusExp=status_exp)
        cb.checkPartInDict(check_point, resp_act)



bus_base = BusBase()
